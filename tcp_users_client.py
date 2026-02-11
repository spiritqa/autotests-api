import socket


client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address_server = ('localhost', 12345)
client_socket.connect(address_server)

message = "Привет, сервер!"
client_socket.send(message.encode())

server_massage = client_socket.recv(1024).decode()
print(server_massage)

client_socket.close()

