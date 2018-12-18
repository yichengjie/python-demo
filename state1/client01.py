#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket
host = 'localhost'

port = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
print('Received', repr(data))
