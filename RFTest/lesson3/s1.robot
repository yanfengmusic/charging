*** Settings ***
Library   mylib33
Library  Dialogs
Library  Collections
Library  Collections   #操作列表的包
*** Test Cases ***
测试1
    ${res}  getWebInfo
    log to console   ${res}
    run keyword if   '2020' in $res   log to console   测试通过



#测试2
    #获取接口返回
#    ${text}   getwebinfo
#    #打印变量
#    log to console  ${text}   #$text这种写法只能用于python表达式类型的参数中
#    #如果2020再返回的字符串中，就打印测试通过
#    run keyword if  '2020' in $text and 'UTF' in $text
    #换行...之后至少空两格
#    ...          log to console  测试通过
#    ...          ELSE IF   'Wed123' in $text   log to console   今天是周三
#
#    #ELSE不可以小写
#    ...           ELSE    log to console  测试不通过

测试3
#
#    FOR  ${i}  IN RANGE   99
#
#    ${score}  get value from user    请输入成绩
#    run keyword if   $score  == 'cont'    continue for loop
#    run keyword if   $score  == 'over'    exit for loop
#    run keyword if  int($score) >= 60   log to console  及格
#    ...     ELSE  log to console  不及格
#    END

#跳出循环的另外一种写法  ???为什么一定要是这个顺序呢
#    FOR   ${i}   IN RANGE  99
#    ${score}  get value from user  请输入成绩
#    continue for loop if     $score == 'cent'
#    EXIT FOR LOOP if   $score == 'over'
#    run keyword if     int($score) >= 60     log to console  及格
#    ...   ELSE  log to console  不及格
#    END


#测试4
#    ${list}  create list   a,b,c
#    FOR  ${i}  IN  @{list}
#        log to console  ${i}
#    END
#    append to list   ${list}   d,e,f   aaa
#    log to console   ${list}
#     evaluate  $list.append(2020)
#     log to console  ${list}
#     evaluate  [print(i) for i in ${list}]

测试5
    ${dict1}   create dictionary  a=1  b=3  c=2
    set to dictionary  ${dict1}   e = 4  f=5
<<<<<<< HEAD
    evaluate   $dict['a'] = 2020   #evaluate不能使用赋值操作，因为他本身就是调用的eval(),eval就不支持赋值操作的
=======
    evaluate   $dict['a'] = 2020  #使用evaluate时，他调用的是eval,本身就是不能被赋值的东西
>>>>>>> 138f8b7a9108e44b203fde456990b5c6084ea1ef
    log to console   ${dict1}









