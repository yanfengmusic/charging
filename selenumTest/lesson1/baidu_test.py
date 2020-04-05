#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-02-08'
"""
1、基本用户场景测试
2、验收测试
3、无法绕过UI直接测试的核心模块
如果不是做兼容性测试的话，最好是用Chrome浏览器，Chrome浏览器的兼容性目前来看是最好的
"""



from selenium import webdriver
from time import sleep
import uuid

def get_uuid():
    return uuid.uuid4()


def search_test():

    # driver = webdriver.Chrome()  #chromdriver直接放在python的安装包中
    # driver = webdriver.Chrome(r"D:\Tools\Python\Python36\chromedriver.exe")#chromdriver没有放在python的安装包
    driver = webdriver.Firefox()
    driver.get("http://www.baidu.com")
    print(driver.get_window_size())
    driver.minimize_window()#最小化
    sleep(3)
    driver.maximize_window()
    sleep(3)
    driver.set_window_size(480,800)
    sleep(3)
    driver.get("http://www.baidu.com")
    sleep(3)
    """
    <a href="http://www.baidu.com" target="_Blank">百度</a>

    _Blank是新窗口
    _Self是自身
    _Parent是父窗口
    _Top是顶层窗口
    当然也可以是自己定义的一个frame 的名字
    比如
    <a href="http://www.baidu.com" target="frame1">百度</a>
    
    """
    # 控制浏览器前进
    driver.forward()
    # 控制浏览器后退
    driver.back()
    # 控制浏览器刷新
    driver.refresh()

    # 八大定位方法：
    # driver.find_element_by_css_selector("#kw").send_keys("小米\n")
    # driver.find_element_by_xpath('//*[@id="kw"]').send_keys("小米\n")
    # driver.find_element_by_id('kw').send_keys("小米\n")#在字符串中加\n默认是回车的操作
    ele = driver.find_element_by_name()
    driver.find_elements_by_tag_name()
    driver.find_element_by_class_name()
    driver.find_element_by_link_text()#针对P标签，不支持模糊查询
    driver.find_element_by_partial_link_text()#针对P标签，支持模糊查询

    # 获取元素列表：在八大基本定位方法中加s
    driver.find_elements_by_tag_name()

    ele_attribute = ele.get_attribute('name')#获取元素的属性，包括name,id,href等


    sleep(3)
    driver.quit() #关闭浏览器并退出driver,如果该方法是放在函数中的，就算是没有这个方法，当函数结束时，也会关闭浏览器
    # driver.close()#只是关闭标签，而不是关闭浏览器，并且不会退出driver进程

    # driver.find_element(by=By.ID,value="aaa")
if __name__ == '__main__':
    search_test()
    # print(get_uuid())

