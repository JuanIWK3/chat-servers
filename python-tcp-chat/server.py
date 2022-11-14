import socket
from _thread import *

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = '127.0.0.1'
port = 8080

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
s.listen(5)


def multi_threaded_client(conn):
    while True:
        data = conn.recv(2048)
        if not data:
            break
        print(data.decode('utf-8'), end="")
    conn.close()


while True:
    Client, address = s.accept()
    start_new_thread(multi_threaded_client, (Client, ))
s.close()
