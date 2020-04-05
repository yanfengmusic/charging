#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp
import time

__mtime__ = '2020-03-16'

"""
def foo():
    print("执行了一些测试用例")
    time.sleep(1)

def showtime(func):
    def inner():
        begin_time = time.time()
        func()
        endtime = time.time()
        print("总运行时间：",endtime-begin_time)
    return inner

foo = showtime(foo)
foo()
"""

def showtime(func):  #装饰函数，也就是装饰器
    def inner():
        begin_time = time.time()
        func()
        endtime = time.time()
        print("总运行时间：",endtime-begin_time)
    return inner

@showtime
def foo(): #被装饰函数
    print("执行了一些测试用例")
    time.sleep(1)

foo()
