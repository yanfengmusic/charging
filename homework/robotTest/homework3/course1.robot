*** Settings ***
#Library  courseaction
Library  SeleniumLibrary
Library  Collections
Resource  rc.robot
*** Test Cases ***

case1
    [Setup]  deleteAllCourse
    [Teardown]  deleteAllCourse
#登录
    loginWebsite
#添加课程
    addCourse   robot1   robot框架   1
#判断课程是否被添加
    checkCourse   robot1
#关闭浏览器
    close browser

case2
    [Setup]     deleteAllCourse
    [Teardown]  deleteAllCourse
#登录
    loginWebsite
#添加课程
    addCourse     自动化测试   自动化测试   1
#判断课程是否被添加
    checkCourse    自动化测试
#关闭浏览器
    close browser





