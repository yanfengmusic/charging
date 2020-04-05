#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-03-03'

import requests
import pprint

url = "http://localhost:90"
# 【案例1】：百度首页
# r = requests.get("http://www.baidu.com")
# 1.HTTPS请求进行SSL验证或忽略SSL验证才能请求成功，忽略方式为verify = False。
# 2.SSL证书是由CA机构颁发的，所以安全也是要钱的
# 3.要完全理解HTTP协议，不能只到分辨HTTP的GET，POST等动作的程度，还要去理解7层
r = requests.get("https://www.baidu.com",verify=False)
r.encoding = "utf-8"
print(r.text)
# print(type(r))
# r.encoding="utf-8"
# pprint.pprint(r.text)


# 【案例2】：教管系统-列出课程
payload = {
    "action": "list_course",
    "pagenum": 1,
    "pagesize": 20
}
r = requests.get("http://localhost:90/api/mgr/sq_mgr/",params=payload)
pprint.pprint(r.json())

# 【案例3】：教管系统-新增课程
# dict1 = {"Content-Type":"application/x-www-form-urlencoded"}
# payload = {
#     "action":"add_course",
#     "data":"""{
#     "name":"初中化学1",
#     "desc":"初中化学课程",
#     "display_idx":4
#     }"""
# }
# r = requests.post("http://localhost:90/api/mgr/sq_mgr/",data=payload,headers = dict1)
# print(r.url)
# print(r.json())

# 【案例4】：教管系统-新增课程2
# dict1 = {"Content-Type":"application/json"}
# payload = """{
#   "action" : "add_course_json",
#   "data": {
#     "name":"初中化学",
#     "desc":"初中化学课程",
#     "display_idx":"4"
#   }
# }"""
# r = requests.post(url+"/apijson/mgr/sq_mgr/",headers = dict1,data=payload.encode(encoding='UTF-8'))
# print(r.url)
# print(r.text)

# 【案例5】：用户登录
# dict1 = {"Content-Type":"application/x-www-form-urlencoded"}
# payload = {
#     "username":"auto",
#     "password":"sdfsdfsdf"
# }
# r = requests.post(url+"/api/mgr/loginReq",headers = dict1,data=payload)
# print(r.text)
# print(r.json())

# 【案例5】：用户登录cookie
dict1 = {"Content-Type":"application/x-www-form-urlencoded"}
payload={"username":"auto","password":"sdfsdfsdf"}
r = requests.post(url+"/api/mgr/loginReq",data=payload,headers = dict1)
# pprint.pprint(r.headers)
print(r.headers['Set-Cookie'])
print(r.cookies)
print(r.cookies["sessionid"])

