*** Settings ***
#创建一个RF测试套件，包含下面的一个用例
#用例名：
#验证当系统中没有课程的时候，是否能成功添加一个课程
#前置条件：
#系统中没有课程

#测试步骤：
#添加课程，输入课程名、详情描述、展示次序，点击创建

#预期结果：
#创建的课程正确显示在下面的课程列表中。
#这里为了简化，我们只检查 课程名就可以了

#注意：
#这个用例的初始化和清除操作，都是需要设置为无课程状态。
#需要我们开发一个python测试库，使用selenium库开发关键字函数deleteAllCourse， 实现使用Python自动点击删除课程按钮