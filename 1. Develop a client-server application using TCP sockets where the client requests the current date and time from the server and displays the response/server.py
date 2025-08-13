import socket
import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print("Server is listening on port 12345...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connected with {client_address}")
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    client_socket.send(current_datetime.encode())
    client_socket.close()
