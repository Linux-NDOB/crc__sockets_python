import socket, json, time
from logic import crc 

class ServerSocket():
    def __init__(self, server_ip= '127.0.0.1', port= 9000) -> None:
        try:
            self.server = socket.socket()
            self.port = port
            self.server_ip = server_ip
            self.server.bind((str(self.server_ip), int(self.port)))
            self.server.listen(1)

        except Exception as e:
            print(f'Error: {e}')
        
    def start_server(self):
        try:
            self.server.close()
            time.sleep(1)

            self.server = socket.socket()
            self.server.bind((str(self.server_ip), int(self.port)))
            self.server.listen(1)

            client, _ = self.server.accept() 

            generator = client.recv(1024).decode()

            data = client.recv(1024).decode()

            data , crc_code = data.split(' ') 

            result = crc(data, generator, crc_code)

            result_to_int = int(result)

            response = {
                    'state': 'Error, reenvie la trama nuevamente',
                    } if int(result_to_int) != 0 else {
                            'message': data + crc_code,
                            'state': 'La informacion ha llegado integra',
                            'result': result,
                            'generator': generator,
                            'crc_code': crc_code,
                            }  
            response_to_string = json.dumps(response)
        
            client.send(response_to_string.encode('utf-8'))

            client.close()

            self.server.close()        

        except Exception as e:
            print(f'Error {e}')
            return

    def close(self):
        self.server.close()
                    
