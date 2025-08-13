import socket
import threading

HOST = 'localhost'
PORT = 12345

def handle_client(conn, addr):
    print(f"Connected with {addr}")
    while True:
        try:
            message = conn.recv(1024).decode()
            if not message:
                break
            print(f"Client: {message}")
        except:
            break
    conn.close()

def send_messages(conn):
    while True:
        try:
            msg = input("")
            conn.sendall(msg.encode())
        except:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT} ...")
    conn, addr = s.accept()
    threading.Thread(target=handle_client, args=(conn, addr)).start()
    threading.Thread(target=send_messages, args=(conn,)).start()
