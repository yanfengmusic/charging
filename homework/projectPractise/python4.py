#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-07-02'

"""
4、下面的函数目的是把参数字符串倒序返回，请补全代码，完成功能
下面的程序用来将字符串倒序，
请补全代码
"""
def reverseStr(source):
    # 将字符串中的每个字符放入列表中
    tmp = [c for c in source]
    # 列表倒序
    tmp.reverse()

    return tmp

print (reverseStr('hello'))

