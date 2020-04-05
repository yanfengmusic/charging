#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-02-19'

"""
登录华为官网 https://www.vmall.com/， 
点击 "华为官网" 链接
检查 "华为官网" 页面上是否 有如下主菜单
  手机
  笔记本
  平板
  智慧屏
  穿戴
  更多产品
  软件应用
  服务与支持
  零售店
并输出检查结果
最后再回到主窗口， 检查鼠标停留在 "笔记本&平板" 处的时候， 是否显示的菜单有"平板电脑  笔记本电脑 笔记本配件"
怎么模拟鼠标停留事件，请大家自行网上搜索，看看能不能自己解决问题。
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# 初始化
driver = webdriver.Chrome()
driver.get("https://www.vmall.com/")
driver.implicitly_wait(10)
driver.maximize_window()

# 点击 "华为官网" 链接
driver.find_element_by_link_text("华为官网").click()
cur_handle = driver.current_window_handle

def getMaiMenus():
    """
    悬停主菜单
    :return:
    """
    expec_str ="华为Matebook X系列|华为Matebook系列|华为Matebook D系列|华为Matebook E系列|荣耀MagicBook系列|荣耀MagicBook Pro系列"
    ele = driver.find_element_by_id("zxnav_1")
    ActionChains(driver).move_to_element(ele).perform()
    Menus = driver.find_elements_by_css_selector("#zxnav_1>.category-panels>.subcate-list>li>a>p>span")
    Menus_text = [one.text for one in Menus]
    acture_text = "|".join(Menus_text)
    if expec_str == acture_text:
        print('页面显示正确')
    else:
        print('页面显示错误')


def check():
    """
    验证是否存在指定的菜单
    :return:
    """
    expect_str = '手机|笔记本|平板|智慧屏|穿戴|更多产品|软件应用|服务支持|零售店'
    sleep(5)
    Menus = driver.find_elements_by_css_selector(".left-box .nav-cnt > li")
    Menus_text = [one.text for one in Menus]
    acture_str = "|".join(Menus_text)
    # print(acture_str)
    if expect_str == acture_str:
        # print(acture_str)
        print('页面显示正确')
    else:
        print('页面显示错误')


# 根军handel切换到指定的页面
for handle in driver.window_handles:
    if handle != cur_handle:
        driver.switch_to.window(handle)
        check()
    else:
        driver.switch_to.window(handle)
        getMaiMenus()






