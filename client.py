import socket

host = 'localhost'
port = 12800

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((host, port))
print("Connection established with the server on port {}".format(port))
print("For close connection write 'end'")

sendingMesg = ""
while sendingMesg != b"end":
    sendingMesg = input(">>> ")
    # Sometimes goes crash with special char
    sendingMesg = sendingMesg.encode()
    connection.send(sendingMesg)
    receivingMsg = connection.recv(1024)
    print(receivingMsg.decode())

print("Closing connection")
connection.close()