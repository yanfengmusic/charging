#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-03-15'

# a = "abc"
# b = b'执子之手与子偕老'  #默认会用ASCCII码来解析
# print(type(a),type(b))

text = "落红不是无情物，化作春泥更护花"
Byte_text = text.encode("utf8")  #encode 将字符串转化为byte类型
print(type(text))
print(type(Byte_text))
print(Byte_text)

c = b'\xe8\x90\xbd\xe7\xba\xa2\xe4\xb8\x8d\xe6\x98\xaf\xe6\x97\xa0\xe6\x83\x85\xe7\x89\xa9\xef\xbc\x8c\xe5\x8c\x96\xe4\xbd\x9c\xe6\x98\xa5\xe6\xb3\xa5\xe6\x9b\xb4\xe6\x8a\xa4\xe8\x8a\xb1'
print(c.decode("utf8"))#decode 将byte类型转换为字符串转
