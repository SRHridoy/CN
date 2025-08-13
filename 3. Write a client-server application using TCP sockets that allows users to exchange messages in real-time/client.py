import socket
import threading

HOST = 'localhost'
PORT = 12345

def receive_messages(s):
    while True:
        try:
            message = s.recv(1024).decode()
            if not message:
                break
            print(f"Server: {message}")
        except:
            break

def send_messages(s):
    while True:
        try:
            msg = input("")
            s.sendall(msg.encode())
        except:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    threading.Thread(target=receive_messages, args=(s,)).start()
    threading.Thread(target=send_messages, args=(s,)).start()
