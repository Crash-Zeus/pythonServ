import threading
import socket
import time
import select

class ClientThread(threading.Thread):

    def __init__(self, host, port, clientsocket):

        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.clientsocket = clientsocket
        print("[+] New thread for %s %s" % (self.host, self.port, ))

    def run(self): 
        print("Connection of %s %s" % (self.host, self.port, ))
        request = self.clientsocket.recv(2048)
        print(request.decode())
        self.clientsocket.send("Server ok -".encode())


port = 1111

mainConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mainConnection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mainConnection.bind(("",1111))

clientConnected = []
serverUp = True

while serverUp == True:
    mainConnection.listen(10)
    print( "listening on %s" % (port))
    (clientsocket, (host, port)) = mainConnection.accept()
    newthread = ClientThread(host, port, clientsocket)
    newthread.start()