*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
用例1
    ${a}   evaluate  [i for i in range (10)]
    log to console  ${a}
    log to console  @{a}

