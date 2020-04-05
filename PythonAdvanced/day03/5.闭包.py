#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-16'

# 一个内部函数，引用了一个外部函数的变量，而不是全局变量，那么这个内部函数就属于一个闭包

def outer(func):

    x = 10 #局部函数

    # 内部函数
    def inner():
        print(x)   #一个内部函数，引用了一个外部函数的变量，而不是全局变量，那么这个内部函数就属于一个闭包
    return inner

c = outer()
c()
