#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-02-21'
from appium import webdriver

import time

# server 启动参数
desired_caps={
# 设备信息
"platformName": "Android",
"platformVersion": "9",
"deviceName": "dea53838", #可以随便写，但是必须得有，且值不能为空，或者指定某一个设备的ip,端口号一般默认为5555
# app信息
'appPackage': 'com.sina.weibo',
'appActivity': '.SplashActivity',
# "app": r'd:\apk\toutiao.apk', #如果APP没有安装在手机上，可以指定路径然后自动安装，并自动删除该安装包
#解决输入中文问题
# 'unicodeKeyboard': True,
# 'resetKeyboard' : True,
#其他配置
"noReset":True,#防止初始化app，
'newCommandTimeout': 6000,#单位是秒s
#"automationName": "UiAutomator2" #系统在第一次运行的时候会自动安装，并且会自动自动选择该服务
# 如果不想每次都安装UI2驱动，可以这么设置
# 指定自动化驱动
# 'automationName':'UiAutomator2',
# 'skipServerInstallation':True
# 使用指定的浏览器驱动-匹配手机上的谷歌浏览器
# 'chromedriverExecutableDir': r'D:\tools\webdrivers'
}

# 补充
"""
无线连接设备操作：
1.进入cmd
2.激活服务端口adb tcpip 5555
3.连接指定设备IP：adb connect 192.168.232.1 可以不输入端口号 端口号默认为5555 
"""


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
input('...')

driver.quit()


