*** Settings ***
#Variables  cfg.py
Resource   rflib/rc.robot
Suite Setup       websetup
Suite Teardown    webtearown

*** Test Cases ***
添加课程1
    deleteAllCourse
    loginWebsite
    addCourse      robot    robot课程    2
    checkCourse     robot
添加课程2
    addCourse       自动化测试    自动化测试课程    1
    checkCourse     自动化测试
    deleteAllCourse










