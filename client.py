import socket


server_ip = input("Enter Server IP: ")
port = 12345


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, port))

print(f"[CONNECTED] Connected to server {server_ip}:{port}")


while True:
    msg = input("You: ")
    client_socket.send(msg.encode())
    if msg.lower() == 'exit':
        break
    data = client_socket.recv(1024).decode()
    print(f"Server: {data}")


client_socket.close()
