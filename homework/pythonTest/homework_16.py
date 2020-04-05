#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-02-20'

"""
-- 作业2
写一个程序实现如下的自动化过程
- 登录   https://tinypng.com/ 
- 点击 上传文件的虚线框
- 选择 插图，在本地目录中选择一张准备好的图片 , 查看是否能够上传图片成功
"""

from selenium import webdriver
from time import sleep
import win32com.client  #操作windows的一些键盘事件

driver = webdriver.Chrome()
driver.get("https://tinypng.com/")
driver.implicitly_wait(10)
ele = driver.find_element_by_class_name("target")
ele.click()
sleep(5)
# 使用win32com.client包来上传附件
# 需要默认输入法设置成英文
shell = win32com.client.Dispatch("WScript.shell")
shell.Sendkeys(r"E:\pconline1497363391557\001.jpg"+'\n\n')
