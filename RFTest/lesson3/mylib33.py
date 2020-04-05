import requests
import os,sys
from selenium import webdriver

def check_score(num):
    assert num>60

def getWebInfo():
    response = requests.get('http://mirrors.163.com/centos/timestamp.txt')
    return response.text


def opencalc():
    os.system('calc')

def openmspaint():
    os.system('mspaint')

def printarg(*args,**kwargs):

    if len(args) == 0:
        print('** no args **')
    else:
        print('** args are **')
        print('-----------------')
        for one in args:
            print(repr(one))
        print('-----------------')

    if len(kwargs) == 0:
        print('** no kwargs **')
    else:
        print('** kwargs are **')
        print('-----------------')
        for k,v in kwargs.items():
            print(repr(k) + ':' + repr(v))
        print('-----------------')



def returnlist():
    return [1,2,3]

def returndict():
    return {
        'ele1' : 'male',
        'ele2' : 'female'
    }


if __name__ == '__main__':
    # import requests
    # data={'action':'delete_course','id':1234}
    # res=requests.delete('http://localhost/api/mgr/sq_mgr/',data=data)
    # print(res.text)
    print(getWebInfo())