import socket


host = socket.gethostbyname(socket.gethostname())  
port = 12345


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

print(f"[SERVER STARTED] Listening on {host}:{port}...")


client_socket, client_address = server_socket.accept()
print(f"[CONNECTED] Client connected from {client_address}")

# Communicate
while True:
    data = client_socket.recv(1024).decode()
    if data.lower() == 'exit
        print("Client disconnected.")
        break
    print(f"Client: {data}")
    msg = input("You: ")
    client_socket.send(msg.encode())

client_socket.close()
server_socket.close()
