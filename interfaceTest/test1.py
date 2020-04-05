#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-03-02'

import requests
import pprint

r = requests.get("http://www.baidu.com")
r.encoding = "utf8"
pprint.pprint(r.text)
# print(r.text)
# print(r.content)
