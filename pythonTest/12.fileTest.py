#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-08'

"只针对txt文件"
# file_object = open("file_name",access_mode = 'r')
# file_name : 绝对路径和相对路径
# access_mode:打开的模式，包括：读，写，读+写

# 3种文件路径写法
# fileDir = "D:/test1.txt"
# fileDir2 = "D:\\pytest1.txt"
# fileDir3 = r'D:\ptest.txt' #只有在python中可以用r来取消转义

# 读操作如果文件不存在，会报No such file or directory错误
# 写操作时，文件不存在，则会自动生成一个文件
# fileDir = "E:\\pytest测试1.txt"
# fo = open(fileDir,encoding='utf-8') #encoding='utf-8'如果文件名有中文就加这个
# print(type(fo))
# print(fo.tell())
# print(fo.read(2))#读指定长度，返回的类型都是字符串
# print(fo.tell())
# print(fo.read(2))#从上面结束的地方再读两个
# print(fo.tell())
# print(fo.read())#从上面结束的地方读后面的全部

# 文件关闭
# fo.close() #关闭内存对象，就不能再操作了  ValueError: I/O operation on closed file.
# print(fo.read())

# 文件指针 也就是文件的光标，标记当前所在的位置，默认在0，可以使用tell（）方法获取
# 文件移动 seek（1,0）方法 两个参数，移动到的位置和模式：
# 0读模式，永远从文件指针开始的地方计算
# 1、2模式：必须是‘rb'模式，也就是以二进制形式读取模式,1，从当前位置开始移动，2是从尾部开始数

# 读一行,读多行，今晚的作业题
# fo.readline()
# fo.readlines() #返回list列表
# 读取所有行 -- 去换行符.splitlines() 默认以行为单元进行切割 就会把换行符去掉

# 2、文件写操作，--文件不存在会新建；文件存在会清空所有的内容
fileDir = "E:\\pytest测试1.txt"
fo = open(fileDir,'w',encoding='utf-8') #encoding='utf-8'如果文件名有中文就加这个
# 使用场景：输出本次使用的详细信息
str = """
        说你又不听，
        听又不懂，
        董又不做，
        做不又做错，
        错又不认，
        认又不改，
        改又不服，
        不服也不说，
        那让我怎么办？？？？
"""

fo.write(str)#这个操作最好是在python解释器中看，本身不写在磁盘，而是写在缓存中
# write模式在使用时，如果文件不存在，会自动创建文件，如果文件存在了内容，会清空之前的内容，从而覆盖
# 如果需要一个接着写的，可以去换其他的模式来操作
fo.flush()#或者关闭，才能看见

# 打开多个文件操作,可以省略close（）操作,读写操作写在下面的缩进俩面
# with open(fileDir) as fo,open("xxx",'w')as fo2:
#     fo.readlines()
#     fo2.readlines()
#     pass
