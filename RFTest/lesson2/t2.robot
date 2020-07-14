*** Test Cases ***
case1
#如何使用变量和电仪的时候是没有关系的，只和传参的时候有关
    ${list}  create list  1   2   3
#    log many  ${list}  #以一个整体的形式来传参
#    log many  @{list}    #以list形式多个参数参数
    log many  ${list[0]}
    log many  @{list}[1]
case2
    ${dict}   create dictionary    a=15555    b=2    c=3
    log many  ${dict}        #以一个整体的形式来传参
    log many  &{dict}       #以键值对的形式多个参数参数
    log many  ${dict['a']}
    log many  &{dict}[a]   #rf会默认带上引号

case3  [Documentation]  for循环老语法

        :FOR   ${A}  IN   A    B    C
        \     log to console    ${A}
        log to console   循环体外面

case4  [Documentation]  for循环新语法
        FOR  ${a}  in   a   b   c              #爆红是因为插件比较老，不支持新语法
        log to console  ${a}
        END
        log to console    循环体外面


        [Documentation]  新语法整合
        ${list}   create list    a  b  c  d  e
        FOR  ${a}  in   @{list}           #爆红是因为插件比较老，不支持新语法
        log to console  ${a}
        END
        log to console    循环体外面


case4  [Documentation]  FOR循环-Range
    FOR  ${S}  IN RANGE   10    #IN RANGE是一个整体 所以只能是一个空格  FOR IN RANGE  END需要都是大写  不然会报警告
    LOG TO CONSOLE  ${S}
    END
    log to console  结束循环



case5  [Documentation]  FOR循环-Range指定循环区间
    FOR  ${S}  IN RANGE   5   10    #IN RANGE是一个整体 所以只能是一个空格  FOR IN RANGE  END需要都是大写  不然会报警告
    LOG TO CONSOLE  ${S}
    END
    log to console  结束循环


case6  [Documentation]  FOR循环-Range 步长用法
    FOR  ${S}  IN RANGE   2    10    2
    LOG TO CONSOLE  ${S}
    END
    log to console  结束循环





