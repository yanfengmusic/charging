#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-16'

# 函数名可以赋值给其他变量
# 函数名可以当做参数传递
# 函数名可以作为返回值

"""
# 函数名可以赋值给其他变量

a = 99
print(a)

def foo():
    print("轻轻的我来了")

a = foo #函数名可以赋值给其他变量
print(a)
a()
"""

# 函数名可以当做参数传递
def foo(func):
    func()

def bar():
    print("函数名可以当做参数传递")

foo(bar)





"""
# 函数名可以作为返回值

def foo():
    def bar():
        print("函数名可以作为返回值")
    return bar
re = foo()
print(re())

"""
