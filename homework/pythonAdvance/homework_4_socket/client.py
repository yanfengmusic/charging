#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-24'

import socket
sk = socket.socket()
sk.connect(("127.0.0.1",13000))

my_name = "liyanfeng"

def handleData(data):
    # 处理消息第二部分吗
    if data == "name":
        dataType = "1"
    else:
        dataType = "2"

    #     处理消息第一部分
    str_len = len(data) + 7
    if len(str(str_len)) < 4:
        data_len = "0" * (4 - len(str(str_len))) + str(str_len)
    else:
        data_len = str(str_len)

    return data_len + "|" + dataType + "|" + data

# 先自报家门
sk.sendall(handleData(my_name).encode("utf8"))
sk.recv(1024)

while True:
    client_Data = input(">>>>>")
    sk.sendall(handleData(client_Data).encode("utf8"))

    if "exit" in client_Data:
        break
    server_data = sk.recv(1024).decode("utf8")
    print("服务端：",server_data)
