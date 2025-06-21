import socket

# Replace with server's IP address
server_ip = input("Enter Server IP: ")  # eg: 192.168.0.105 same server kum client same ip irruntha matum thaan run akum code a
port = 12345

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket.af_inet-ip address,socket.sock_stream-tcp
client_socket.connect((server_ip, port))#connect pannu (server_ip-ip address .port-port number)

print(f"[CONNECTED] Connected to server {server_ip}:{port}")

# Communicate
while True:
    msg = input("You: ")
    client_socket.send(msg.encode())#msg send panrom sencodela  client to server ku
    if msg.lower() == 'exit':
        break
    data = client_socket.recv(1024).decode()#server la vantha message receieve panrom
    print(f"Server: {data}")

# Close connection
client_socket.close()
