#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

__mtime__ = '2020-02-29'

from appium import webdriver
import time
import traceback
"""
代码操作 手机端运行APP 需要电脑端下载与手机系统的webview版本匹配的驱动 目前发现不下载指定的确定也可以呢？？？？？
"""
desired_caps = {
    # 'automationName': 'UiAutomator2',
    'platformName': 'Android',
    'platformVersion': '8',
    'deviceName': '192.168.232.222:5555',
    'appPackage': 'com.example.jcy.wvtest',
    'appActivity': '.MainActivity',
    # 'chromedriverExecutableDir': r'D:\Tools\webdrivers\chromedriver_Pro2_mobile_71357880',
    'noReset': True,
    'newCommandTimeout': 6000
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动Remote RPC
driver.implicitly_wait(10)

# 操作原始应用里的webview
try:
    # -----------------------
    # 查看手机当前的context
    print(driver.contexts)

    print(driver.current_context)
    # 如果处于NATIVE_APP,就切换到webview里面
    if driver.current_context == 'NATIVE_APP':
        driver.switch_to.context('WEBVIEW_com.example.jcy.wvtest')
        print(driver.current_context)

    # 此时可以操作web元素了
    driver.find_element_by_id('index-kw').send_keys('松勤\n')
    # driver.find_element_by_id('index-bn').click()
    sleep(3)
    res = driver.find_element_by_css_selector('#results>div:nth-child(1) header')

    print(res.text)

    print(driver.current_context)
    # 切回原生模式
    driver.switch_to.context('NATIVE_APP')
    print(driver.current_context)
    # 操作元素界面控件
    driver.find_element_by_accessibility_id('面板').click()
    time.sleep(3)
    driver.find_element_by_accessibility_id('通知').click()

    # -----------------------

except:
    print(traceback.format_exc())

input('**** Press to quit..')
driver.quit()
