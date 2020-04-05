#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-03-15'

# with open("./a.txt","w",encoding='utf8') as f:
#     f.write("落红不是无情物，化作春泥更护花")
#
# with open("a.txt","r",encoding='utf8')as file:
#     print(file.read())

with open("../b.txt","wb")as ff:
    ff.write("美人卷珠帘".encode("big5"))

with open("../b.txt","rb") as f:
    print(f.read().decode('big5'))
