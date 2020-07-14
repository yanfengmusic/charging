*** Settings ***
Variables  cfg.py



*** Variables ***
##全局变量表 只支持常量 且必须是RF格式的
${url}     http://localhost:90/mgr/login/login.html
@{data}    a b c d  3306
&{user1}     username=auto    pw=sdfsdfsdf

*** Keywords ***
#资源文件不可以包含用例表
loginWebsite
    go to   ${url}
    input text  id=username      &{user1}[username]
    input text  id=password      &{user1}[pw]
    click element  css = .btn-success
addCourse
    [Arguments]  ${name}   ${desc}    ${idx}
    click element   css = [ng-click="showAddOne=true"]
    input text  css = [ng-model="addData.name"]             ${name}
    input text  css = [ng-model="addData.desc"]             ${desc}
    input text  css = [ng-model="addData.display_idx"]      ${idx}
    click element  css = [ng-click="addOne()"]
    sleep  2
checkCourse  [Documentation]  判断元素
    [Arguments]  ${expect}
    ${eles}       Get WebElement     css = tbody td:nth-child(2)
    ${courses}    evaluate  [ele.text for ele in $eles]
    should be true  $expect in $courses

deleteAllCourse
    loginWebsite
    set selenium implicit wait  1
    FOR   ${i}  IN RANGE   9999
        ${delete_buttons}     Get WebElements   css=[ng-click="delOne(one)"]
        exit for loop if   $delete_buttons == []
        evaluate   $delete_buttons[0].click()
        sleep  2
        click element   css=.btn-primary
        sleep  1
    END
websetup
    open browser    http://localhost     chrome
    set selenium implicit wait  10
webtearown
    close browser
