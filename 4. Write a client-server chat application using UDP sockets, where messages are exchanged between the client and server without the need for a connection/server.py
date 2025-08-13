import socket

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    print(f"UDP Server listening on {HOST}:{PORT} ...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()
        print(f"Client: {message}")
        reply = input("Message From Server: ")
        server_socket.sendto(reply.encode(), addr)
