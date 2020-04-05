#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-02-10'
# 获取当前窗口的titile

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
print(driver.title)
print(driver.current_url)
print(driver.get_screenshot_as_file("./all.png")) #截取整个页面
ele = driver.find_element_by_css_selector("#kw")
ele.screenshot("./ele.png")

cur_handel = driver.current_window_handle() #获取当前标签页句柄
handls = driver.window_handles()
for one in handls:
    if cur_handel != one:
        driver.switch_to.window(one)
