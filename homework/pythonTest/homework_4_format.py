#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-07'

"""
1.程序开始的时候提示用户输入学生年龄信息 格式如下：
Jack Green ,   21  ;  Mike Mos, 9;
我们假设 用户输入 上面的信息，必定会遵守下面的规则：
学生信息之间用分号隔开（分号前后可能有不定数量的空格），
每个学生信息里的 姓名和 年龄之间用 逗号隔开（逗号前后可能有不定数量的空格） 
2. 程序随后将输入的学生信息分行显示，格式如下
Jack Green :   21;
Mike Mos   :   09;
学生的姓名要求左对齐，宽度为20， 年龄信息右对齐，宽度为2位，不足前面补零
"""
"""
编程思路：
1、获取用户输入的信息
2、提取每一个学生的名字+年龄
3、按照格式进行排版输出

"""
while True:
    instr = input("请输入学生年龄信息 格式如下：Jack Green ,21  ;  Mike Mos,9;")
    info = instr.split(";")
    del info[-1]
    for one in info:
        # temp = one.split(",")
        # name = temp[0].strip()
        # age = int(temp[-1].strip())
        name,age = one.split(",")  #相当于a,b = [10,20]
        print(f'{name:<20}:{age:0>2}')
"""
优化方向：
1.提供代码的交互性(健壮性）---如果用户不按照要求的格式输入---提示用户，按照要求
  1- ，
  2- ；
"""



# while True:
#     info = input("请输入学生年龄信息 格式如下：Jack Green ,21  ;  Mike Mos,9;")
#
#     s = info.split(";")[0].strip().split(',')
#     print('{:<20}:{:0>2}'.format(s[0],s[1]))
#
#     s1 = info.split(";")[1].strip().split(',')
#     print('{:<20}:{:0>2}'.format(s1[0], s1[1]))




