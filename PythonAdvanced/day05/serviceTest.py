#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-20'

import socket

ip = ("127.0.0.1",1000)

# 创建socket对象
sk = socket.socket()
# 绑定IP
sk.bind(ip)
# 监听 看有没有请求过来
sk.listen()
print("服务启动了")
# 等待连接
# 等回到连接之后，会返回一个套接字对象和客户端IP地址、端口号等
conn,addr = sk.accept()
print("客户端的IP地址是：",addr)

# 接收消息
client_data = conn.recv(1024).decode("utf8")
print("客户端：",client_data)

send_data = input(">>>>")
conn.sendall(send_data.encode("utf8"))

conn.close()
sk.close()
