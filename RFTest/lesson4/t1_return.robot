*** Test Cases ***
case1
    log to console  1
    ${list}  getvar1
    log to console  ${list}



*** Keywords ***
getvar1
    ${var}  evaluate  [i for i in range(10)]
    [Return]  ${var}
