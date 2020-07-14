*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}         http://localhost:90/mgr/login/login.html
&{user1}       username=auto   pw=sdfsdfsdf

*** Keywords ***
loginwebsite
    open browser     ${url}        chrome
    ${ele_user}    Get WebElement   id=username
    ${ele_pw}      Get WebElement   id=password
    ${ele_user}  delete all cookies
    ${ele_pw}       delete all cookies
    input text     id=username     &{user1}[username]
    input text     id=password     &{user1}[pw]
    click element  css=.btn-success
addcource
    [Arguments]  ${name}   ${desc}   ${idx}
    click element   css=[ng-click="showAddOne=true"]
    input text      css=[ng-model="addData.name"]    ${name}
    input text      css=[ng-model="addData.desc"]   ${desc}
    input text      css=[ng-model="addData.display_idx"]       ${idx}
    click element   css=[ng-click="addOne()"]
    sleep  2
#    close browser
checkcource
    [Arguments]  ${expect}
    ${text}   get text    css=tbody td:nth-child(2)
    should be true  $text == $expect
