# -*- coding: utf-8 -*-
# TCP-Client
 
import socket
 
address = ('127.0.0.1', 10140)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
 
while True:
    message = raw_input()
    if not message:
        break
    s.send(message)
    data = s.recv(512)
    print 'server:', data
 
s.close()