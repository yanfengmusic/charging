#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver

"""
直接使用电脑浏览器访问带有web端的APP
"""

#1打开电脑上的浏览器以手机模式运行
chrome_options = webdriver.ChromeOptions()

# 2选择一种存在的模拟手机设备类型
chrome_options.add_experimental_option(
    "mobileEmulation",
    {"deviceName": "iPhone X"})

print(chrome_options.to_capabilities())

# 3启动webdriver 添加配置项
driver = webdriver.Chrome(desired_capabilities = chrome_options.to_capabilities())

driver.implicitly_wait(10)
driver.get('http://www.baidu.com')
sleep(1)

#设置浏览器窗口尺寸
driver.set_window_size(411,731)

element_keyword = driver.find_element_by_id("index-kw")

# 输入字符
element_keyword.click()
element_keyword.send_keys('小米\n')


input('press to continue...')
driver.quit()
