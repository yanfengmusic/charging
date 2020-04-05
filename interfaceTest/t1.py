#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-19'

"""
信息一、
我的名字叫呱呱，年龄35岁,不抽烟
A. 用urlencoded格式表述为,form表单表达方式
B. 用JSON格式表述为

name=呱呱&age=35
{
"name":"呱呱"
"age":35
}

"""
# import requests
# # proxies = {
# #   "https": "http://10.10.26.28:8888",
# # }
# r = requests.get("https://www.baidu.com",verify=False)
# print(r.text)

"""
信息二、
我的名字叫呱呱，年龄35岁，不抽烟，我有三本书（语文、数学、英语），我的领导是小猪老师，他年龄35岁。我有2个孩子，分别是：呱小呱，3岁，呱唧呱 ，5岁。
"""

{
"name":"呱呱",
    "age":35,
    "smoke":false,
    "books":["语文","数学","英语"],
    "leader":{
        "age": 35,
        "sons":[{"name":"呱小呱","age":3},{"name":"呱唧呱","age":5}]
    }
}
