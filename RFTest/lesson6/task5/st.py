import time

from selenium import webdriver

def deleteAllLesson():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://localhost/mgr/login/login.html')
    driver.find_element_by_id('username').send_keys('auto')
    driver.find_element_by_id('password').send_keys('sdfsdfsdf')
    driver.find_element_by_css_selector('.btn-success').click()
    #删除所有课程
    driver.implicitly_wait(1)
    while 1:
        del_btns = driver.find_elements_by_css_selector('[ng-click="delOne(one)"]')
        if del_btns == []:
            print('课程删除完毕')
            break

        del_btns[0].click()
        #点击确认
        driver.find_element_by_css_selector('.btn-primary').click()
        #等待弹出框消失
        time.sleep(1)

    driver.quit()


if __name__ == '__main__':
    deleteAllLesson()