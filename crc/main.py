from client import ClientSocket
from server import ServerSocket
import threading, json
from time import sleep

class MainClass():
    def __init__(self) -> None:
        self.client_socket = ClientSocket()
        self.server_socket = ServerSocket()

    def run_server_in_thread(self, server_socket):
        try:
            server_socket.start_server()
        except Exception as e:
            print(f'Error: {e}')
            return

    def start_server(self):
        print("Iniciando servidor...")
        server_thread = threading.Thread(target=self.run_server_in_thread, args=(self.server_socket,))
        server_thread.start()
        sleep(1)

    def start_client(self):
           print('Iniciando Cliente... \n')
           sleep(1)
           self.client_socket.connect()
           
           print('Bienvenido al menu principal, porfavor rellene los datos requeridos')
            
           required_gen = input('Porfavor ingrese el polinomio generador(binario): ')

           required_data = input('Porfavor ingrese la trama a enviar: ')

           _, answer_to_json = self.client_socket.send_data(required_gen, required_data)

           print(f"""\n Se ha enviado la siguiente informacion al servidor:
                  Generador: {required_gen}
                  Trama: {required_data}
                  """)

           print(f"""Esta es la respuesta del servidor:
                  Mensaje: {answer_to_json['data']}
                  Generador: {answer_to_json['generator']}
                  CRC: {answer_to_json['crc_code']}
                  Resultado: {answer_to_json['result']}
                  Respuesta: {answer_to_json['state']}""")

    def run_client(self):
       while True:
           try:
            self.start_server() 
            self.start_client()

           except KeyboardInterrupt as e:
               print(f'Error: {e}')
               self.client_socket.close()
               self.server_socket.close()
               break
       
if __name__ == "__main__":
    main = MainClass()
    main.run_client()
