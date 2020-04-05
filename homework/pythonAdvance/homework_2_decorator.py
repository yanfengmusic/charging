#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

import uuid

__mtime__ = '2020-03-17'

user_dict = {
    "user1":"123",
    "user2":"123"
}
token = ""
print(token)

def decorator(func):
    def inner(*args,**kwargs):
        global token
        if token:
            func(*args,**kwargs)
        else:
            name = input("请输入用户名:").strip()
            password = input("请输入密码:").strip()
            if name==user_dict["user1"] and password == user_dict["user2"]:
                func(*args, **kwargs)
                token = uuid.uuid4()
            else:
                print("输入的用户不存在")
    return inner

@decorator
def my_log():
    print("this is my log")

@decorator
def my_name(name):
    print(name)

def my_shoping_mall():
    print("商城购物")

while True:
    choose_num = input("\n1、查看日志\n2、我的信息\n3、我的商城\n4、请输入操作选项（输入q退出）")
    if choose_num == 'q'or choose_num == 'Q':
        break
    elif choose_num == "1":
        my_log()
    elif choose_num == '2':
        my_name("张三")
    elif choose_num == '3':
        my_shoping_mall()
    else:
        print("输入不合法")
