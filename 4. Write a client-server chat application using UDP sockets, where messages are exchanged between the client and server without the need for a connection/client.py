import socket

SERVER_HOST = 'localhost'
SERVER_PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    while True:
        msg = input("Message from Client: ")
        client_socket.sendto(msg.encode(), (SERVER_HOST, SERVER_PORT))
        data, addr = client_socket.recvfrom(1024)
        print(f"Server: {data.decode()}")
