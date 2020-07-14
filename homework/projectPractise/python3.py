#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-07-02'

"""
3、下面的列表里面包含了一些字符串元素
info = [
    '月亮ok',
    '太阳good',
    '月亮fine',
    '太阳ok',
]

请用while 循环 写一段代码打印其中所有包含ok的字符串元素
"""
info = [
    '月亮ok',
    '太阳good',
    '月亮fine',
    '太阳ok',
]

i = 0
while i<len(info):
    if 'ok' in info[i]:
        print(info[i])
    i += 1

