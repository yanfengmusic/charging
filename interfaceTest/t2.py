#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-19'

import requests
import pprint

# 【案例1】：百度首页
# r = requests.get("https://www.baidu.com",verify = False)
# r.encoding = "utf-8"
# pprint.pprint(r.text)

# 【案例2】：教管系统-列出课程
# payload = {
#     "action":"list_course",
#     "pagenum":1,
#     "pagesize":20
# }
# r = requests.get("http://localhost:90/api/mgr/sq_mgr/",params=payload)
# print(r.url)
# pprint.pprint(r.json())

# 【案例3】：教管系统-新增课程
# dict_header = {
# "Content-Type":"application/x-www-form-urlencoded"
# }
#
# dict_data = {
# "action":"add_course",
# "data":""" {
#   "name":"初中化学12",
#   "desc":"初中化学课程",
#   "display_idx":"4"
#  }"""
# }
#
# r = requests.post("http://localhost:90/api/mgr/sq_mgr/",headers = dict_header, data = dict_data)
# print(r.json())


# 【案例4】：教管系统-新增课程2
# dict_header ={
# "Content-Type": "application/json"
# }
# payload = """{
#   "action" : "add_course_json",
#   "data": {
#     "name":"初中化学222",
#     "desc":"初中化学课程",
#     "display_idx":"4"
#   }
# }"""
# r = requests.post("http://localhost:90/apijson/mgr/sq_mgr/",data=payload.encode(encoding="utf-8"), headers=dict_header)
# print(r.json())

# 【案例5】：用户登录

dict_header = {
"Content-Type":"application/x-www-form-urlencoded"
}
payload = {
"username":"auto",
"password":"sdfsdfsdf"
}
r = requests.post("http://localhost:90/api/mgr/loginReq",data=payload,headers= dict_header)
print(r.json())
# pprint.pprint(r.headers)
# print(r.headers["Set-Cookie"].split(";")[0])
print(r.cookies["sessionid"])
"""
{'Content-Type': 'application/json', 'X-Frame-Options': 'SAMEORIGIN', 'Content-Length': '14', 'Vary': 'Cookie', 'Set-Cookie': 'sessionid=sqw8bufgwfcn6e47kc53psuetdzxdady; HttpOnly; Path=/', 'Date': 'Thu, 19 Mar 2020 10:20:11 GMT', 'Server': '0.0.0.0'}



"""


# 【案例6】：用户登录cookie


