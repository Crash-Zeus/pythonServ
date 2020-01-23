import socket
from time import gmtime, strftime

host = 'localhost'
port = 12800
time = strftime("%H:%M:%S", gmtime()).encode()


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((host, port))
print("Connection established with the server on port {}".format(port))
print("For close connection write 'end'")

sendingMesg = ""
while sendingMesg != b"end":
    sendingMesg = input(">>> ")
    # Sometimes goes crash with special char
    sendingMesg = sendingMesg.encode()
    connection.send(sendingMesg + " à ".encode() + time)
    receivingMsg = connection.recv(1024)
    print(receivingMsg.decode())

print("Closing connection")
connection.close()