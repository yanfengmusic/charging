*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
case1
    checklog1
    checklog2   110022
    ${res}  checklog3  5555
    log to console  ${res}

*** Keywords ***
checklog1
    ${var}   set variable  hello
    log to console  ${var}
    should be true  $var == 'hello'

checklog2
    [Arguments]  ${expect}
    ${var}   set variable  ${expect}
    log to console  ${var}
    should be true  $var == $expect
checklog3
    [Arguments]  ${expect}
    ${var}   set variable  ${expect}
    log to console  ${var}
    should be true  $var == $expect
    [Return]  Success


