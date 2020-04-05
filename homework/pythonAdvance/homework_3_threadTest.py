#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-22'

# 先阅读下面关于Python requests 库的文章 ，了解 使用它去获取一个网页内容的方法。
# http://cn.python-requests.org/zh_CN/latest/user/quickstart.html
# 然后编写一个python程序，创建两个子线程，分别到下面的网址获取文本内容
# http://mirrors.163.com/centos/6/isos/x86_64/README.txt
# http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt
# 主线程等待这个两个子线程获取到信息后，将其内容依次合并后存入名为 readme89.TXT 的文件中


import requests,threading


url_thread1 = "http://mirrors.163.com/centos/6/isos/x86_64/README.txt"
url_thread2 = "http://mirrors.163.com/centos/7/isos/x86_64/0_README.txt"


new_str = ""
def get_intenet_content(url):
    global new_str
    content = requests.get(url)
    new_str += content.text
    return new_str

t1 = threading.Thread(target=get_intenet_content,args=[url_thread1])
t2 = threading.Thread(target=get_intenet_content,args=[url_thread2])
t1.start()
t2.start()
t1.join()
t2.join()

with open("./readme89.TXT","w") as file:
    file.write(new_str)


