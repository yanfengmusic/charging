#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType
from appium.webdriver.common.touch_action import TouchAction

__mtime__ = '2020-02-27'


#准备自动化配置信息
desired_caps={
    'platformName':'Android',
    'plathformVersion':'8',
    'deviceName':'192.168.232.222:5555',
    'appPackage':'com.miui.home',#'com.ibox.calculators',  com.android.settings/.MiuiSettings
    'appActivity':'.launcher.Launcher',
    'noReset':True,
    'newCommandTimeout':6000
}

#初始化driver对象-用于控制手机
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素
sleep(2)
# eles = driver.find_elements_by_xpath("//*[contains(@content-desc,'设置')]")
# eles[0].click() 这种方式 比较麻烦
# ele = driver.find_element_by_xpath("//*[contains(@text,'设置')]") 桌面的识别都得是图标，文字点了没反应

# 可以直接获取设置这个元素的全部的xpath
driver.find_element_by_xpath("//android.widget.RelativeLayout[@content-desc='设置']").click()
# TouchAction(driver).tap(eles[0]).perform()
# driver.tap([(148, 1633)])
# driver.find_element_by_xpath("//*[contains(@resource-id,'com.miui.home:id/icon_icon')]").click()
print(driver.device_time)
a  = driver.get_window_size()
print(a)
# for i in range(6):
#     # 调整声音
#     driver.keyevent(24)
# driver.close()
# 打开通知栏
driver.open_notifications()
sleep(3)
# 返回
driver.keyevent(4)
# 设置网络
driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
#获取网络
print(driver.network_connection)
driver.get_screenshot_as_file("./xxx.png")
