#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-02-25'

from appium import webdriver
from time import sleep

"""
自动化BOSS
尝试自动化方式完成以下操作
1.进入我的标签
2.点击右上角设置图标
3.进入账号与绑定
4.进入设置密码
5.完成密码设置    
#利用该方法获取页面的XML信息，自行进行元素定位
driver.page_source
"""

#准备自动化配置信息
desired_caps={
    'platformName':'Android',
    'plathformVersion':'8',
    'deviceName':'192.168.232.222:5555',
    'appPackage':"com.hpbr.bosszhipin",#'com.android.settings',#'com.ibox.calculators',
    'appActivity':"com.hpbr.bosszhipin.module.launcher.WelcomeActivity",#'.Settings',
    'noReset':True,
    'newCommandTimeout':6000
}

#初始化driver对象-用于控制手机
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素

# 1.进入我的标签(使用xpath)
driver.find_element_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/tv_tab_4']").click()
# 2.点击右上角设置图标
driver.find_element_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/iv_general_settings']").click()
# 3.进入账号与绑定
driver.find_element_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/rv_list']/android.widget.LinearLayout[1]").click()
# 4.点击设置密码
sleep(3)
driver.find_element_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/rv_list']/android.widget.LinearLayout[2]").click()
# eles = driver.find_elements_by_xpath("//*[@resource-id='com.hpbr.bosszhipin:id/tv_desc']")   #？？？？Message: Cached elements 'By.xpath: //*[@resource-id='com.hpbr.bosszhipin:id/tv_desc']' do not exist in DOM anymore

# try:
#     for ele in eles:
#         if ele.text == '去设置':
#             ele.click()
# except Exception as info:
#     print(info)
# finally:
    # page_xml = driver.page_source
    # print(page_xml)
    # 请设置密码
driver.find_element_by_xpath('//*[@resource-id="com.hpbr.bosszhipin:id/et_set_password"]').send_keys("123")
    # 再次输入密码
driver.find_element_by_xpath('//*[@resource-id="com.hpbr.bosszhipin:id/et_confirm_password"]').send_keys("hhhjhjh")
    # 点击确定
driver.find_element_by_xpath('//*[@resource-id="com.hpbr.bosszhipin:id/btn_confirm"]').click()
sleep(3)
driver.quit()
