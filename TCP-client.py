#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.0.45'

port = 4444

clientsocket.connect(('192.168.0.45', port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode())

