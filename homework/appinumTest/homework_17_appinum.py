#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

__mtime__ = '2020-02-22'

# BOSS自动化脚本
#导包
from appium import webdriver

#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号
    'plathformVersion':'9',
    #设备的名称--值可以随便写
    'deviceName':'MI6',
    #提供被测app的信息-包名，入口信息
    'appPackage':'io.manong.developerdaily',
    'appActivity':'io.toutiao.android.ui.activity.LaunchActivity',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000
}
#初始化driver对象-用于控制手机
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素
# 定位到我的选项卡下，并点击进入到我的页面
time.sleep(3)
# driver.find_element_by_xpath("//*[contains('text','我的')]").click()
eles = driver.find_elements_by_class_name("android.widget.TextView")
print(len(eles))
for e in eles:
    if e.text == '我的':
        e.click()
# 点击头像右侧区域，对用户名进行修改
driver.find_element_by_id("user_name_layout").click()
time.sleep(2)
# 修改前截图
driver.get_screenshot_as_file("./修改前.png")
driver.find_element_by_id("subtitle_nickname").click()
time.sleep(1)
# 进行修改
driver.find_element_by_id("android:id/input").send_keys("凌晨1點\n")
time.sleep(1)
# 修改后点击确定按钮
driver.find_element_by_id("io.manong.developerdaily:id/md_buttonDefaultPositive").click()
time.sleep(1)
# 修改后截图
driver.get_screenshot_as_file("./修改后.png")
time.sleep(1)
driver.quit()

