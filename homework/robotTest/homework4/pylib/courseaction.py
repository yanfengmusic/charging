#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-04-01'
from selenium import webdriver
from time import sleep
"""
陈旧的元素引用:元素没有附加到页面文档
查找元素是引用过期，页面刷新后，之前查找到的元素被更新了，导致元素不能正常使用
selenium.common.exceptions.StaleElementReferenceException: Message: stale element reference: element is not attached to the page document
  (Session info: chrome=80.0.3987.122)

"""

def deleteAllCourse():
    driver = webdriver.Chrome()
    driver.get("http://localhost:90/mgr/login/login.html")
    driver.implicitly_wait(10)
    # driver.find_element_by_id("username").click()
    # driver.find_element_by_id("password").click()
    driver.find_element_by_class_name("btn.btn-success").click()
    driver.implicitly_wait(2)
    while True:
        delete_buttons = driver.find_elements_by_xpath("//tbody/tr/td[4]/button[2]")
    # while True:
        print(len(delete_buttons))
        if delete_buttons == []:
            print("删除完毕")
            break
            sleep(2)
        delete_buttons[0].click()
        sleep(2)
        driver.find_element_by_class_name("btn.btn-primary").click()
        sleep(2)

    driver.quit()

if __name__ == '__main__':
    deleteAllCourse()
