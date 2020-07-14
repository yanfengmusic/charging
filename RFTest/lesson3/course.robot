*** Settings ***
Library  SeleniumLibrary
Library  course
Suite Setup  deleteAllLesson
#Suite Teardown  deleteAllLesson
Resource  resource.robot

*** Test Cases ***
添加课程
    set selenium implicit wait  5
#登录
    loginwebsite
#添加
    addcource      robot   robot学习   1
#检查添加课程
    checkcource     robot
    close browser




