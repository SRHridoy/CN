import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
data = client_socket.recv(1024).decode()
print("Current Date & Time from Server:", data)
client_socket.close()
