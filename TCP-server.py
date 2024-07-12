#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 4444

serversocket.bind(('192.168.0.45', port))
serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    
    print(f"received connection from {str(address)}")
    
    message = 'You are connected to the server' + "\r\n"
    clientsocket.send(message.encode())
    
    clientsocket.close()
    