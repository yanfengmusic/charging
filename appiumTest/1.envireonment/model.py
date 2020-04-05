#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
#如果被测应用没有安装到手机上,可以指定apk的在电脑上路径
    # 'app':r'D:\apk\xxx.apk',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000
}

#初始化driver对象-用于控制手机
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素

#点击放大镜
eles=driver.find_elements_by_id('com.hpbr.bosszhipin:id/img_icon')#先取所有符合条件的元素
#找到第二个元素--放大镜
btn=eles[1]
btn.click()

#搜索框输入职位信息
search_input=driver.find_element_by_id('com.hpbr.bosszhipin:id/et_search')
search_input.send_keys('软件测试')#输入参数

#选择符合条件的第一个搜索结果
driver.find_element_by_id('com.hpbr.bosszhipin:id/tv_filtered_name').click()


#获取当前页面所有职位信息元素
job_msg=driver.find_elements_by_id('com.hpbr.bosszhipin:id/view_job_card')

for job in job_msg:
    #输出岗位名称
    name=job.find_element_by_id('com.hpbr.bosszhipin:id/tv_position_name')
    # print(name.text)
    #输出薪资
    salray=job.find_element_by_id('com.hpbr.bosszhipin:id/tv_salary_statue')
    # print(salray.text)
    #输出公司名称
    company=job.find_element_by_id('com.hpbr.bosszhipin:id/tv_company_name')

    print('%s|%s|%s'%(name.text,salray.text,company.text))



# input('......')


driver.quit()

# Lagou自动化脚本
#导包
from appium import webdriver

#准备自动化配置信息
desired_caps={
    #移动设备平台
    'platformName':'Android',
    #平台OS版本号
    'plathformVersion':'10',
    #设备的名称--值可以随便写
    'deviceName':'test0106',
    #提供被测app的信息-包名，入口信息
    'appPackage':'com.alpha.lagouapk',
    'appActivity':'.HelloActivity',
    #确保自动化之后不重置app
    'noReset':True,
    #设置session的超时时间，单位秒
    'newCommandTimeout':6000,

}

#初始化driver对象-用于控制手机
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)#稳定元素

#点击弹出搜索框
search_bar=driver.find_element_by_id('com.alpha.lagouapk:id/search_tab_txt')
search_bar.click()

#搜索框输入职位信息
search_input=driver.find_element_by_id('com.alpha.lagouapk:id/result_Search')
search_input.send_keys('软件测试')#输入参数

#待选结果-选择第一个
seres=driver.find_elements_by_id('com.alpha.lagouapk:id/tv_suggest_key')
seres[0].click()

#搜索查询结果-岗位名，待遇，公司
jobs=driver.find_elements_by_id('com.alpha.lagouapk:id/position_card_content_layout')
#通过公司信息元素找到详细信息
for job in jobs:
    name=job.find_element_by_id('com.alpha.lagouapk:id/position_name').text
    salary=job.find_element_by_id('com.alpha.lagouapk:id/position_card_salary').text
    company=job.find_element_by_id('com.alpha.lagouapk:id/position_card_company_name').text

    print(f'公司：{company}|职位：{name}|待遇：{salary}')



# input('......')


driver.quit()

