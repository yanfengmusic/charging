#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-03-15'

pngData = b""
# 以二进制的形式读出图片
with open("./test.png","rb") as f:
    pngData = f.read()

# 以二进制的形式写进图片
with open("./testCopy.png","wb") as f:
    f.write(pngData)
