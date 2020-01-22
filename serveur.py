import socket

host = ''
port = 12800

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind((host,port))
connection.listen(5)

print("Server up, listen on port {}".format(port))