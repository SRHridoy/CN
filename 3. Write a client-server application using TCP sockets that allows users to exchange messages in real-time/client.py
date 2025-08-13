import socket

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = input("Enter a message: ")
    s.sendall(message.encode())
    data = s.recv(1024)
    print("Echo from server:", data.decode())
