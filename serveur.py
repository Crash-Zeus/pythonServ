import socket
import select

host = ''
port = 12800

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind((host,port))
connection.listen(5)

print("Server up, listen on port {}".format(port))

clientConnected = []
serverUp = True

while serverUp == True:
    # Testing connection request, check for 50ms
    request, wlist, xlist = select.select([connection], [], [], 0.05)

    for connection in request:
        connectionClient, infoConnection = connection.accept()
        # Store connection in client conneted list
        clientConnected.append(connectionClient)

    clientToRead = []
    try:
        clientToRead, wlist, xlist = select.select(clientConnected, [], [], 0.05)
    except select.error:
        pass
    else:
        for client in clientToRead:
            receivingMesg = connectionClient.recv(1024)
            print("Sending from {} : ".format(infoConnection)+receivingMesg.decode())
            connectionClient.send(b"-- server receiving ok --")
            if receivingMesg == "end":
                serverUp = False

print("Closing connection")
for client in clientConnected:
    client.close()

connection.close()