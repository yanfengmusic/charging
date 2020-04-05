*** Settings ***
Library  mylib4

*** Test Cases ***
测试1
    ${html}=    getwebinfo
    run keyword if    '2019' in $html and 'UTC1' in $html
    ...     log to console   \n2019年的,UTC时间
    ...     ELSE IF     'Jan' in $html  log to console  Jan11111
    ...     ELSE    log to console   ${html}



