#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-06-05'

from selenium import webdriver
from time import sleep

def deleteAllLesson():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("http://localhost:90/mgr/login/login.html")
    driver.find_element_by_id("username")
    driver.find_element_by_id("password")
    driver.find_element_by_class_name("btn-success").click()
    while True:
        delete_buttons = driver.find_elements_by_css_selector('[ng-click="delOne(one)"]')
        if delete_buttons:
            delete_buttons[0].click()
            sleep(2)
            driver.find_element_by_css_selector(".btn-primary").click()
            sleep(1)
        else:
            print("浏览器关闭")
            break
    driver.quit()

if __name__ == '__main__':
    deleteAllLesson()
