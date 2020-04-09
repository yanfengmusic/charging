*** Settings ***

*** Test Cases ***
case1
    [Template]  loginandcheck
    abc   123   sucessd
    sdjjkh    ijh    ljh




*** Keywords ***
getvar1
    ${var}  evaluate  [i for i in range(10)]
    [Return]  ${var}

loginandcheck
    [Arguments]  ${name}   ${desc}    ${idx}
    log to console  ${name}   ${desc}    ${idx}
