#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp
from selenium.webdriver.common import by

__mtime__ = '2020-03-29'

from selenium import webdriver
from time import sleep

"""
用例2：
    登录网站https://www.vmall.com/index.html
    获得所有热销单品的名称，打印在log报表中
"""

loc_scrollEle = ("css selector","#zxnav_9 > div.category-item-bg > div > a > span")
loc_goods = ("css selector",".span-968.fl ul li div")
list_data = []
def get_info():
    driver = webdriver.Chrome()
    driver.get("https://www.vmall.com/index.html")
    driver.maximize_window()

    # 滚动到指定的元素，从而查看到热销单品
    target = driver.find_element(*loc_scrollEle)
    driver.execute_script("arguments[0].scrollIntoView()", target)

    goods = driver.find_elements(*loc_goods)
    for i in goods:
        list_data.append(i.text)

    return list_data


if __name__ == '__main__':
    a = get_info()
    print(a)
