#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-03-14'

import MySQLdb
import requests

data = [
    {"action":"add_course", "data": '{"name":"课程01--xctext","desc":"01","display_idx":1}'},
    {"action":"add_course", "data": '{"name":"课程02","desc":"02","display_idx":1}'},
    {"action":"add_course", "data": '{"name":"课程03","desc":"03","display_idx":1}'},
    {"action":"add_course", "data": '{"name":"课程04","desc":"04","display_idx":1}'},
    {"action":"add_course", "data": '{"name":"课程05","desc":"05","display_idx":1}'},
    {"action":"add_course", "data": '{"name":"课程06","desc":"06","display_idx":1}'},
]
# 一行代码实现接口请求，一次性传100个数据

sli = [requests.post(url = "http://localhost:90/api/mgr/sq_mgr/",data=i) for i in data]

for res in sli:
    print(res.json)
