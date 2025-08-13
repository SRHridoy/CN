import socket

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    while True:
        msg = input("Reply from Client: ")
        client_socket.sendall(msg.encode())
        data = client_socket.recv(1024).decode()
        print(data)
