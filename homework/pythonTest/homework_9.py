#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-02-01'

class Tiger():
    def __init__(self,name ='tiger',weight=200):
        self.weight = weight
        self.name = name
    def eat(self,food):
        if food == 'meat':
            self.weight += 10
            print("恭喜，喂食正确，体重增加10斤")
        else:
            self.weight -= 10
            print("抱歉，喂食错误，体重减少10斤")

    def roar(self):
        print('我是老虎---wow,体重减了5斤')
        self.weight -= 5

class Yang():
    def __init__(self,name='yang',weight=200):
        self.weight = weight
        self.name = name


    def eat(self,food):
        if food == 'grass':
            self.weight += 10
            print("恭喜，喂食正确，体重增加10斤")
        else:
            self.weight -= 10
            print("抱歉，喂食错误，体重减少10斤")

    def roar(self):
        print('我是羊---mie,体重减了5斤')
        self.weight -= 5

class Room():
    def __init__(self,num,annimal):
        self.num = num
        self.ani = annimal
    def __str__(self):
        return ('%s%s' %(self.num,self.ani))


# T = Tiger(200)
# r1 = Room(1,T)
# r1.ani.eat('meat')

from random import randint
room_list = []
for one in range(1,11):
    if randint(0,1) == 1:
        ani = Tiger()
    else:
        ani = Yang()
    room = Room(one,ani)
    # print(room)
    room_list.append(room)

import time
start_time = time.time()
while True:
    cur_time = time.time() #返回值是秒
    if cur_time - start_time >= 10:
        print('\n\n **********  游戏结束 ********** \n\n')
        for one in room_list:
            print(f'当前房间的编号是:{one.num}，动物是:{one.ani.name}，体重还有:{one.ani.weight}')
        break

    room_num = randint(1,10)
    room_object = room_list[room_num-1]
    # room_ani = None
    # for one in room_list:
    #     if one.num == room_num:
    #         room_ani = one.ani

    info = input("请问%d号房间，您是选择喂食还是敲门，如果选择喂食，请输入1，如果选择敲门，请输入2" %room_num)
    if info == '1':
        food = input("请选择需要喂的食物是'meat' or 'grass'")
        room_object.ani.eat(food)

    elif info == '2' :
        room_object.ani.roar()









