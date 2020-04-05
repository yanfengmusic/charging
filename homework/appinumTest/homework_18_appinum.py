#!/usr/bin/env python
# -*- coding: utf-8 -*-


__mtime__ = '2020-02-23'

"""
1 到手机应用市场下载或如下网址下载 多多计算器 
http://android.myapp.com/myapp/detail.htm?apkName=com.ibox.calculators&ADTAG=mobile
2 用 aapt.exe 命令查看 apk包的 appPackage 信息和 主 Activity 信息
3 用 UIAutomator Viewer 查看应用界面元素信息
4 编写python程序，完成一个 计算 3+9 ，结果 再乘以5 的自动化功能. 最后判断计算结果是否为60，如果是，测试通过；否则测试不通过
"""

from appium import webdriver
from time import sleep
#准备自动化配置信息
desired_caps={
    'platformName':'Android',
    'plathformVersion':'8',
    'deviceName':'MI6',
    'appPackage':'com.ibox.calculators',
    'appActivity':'com.ibox.calculators.SplashActivity',
    'noReset':True,
    'newCommandTimeout':6000
}

#初始化driver对象-用于控制手机
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素
# 定位到我的选项卡下，并点击进入到我的页面
# driver.install_app(r"D:\Download\BaiDuYun\松勤自动化\作业\com.ibox.calculators_3.1.5_1315.apk")
# driver.start_activity('com.ibox.calculators','com.ibox.calculators.SplashActivity')
# sleep(5)
# 获取第一个加数a,第二个加数b,第三个数9
num3 = driver.find_element_by_id("com.ibox.calculators:id/digit3").click()
puls = driver.find_element_by_id("com.ibox.calculators:id/plus").click()
num9 = driver.find_element_by_id("com.ibox.calculators:id/digit9").click()
equal = driver.find_element_by_id("com.ibox.calculators:id/equal").click()
mul = driver.find_element_by_id("com.ibox.calculators:id/mul").click()
num5 = driver.find_element_by_id("com.ibox.calculators:id/digit5").click()
equal = driver.find_element_by_id("com.ibox.calculators:id/equal").click()
re = driver.find_elements_by_class_name("android.widget.TextView")
# for one in re:
#     print(one.text)
if re[1].text == '60':
    print("测试通过")
else:
    print("测试不通过")

sleep(3)
driver.quit()
