#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-04-01'
from selenium import webdriver
from time import sleep

def deleteAllCourse():
    driver = webdriver.Chrome()
    driver.get("http://localhost:90/mgr/login/login.html")
    driver.implicitly_wait(10)
    # driver.find_element_by_id("username").click()
    # driver.find_element_by_id("password").click()
    driver.find_element_by_class_name("btn.btn-success").click()

    while True:
        delete_buttons = driver.find_elements_by_xpath("//tbody/tr/td[4]/button[2]")
        print(len(delete_buttons))
        if delete_buttons == []:
            print("删除完毕")
            break
            sleep(2)
        delete_buttons[0].click()
        sleep(2)
        driver.find_element_by_class_name("btn.btn-primary").click()
        sleep(2)
deleteAllCourse()
