#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-04-10'

from selenium  import webdriver

driver = webdriver.Chrome()

url = "http://localhost/mgr/login/login.html"
data = ['a','b',306]
user1={"username":"auto","pw":"sdfsdfsdf"}

