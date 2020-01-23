import socket
import select

host = ''
port = 12800

mainConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mainConnection.bind((host,port))
mainConnection.listen(5)

print("Server up, listen on port {}".format(port))

clientConnected = []
serverUp = True


while serverUp == True:
    # Testing connection request, check for 50ms
    request, wlist, xlist = select.select([mainConnection], [], [], 0.05)

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
            if receivingMesg != b"end":
                # Pass into allways
                connectionClient.send("-- Server message receiving is : \"".encode() + receivingMesg + "\" --".encode())
            if receivingMesg == b"end":
                serverUp = False

if serverUp == False:
    print("Closing connection")

    for client in clientConnected:
        client.close()

    mainConnection.close()