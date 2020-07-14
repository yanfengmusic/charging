*** Settings ***
Library    pylib.WebOpAdmin



*** Test Cases ***
添加课程1
    [Setup]  deleteAllCourse
#    loginWebsite
    addCourse          robot    robot课程    2
    ${course}          GetCourseList
    should be true     $course==[u'robot']
添加课程2
    [Setup]   deleteAllCourse
    loginWebsite
    addCourse          test    test课程    1
    ${course}          GetCourseList
    should be true     $course==[u'test']
#    closeBrower










