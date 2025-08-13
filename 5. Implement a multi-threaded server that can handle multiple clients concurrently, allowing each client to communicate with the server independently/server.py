import socket
import threading

HOST = 'localhost'
PORT = 12345

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"[{addr}] {data}")
            conn.sendall(f"Server received: {data}".encode())
        except:
            break
    conn.close()
    print(f"[DISCONNECTED] {addr} disconnected.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
