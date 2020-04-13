*** Settings ***
Library  courseaction
Library  SeleniumLibrary
<<<<<<< HEAD
=======
Library  Collections
>>>>>>> 138f8b7a9108e44b203fde456990b5c6084ea1ef
*** Test Cases ***

case1
    [Setup]  deleteAllCourse
<<<<<<< HEAD
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
=======
    open browser   http://localhost:90/mgr/login/login.html   chrome
    set selenium implicit wait  10
    input text  id=username      auto
    input text  id=password     sdfsdfsdf
    click element  css = .btn-success
#    开始添加课程
    click element   css = [ng-click="showAddOne=true"]
    input text  css = [ng-model="addData.name"]             课程1
    input text  css = [ng-model="addData.desc"]             课程描述
    input text  css = [ng-model="addData.display_idx"]         1
    click element  css = [ng-click="addOne()"]
#检查课程是否被添加
    sleep  2
    ${eles}      get webelements     css = tbody td:nth-child(2)
    ${courses}    evaluate   [eles.text  for ele in  $eles]
#    FOR  ${ele}   in  @{eles}
#        append to list   ${courses}    ${ele.text}
#    END
#判断课程是否被添加
#    should contain   ${courses}   课程1
    should be true   '课程1' in $courses
    close browser







>>>>>>> 138f8b7a9108e44b203fde456990b5c6084ea1ef

