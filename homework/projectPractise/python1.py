#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-07-02'


"""
1、请写代码， 用if语句判断字符串变量var的长度是否大于10，并且其中是否包含'ok'，如果两个条件都满足，就打印ok
"""

def isLong(s):
    if len(s) > 10 and 'ok' in s:
        print("ok")


s = 'abcdefgoklll'
isLong(s)
