#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-07-02'
"""
2、下面的列表里面包含了一些字符串元素
info = [
    '月亮ok',
    '太阳good',
    '月亮fine',
    '太阳ok',
]
请用for循环 写一段代码打印其中所有包含ok的字符串元素
"""

info = [
    '月亮ok',
    '太阳good',
    '月亮fine',
    '太阳ok',
]

for i in info:
    if 'ok' in i:
        print(i)

