import threading
import socket
import time
import select

serverUp = True
class ClientThread(threading.Thread):

    def __init__(self, host, port, clientsocket):

        threading.Thread.__init__(self)
        self.host = host
        self.port = port
        self.clientsocket = clientsocket
        print("[+] New thread for %s %s" % (self.host, self.port, ))

    def run(self): 
        print("Connection of %s %s" % (self.host, self.port, ))
        while serverUp == True:
            try:
                request = self.clientsocket.recv(2048)
            except Exception as e:
                pass
            if request.decode() != "end":
                    print(request.decode())
                    try:
                        self.clientsocket.send("Server ok -".encode())
                    except Exception as e:
                        print("[-] Thread killed for %s %s" % (self.host, self.port))
                        self.clientsocket.close()
                        self.killed = True
                        break


port = 1111

mainConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mainConnection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mainConnection.bind(("",1111))

while serverUp == True:
    try:
        mainConnection.listen(10)
        print( "listening on %s" % (port))
        (clientsocket, (host, port)) = mainConnection.accept()
        newthread = ClientThread(host, port, clientsocket)
        newthread.start()
    except KeyboardInterrupt:
        newthread._stop()