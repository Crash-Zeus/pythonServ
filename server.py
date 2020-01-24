from colorama import Fore, Back, Style
import threading
import socket
import time
import select
import tkinter as tk


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


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Btn start server
        self.start = tk.Button(self)
        self.start["text"] = "Start server"
        self.start["command"] = self.startServ
        self.start.pack(side="top")
        # Quit button
        self.quit = tk.Button(self, text="Close", fg="black",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def loading(self, valmin, valmax):
        bar = [
            " [=     ]",
            " [ =    ]",
            " [  =   ]",
            " [   =  ]",
            " [    = ]",
            " [     =]",
            " [    = ]",
            " [   =  ]",
            " [  =   ]",
            " [ =    ]",
        ]
        
        while valmin != valmax:
            print(bar[valmin % len(bar)], end="\r")
            time.sleep(.2)
            valmin += 1
        else:
            print("")
            print(Back.GREEN+"Server up !")
    # On click start server

    def startServ(self):
        print("Starting server ")
        self.loading(0,5)


        


root = tk.Tk()
app = Application(master=root)
app.mainloop()
