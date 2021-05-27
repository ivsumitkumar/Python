import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5090))

server_socket.listen(13)
print("[+] Listening for connections on 127.0.0.1:5090..")

while True:

    conn, addrs = server_socket.accept()
    print("Got a connection from {}".format(addrs))

    while True:

        data = conn.recv(1024)
        if (data.decode() == 'bye'):
            break
        print("[+] client sent:", data.decode())

        server_data = input("Reply to client: ")
        conn.send(server_data.encode())

    conn.close()
    print("[+] Client Disconnected.")
