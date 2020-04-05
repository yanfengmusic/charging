#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-05'
"""
1、缩进：往后：tab 往前；shift+tab
2、函数的参数：形参、实参
3、方法的调用标准
4、string方法介绍
"""
# def getSum(a,b):#形参,必填的
#     return (a+b)
#
# res = getSum(a=10,b=20)
# print(res)

"""
string方法
"""
# 1.计数count(),返回值，有就是具体的个数，没有就是0
# str1 = 'abcadefag'
# print(str1.count('a'))
# 2.startswith() endswith(),返回值True,False
# print(str1.startswith("a"))
# print(str1.endswith("x"))
# 3.find() 返回指定的字符在字符串所在的位置,元素不存在返回-1
# print(str1.find("a"))
# print(str1.find("bc"))
# print(str1.find("x"))
# index()返回下标，前提是元素一定是存在的,不存在就会报错
# print(str1.index("x"))
# 4、rfind()在指定范围下查找
# print(str1.rfind('a',1))
# 5、isdigit(),检查是否是存数字
# 6、join()自定义拼接
print("***".join(['name','is','tom']))
# 7、split()分割,返回值是列表，切点会被切掉
# print(str1.split('a'))
# 8、lower(),upper()
# 9、replace()替换,默认是全部替换，可以指定个数
# print(str1.replace("a","x",1))
#10、 strip()默认替换所有的空格
# str1 = " a  abc de "
# print(str1.replace(" ",""))

# def my_find(inStr,unit):
#     if unit in inStr:
#         return inStr.index(unit)
#     else:
#         return -1
# print(my_find(str1,'b'))


"""
1.作用域：有一些微型处理器，内存很小，如果全部都是全局变量，会导致内存泄露
    1.局部变量：运行完后，会自动删除。我们在日常编码时，如果没有特殊要求，会优先定义局部变量
    2.全局变量：可以使用global x  将一个局部变量改为全局变量
2.参数:缺省参数
3.定义函数时，必填在前，缺省在最后
4.可变数量参数：*args，会封装成元祖 用途：print(1,2,3,4,5,6,7,8,9,10)
5、三者顺序：必填，可变数量参数，缺省
6.关键字可变参数 **kargs,是一个字典的形式,键最好是用字符串keywords must be strings
"""
# x = 10
# def func():
#     global x  #声明为全局变量
#     x = 9
#     print("this x is in func :",x)
# func()
# print("this x is out func:",x)
#
# def getSum(start,end=100):
#     print(start+end)
#
#
# getSum(50)
# getSum(50,end=200)
#
#
# print('hello',end='****')
# print("world")
# print(1,2,3,4,5,sep='￥￥')#sep分割属性，默认是以空格分割
# def print(self, *args, sep=' ', end='\n', file=None)  *args代表参数数量没有限制

# def func(a,*b,c=10):
#     print(a,b,c)
# func(1,2,3,c=20) #1 (2, 3) 20

# def getSum1(*numbers):
#     total = 0
#     print(numbers)
#     for n in numbers:
#         total = total+n
#     return  total
# alist = [1,2,3]
# print(getSum1(alist)) #([1, 2, 3],)直接传列表，会将参数封装成元祖，元祖里面包着列表
# print(getSum1(alist[0],alist[1],alist[2]))
# print(getSum1(*alist)) #可变参数调用的时候，可以用'*'标识符来代表展开元祖或列表


def func(a,c=2,*b,**kwargs):
    print(a,b,c,kwargs)

func(1,3,5,7,9,11,name='tom',age=20) #**kwargs 需要以字典的形式传入

dict1 = {'name':'lili'}
func(1,3,5,7,9,dict1)#与上面情况一样，不展开，就会以元祖的形式给包裹起来
func(1,3,5,7,9,**dict1)

"""
综合使用
"""
def func(a,b,c=0,*args,**kwargs):
    print(a,b,c,args,kwargs)
func(1,2)
func(1,2,c=3)
# func(1,2,c=3,5)报错
func(1,2,c=3,r=5)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x=99)


"""
文档说明
"""
def getAll():
    """
    测试文档说明
    :return:
    """
    return 'ok'
print(getAll.__doc__)
print(help(getAll))



