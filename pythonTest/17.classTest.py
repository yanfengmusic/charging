#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-16'

"""
游戏分解
1、找出设计的对象
    老虎：特征：属性，本质是:变量
          属性：
          静态属性：属于整个类的
          动态属性    
          行为：方法，本质是：函数
          静态方法：这个方法具体跟实例有关：这个方法有没有涉及到实例属性
          实例方法：整个类所有的实例都有这个方法。都是一样的
             
        
    羊
    房屋
2、关系组
3、验证
"""

# class Tiger:
#     className = '老虎'  #静态属性 属于整个类 每一个个体都一样
#     def __init__(self,weight):#构造方法/初始化方法 可以理解为java的构造器 只要创建实例就会被调用
#         self.weight = weight
#         print(self,"----我执行了-----")  #self谁创建就是谁


# 静态属性，既可以用类调用，也可以用对象调用
# print(Tiger.className)
# print(t1.className)

# 静态属性可以修改，可以用类.属性进行修改
# Tiger.className = '老虎1'
# print(Tiger.className)

# 实例属性 只有由对象来调用
# print(t1.height)

# t1 = Tiger(100)
# print(t1.weight)
# t2 = Tiger(200)
# print(t2.weight)


class Tiger:
    className = '老虎'
    def __init__(self,weight=200):#构造方法/初始化方法 可以理解为java的构造器 只要创建实例就会被调用
        self.weight = weight
        print(self,"----我执行了-----")  #self谁创建就是谁
    def roar(self):
        print('我是老虎---wow,体重减了5斤')
        self.weight -= 5
    def eat(self,food):
        if food == 'meat':
            self.weight += 10
            print("恭喜，喂食正确，体重增加10斤")
        else:
            self.weight -= 10
            print("抱歉，喂食错误，体重减少10斤")

#   静态方法:所有的实例都有一样的行为
    @staticmethod
    def static_roar():
        print("静态方法")
        return 1



t1 = Tiger(200)
# print(f'操作前的体重：{t1.weight}')
# t1.roar()
# print(f'操作后的体重：{t1.weight}')
# t1.eat('a')
# print(f'操作后的体重：{t1.weight}')
#
# print(Tiger.static_roar())
# print(t1.static_roar())


# 对象的组合
class Room:
    def __init__(self,num,inAnimal):
        self.num = num
        self.animal = inAnimal
r1 = Room(2,t1)
# 这个房间的老虎叫一声
r1.animal.roar()

class yang:
    pass
# 游戏初始化
# 游戏开始前
import random
roomList = []
from random import randint
print(randint(0,2))#双闭区间0,1,2
for one in range(1,11):
    if randint(0,1) == 1:
        ani = Tiger()
    else:
        ani = ''

    room = Room(one,'xx')
    roomList.append(room)
print(roomList)

import time
print(time.time())
start = time.time()
while True:
    curTime = time.time()
    if curTime-start >= 20:
        break


# 继续
# java是单继承 多实现
# python多继承 1个儿子 一群父亲
# 如果子类没有__init__方法，会自动调用父类的
# 如果子类自己有__init__方法，则不会自动调用父类，就意味着不会继承，需要自己调用一下
# 父类的实例属性不够用的时候，才需要自己init方法来扩充
# 子类有自己的init方法，会优先使用自己的init方法
class SouthTiger(Tiger): #多继承加“，”
    def __init__(self,inname):
        Tiger.__init__(self,weight = 200)
        self.name = inname
s1 = SouthTiger("a")
print(s1.name)

# 方法的重写：多态的一种体现，一个方法在父类和子类有不同的操作
#    父类是有一个方法，子类去继承时，发现不能够满足子类，所以需要重写该方法


