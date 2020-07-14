#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-07-02'
"""
7、浏览器进入网页云音乐  https://music.163.com/
在首页的发现音乐菜单，点击进入排行榜>云音乐新歌版
查看排名前三的歌曲下的评论，在精彩评论部分找到点赞数量最高的评论，获取评论作者，内容，时间和当前点赞数量
"""

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://music.163.com/")
driver.implicitly_wait(10)

def panhang_info(num):
    # 进入到排行榜
    driver.find_element_by_link_text("排行榜").click()
    sleep(1)
    driver.switch_to.frame(0)
    # 进入到云音乐新歌版
    driver.find_element_by_css_selector('#toplist > div.g-sd3.g-sd3-1 > div > ul:nth-child(2) > li:nth-child(2) > div > p.name > a').click()
    # 选择排名第一首的歌曲
    driver.find_element_by_xpath(f'//tbody/tr[{num}]/td[2]/div/div/div/span/a').click()
    text = driver.find_element_by_css_selector(".cmmts.j-flag>div:nth-child(2)  .cntwrap .cnt").text
    author = text.split("：")[0]
    text = text.split("：")[1]
    time = driver.find_element_by_css_selector(".cmmts.j-flag>div:nth-child(2)  .cntwrap .rp .time").text
    zen_num = driver.find_element_by_css_selector(".cmmts.j-flag>div:nth-child(2)  .cntwrap .rp>a[data-type='like']").text
    print(author,text,zen_num,time)
    driver.delete_all_cookies()
    driver.quit()

panhang_info(1)



