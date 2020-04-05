*** Settings ***
Library  course_mgr
Library  SeleniumLibrary
Library  huawei

*** Test Cases ***
用例1
    [Documentation]  验证课程信息是否正确
    ${dict_course}  listCourse
    FOR  ${i}  In  @{dict_course}
        log to console  ${i}
    END

    should be true  ${dict_course['retcode']}== 0
用例2
    [Documentation]  获得所有热销单品的名称，打印在log报表中
    ${list_data}   get_info
    FOR  ${one}  In  @{list_data}
        log to console  ${one}
    END


