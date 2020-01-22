import socket

host = ''
port = 12800

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind((host,port))
connection.listen(5)

print("Server up, listen on port {}".format(port))

clientConnection, infoConnection = connection.accept()

receivingMesg = ""

while receivingMesg != b"fin":
    receivingMesg = clientConnection.recv(1024)
    # Exeption if message with accent
    print(receivingMesg.decode())
    clientConnection.send(b"5/5")

print("Closing connection")
clientConnection.close()
connection.close()