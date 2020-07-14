*** Settings ***
Library  mylib33
Library  Dialogs


*** Test Cases ***
#case1  [Documentation]  简单条件判断
#    ${year}  set variable  2020
#    run keyword if   $year == '2020'   log to console  测试通过
#    should be true   ${year}=='2020'
#    log to console   ${year}

#case2  [Documentation]  条件判断换行,条件成立只能执行一个关键字
#    ${date}  get time
#    log to console  ${date}
#    run keyword if   '2020' in $date and '06' in $date
#    ...     log to console  pass
#    log to console  ${date}

#case3  [Documentation]
#    check score1   59

case4  [Documentation]      条件判断 ELSE  ELSE IF 要求是大写
    ${date}   get time
    log to console  ${date}
    run keyword if    '2021' in $date    log to console  今年是2020年
    ...     ELSE IF   '06' in $date      log to console  本月是06月
    ...     ELSE    log to console   结束

case5  [Documentation]  FOR循环 关键字需要大写

    FOR  ${one}   IN RANGE   9999
    ${score}    get value from user   请输入你的分数        #需要引入dialog库
    run keyword if  $score == 'over'   exit for loop           #结束循环
    run keyword if  $score == 'cont'   continue for loop       #跳出本次，继续循环
    check score1    ${score}
    END


