import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5090))

while True:
    data = input("Enter data to send: ")
    client_socket.send(data.encode())

    server_data = client_socket.recv(1024)
    if (server_data == ''):
        break
    if (data == 'bye'):
        break
    print('[+] Server sent:', server_data.decode())

client_socket.close()
print("[+] Server Disconnected.")