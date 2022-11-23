import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("", 8080))

while True:

    msg = input("you:")

    client.send(msg.encode())
