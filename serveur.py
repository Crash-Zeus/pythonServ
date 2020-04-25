from colorama import Fore, Back, Style
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
        loading(0, 10)
        print("Connection of %s %s" % (self.host, self.port, ))
        while serverUp == True:
            try:
                request = self.clientsocket.recv(2048)
            except Exception:
                pass
            if request.decode() != "end":
                print(request.decode())
                try:
                    self.clientsocket.send("Server ok -".encode())
                except Exception:
                    print("[-] Thread killed for %s %s" %
                          (self.host, self.port))
                    self.clientsocket.close()
                    self.killed = True
                    break

def loading(valmin, valmax):
    begin = "["
    close = "]"
    bar = [
        " =     ",
        "  =    ",
        "   =   ",
        "    =  ",
        "     = ",
        "      =",
        "     = ",
        "    =  ",
        "   =   ",
        "  =    ",
    ]
    while valmin != valmax:
        print(Fore.WHITE+begin+Fore.RED+bar[valmin % len(bar)]+Fore.WHITE+close, end="\r")
        time.sleep(.1)
        valmin += 1
    else:
        print(Fore.GREEN+"Server up !"+Style.RESET_ALL)


if __name__ == "__main__":
    serverUp = True
    port = 1112
    if serverUp == True:
        loading(0, 10)
    mainConnection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mainConnection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    mainConnection.bind(("", port))

    while serverUp == True:
        try:
            mainConnection.listen(10)
            print("listening on %s" % (port))
            # Séparer sur un thread différent pour l'écoute en arrière plan avec tkinter
            (clientsocket, (host, port)) = mainConnection.accept()
            newthread = ClientThread(host, port, clientsocket)
            newthread.start()
            if newthread is None:
                row = input(">>> ")
                if row == "stop":
                    try:
                        newthread._stop()
                    except Exception:
                        pass
                    serverUp = False
        except KeyboardInterrupt:
            try:
                newthread._stop()
            except Exception:
                # Catach & pass exception with none thread open
                pass
            print()
            print("Closing server")
            serverUp = False
