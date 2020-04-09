*** Keywords ***
#资源文件不可以包含用例表
loginWebsite
    open browser   http://localhost:90/mgr/login/login.html   chrome
    set selenium implicit wait  10
    input text  id=username      auto
    input text  id=password     sdfsdfsdf
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
    ${eles}      get webelements     css = tbody td:nth-child(2)
    ${courses}    evaluate  [ele.text for ele in $eles]
    should be true  $expect in $courses

deleteAllCourse
    loginWebsite
    set selenium implicit wait  1
    FOR  ${i}  IN RANGE  9999
        ${delete_buttons}    get webelement     css = //tbody/tr/td[4]/button[2]
        exit for loop if  $delete_buttons == []
        set selenium implicit wait  1
        evaluate  delete_buttons[0].click()
        sleep  1
        click element   css=btn.btn-primary
        sleep  1
    END

    CLOSE BROWSER
