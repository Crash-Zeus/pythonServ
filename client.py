import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(('localhost', 12800))
message = connection.recv(1024)
print(message)