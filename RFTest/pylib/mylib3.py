#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp
import  time
from time import sleep
from selenium import webdriver

__mtime__ = '2020-06-02'

def get_time1():
    return  time.time()


def get_baidu(url):
    driver = webdriver.Chrome()
    driver.get(url)
    sleep(5)
    driver.quit()
    return True

def get_hello():
    return 'hello'

if __name__ == '__main__':
    time = get_time1()
    print(time)
    get_baidu("http://www.baidu.com")
