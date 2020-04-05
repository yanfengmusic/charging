#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-03-29'

import requests

"""
RobotFramework 作业 2
创建一个测试套件文件，实现 2个测试用例：
用例1：
    1.  用Python语言开发一个测试库 course_mgr.py。
        该库有一个函数 listCourse 可以返回教管系统的所有课程（可以使用requests库开发）。
    2.  用RF测试用例来使用 listCourse 关键字， 根据其返回的课程列表，
        将所有的课程名输出到日志文件中（使用循环）
        验证是否和预期课程相同
"""
def login():
    dict_head = {"Content-Type":"application/x-www-form-urlencoded"}
    payload = {"username":"auto","password":"sdfsdfsdf"}
    re = requests.post("http://localhost:90/api/mgr/loginReq",data=payload,headers = dict_head,)
    # print(re.cookies)
    return re.cookies["sessionid"]

cookie = {
    "sessionid":login()
}


def listCourse():
    re = requests.get("http://localhost:90/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20",cookies = cookie )
    return re.json()

if __name__ == '__main__':
    # login()
    a = listCourse()
    print(a)
