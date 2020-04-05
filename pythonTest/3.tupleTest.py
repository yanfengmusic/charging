#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2019-12-30'

# 元祖也是sequence类型 不能改变元素值和个数，不能是一个元素，如果是一个，就变成int类型了
# 一般用途：查询，只读，一般像系统配置参数
tup1 = (10,20)
print(type(tup1))

print(id(tup1))
tup1 = (30,40) # 这个是重新赋值
print(tup1)
print(id(tup1))
# 列表与元祖的转换 是另存为一个新的对象
print(list(tup1))
print(id(list(tup1)))




