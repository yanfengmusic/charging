#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-31'

import base64

str1 = "sdfjhsdjkfhaskdjfh"
pwd = base64.b64encode(str1.encode("UTF-8"))
print("编码后的结果为：",pwd)

# 解码
print("解码后的结果为：",base64.b64decode(pwd))
bstr = base64.b64decode(pwd)
print(bstr.decode("utf-8"))



