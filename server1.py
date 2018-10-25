#!usr/bin/python
# -*- coding:utf-8 -*-
# 文件名:server1.py
import socket
host = 'localhost'
port = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print("Connected by ", addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)


