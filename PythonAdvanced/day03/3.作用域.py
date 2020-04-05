#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-16'
"""
全局作用域，局部作用域，嵌套作用域,内置(built_in)作用域：系统内固定模块内的变量，比如说：__name__,os,d
都是就近原则，现在自己的层找，然后一层一层的往外找
"""

b = 99 #全局变量

def foo():

    a = 100  #局部变量
    b = 200
    print(a)
    print(b)
#   print(c) #引用嵌套作用域的就不可以了

    def bar(): #嵌套作用域
        c = 299
        print(a,b,c) #引用全局和局部变量都可以

foo()
# print(a)  #找不到a

x = 10
def test():
    global x  #生命其成为一个全局变量
    x = 20
    print(x)
test()
print(x)
