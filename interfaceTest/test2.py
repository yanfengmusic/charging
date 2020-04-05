#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-03-02'
import requests

r = requests.get("http://localhost:90/api/mgr/sq_mgr/?action=list_course&pagenum=1&pagesize=20")

repoad = {'action':'list_course','pagenum':1,'pagesize':20}
r = requests.get("http://localhost:90/api/mgr/sq_mgr/",params=repoad)
print(r.text)
