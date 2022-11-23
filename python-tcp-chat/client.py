import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("", 8080))

name = ""
while name == "":
    name = input("Enter your name: ")

while True:
    msg = input("%s: " % name)

    msg = name + ": " + msg

    client.send(msg.encode())
