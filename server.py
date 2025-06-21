import socket

# Get server IP and port
host = socket.gethostbyname(socket.gethostname())  # LAN IP of the server
port = 12345

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket.af_inet-ip address,socket.sock_stream-tcp
server_socket.bind((host, port))##bimn -add(router_ip-ip addr.port-port number)
server_socket.listen(5)## server to client listen 5 mins

print(f"[SERVER STARTED] Listening on {host}:{port}...")

# Accept connections
client_socket, client_address = server_socket.accept()## cllient server accept aichuna
print(f"[CONNECTED] Client connected from {client_address}")

# Communicate
while True:
    data = client_socket.recv(1024).decode()#client message server vanthurkum athu  receive airukum athukaporam athu decode panrom,
    if data.lower() == 'exit':#disconnect aichuna exit airum
        print("Client disconnected.")
        break
    print(f"Client: {data}")
    msg = input("You: ")
    client_socket.send(msg.encode())#nama message send panrom encode formatla

# Close connection
client_socket.close()
server_socket.close()
