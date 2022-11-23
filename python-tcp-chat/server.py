import socket
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = ""
port = 8080

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening on port %s..' % port)
s.listen(5)


def multi_threaded_client(conn):
    while True:
        data = conn.recv(1024)
        print(data.decode('utf-8'))
    conn.close()


while True:
    Client, address = s.accept()
    start_new_thread(multi_threaded_client, (Client, ))
