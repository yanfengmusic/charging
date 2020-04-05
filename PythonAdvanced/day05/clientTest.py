#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-20'

import socket

sk = socket.socket()

sk.connect(("127.0.0.1",1000))

send_data = input(">>>>")

sk.sendall(send_data.encode("utf8"))

server_data = sk.recv(1024).decode("utf8")
print("客户端：",server_data)

sk.close()
