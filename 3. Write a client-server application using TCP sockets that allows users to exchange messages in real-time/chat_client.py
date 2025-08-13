import socket
import threading

HOST = '127.0.0.1'
PORT = 5002

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg:
                print(msg)
        except:
            break

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    message = input()
    if message.lower() == "exit":
        break
    client_socket.send(message.encode())

client_socket.close()
