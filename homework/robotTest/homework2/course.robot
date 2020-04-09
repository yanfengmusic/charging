*** Settings ***
Library  courseaction
Library  SeleniumLibrary
*** Test Cases ***

case1
    [Setup]  deleteAllCourse
    open browser   http://localhost:90/mgr/login/login.html  chrome
    set selenium implicit wait  10
    input text  id=uesername   auto
    input text  id=password    sdfsdfsdf
    click element  css = .btn-success
#    开始添加课程
    click element
    input text
    input text
    input text
    click element

#    获取元素
    ${eles}  get webelements

