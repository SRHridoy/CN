import socket
import threading

HOST = '127.0.0.1'
PORT = 5002

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print("Chat Server started. Waiting for clients...")

clients = []

def handle_client(conn, addr):
    print(f"New connection: {addr}")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if msg:
                print(f"{addr}: {msg}")
                for client in clients:
                    if client != conn:
                        client.send(f"{addr}: {msg}".encode())
            else:
                break
        except:
            break
    conn.close()
    clients.remove(conn)
    print(f"Disconnected: {addr}")

while True:
    conn, addr = server_socket.accept()
    clients.append(conn)
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
