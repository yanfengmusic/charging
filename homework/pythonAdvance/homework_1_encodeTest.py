#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-15'

import os
with open("./gbk编码.txt","r",encoding="gbk")as f,\
     open("./utf8编码.txt", "r", encoding="utf8")as f1:
    # read后，自动转化成unicode
    data_gbk = f.read()
    print(type(data_gbk))

    data_utf8 = f1.read()
    print(type(data_utf8))

content = data_gbk + data_utf8
with open("./re.txt","w",encoding="utf8") as f1:
    f1.write(content)

new_name = input("请出入：请输入新文件的名称")
os.rename("./re.txt",f"{new_name}"+".txt")
