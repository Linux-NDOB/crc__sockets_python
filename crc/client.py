import socket, json
from logic import crc

class ClientSocket():
    def __init__(self, server_ip= '127.0.0.1', port = 9000) -> None:
        self.server_ip = server_ip        
        self.port = port
        self.my_socket = socket.socket()

    def connect(self):
        try:    
            self.my_socket.connect((str(self.server_ip), int(self.port))) 
        except Exception as e:
            print(f'Error: {e}')
            return

    def send_data(self, generator, data):
        try:
            self.my_socket.send(generator.encode())

            crc_code = crc(data, generator) 

            request = data + ' ' + crc_code

            self.my_socket.send(request.encode())

            answer = self.my_socket.recv(1024)

            answer_to_dict = json.loads(answer)

            self.close()

            return crc_code, answer_to_dict

        except Exception as e:
            print(f'Error {e}')
            return

    def close(self):
        self.my_socket.close()
        

