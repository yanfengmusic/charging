#!/usr/bin/env python
# -*- coding: utf-8 -*-

__mtime__ = '2020-01-28'

class Tiger:
    nickName = '老虎'
    def __init__(self,inWeight):#初始化方法---只要创建实例，这个方法会自动调用
        self.weight = inWeight# t1.weight = 100  t2.weight = 200
        print('我是Tiger-----init----')

    #叫---实例方法
    def roar(self):
        print('我是老虎----wow!，体重减少5斤')
        self.weight -= 5#体重减少5斤
    #吃---方法
    def feed(self,food):
        if food == '肉':
            self.weight += 10
            print('恭喜，喂食正确，体重增加10斤！')
        else:
            self.weight -= 10
            print('抱歉，喂食错误，体重减少10斤！')

    #静态方法---所有的实例都一样的操作
    @staticmethod
    def static_roar():
        print('静态方法---wow!')

class Room:
    #2个：编号  动物
    def __init__(self,inNum,inAnimal):
        self.num = inNum
        self.animal = inAnimal

# t1 = Tiger(200)
# # print(f'操作前的体重:{t1.weight}')
# # t1.roar()#老虎1.叫
# # t1.feed('草')#老虎1.喂食
# # print(f'操作后的体重:{t1.weight}')
# # t1.static_roar()
# # Tiger.static_roar()
#
# r1 = Room(2,t1)
# #这个房间的老虎--叫一声   房间实例2.动物.叫
# r1.animal.roar()



#------------游戏初始化-------------创建10个房间实例 1- 10  动物是随机放
#随机数--怎么取
# from random import randint
# # print(randint(0,2))#双闭区间   0 1 2
# roomList = []#存放房间实例---10
# for one in range(1,11):#1- 10
#     if randint(0,1) ==1:
#         ani = Tiger()
#     else:
#         ani = Sheep()
#     room = Room(one,ani)#房间实例
#     roomList.append(room)
#
#
# #时间差
# import time
# print(time.time())#1970到现在时间的秒数
#
# startTime = time.time()
#
# while True:
#     curTime = time.time()
#     if curTime-startTime >= 20:
#         break


#继承:业务需求--扩展------节省重复代码量
#举例：

class SouthTiger(Tiger):
    age = 20#子类独有的
    def __init__(self,inName):
        Tiger.__init__(self,inWeight=200)
        self.name = inName



s1 = SouthTiger("laoshu")
# print(s1.nickName)
# print(s1.weight)
# print(s1.age)

'''
继承：
    1- 如果子类没有 __init__方法，会自动调用父类的__init__
    2- 在父类的实例属性不够用的时候，子类自己有__init__方法，不会自动调用，就意味不会继承！
        如果话需要继承，手动调用

方法重写：是多态一种体现
    一个方法在父类和子类有不同的操作
    什么时候使用重写：父类有一个方法a  ,但是子类去继承，发现a方法不满足子类，
    为了保持整体一个模式，会重写这个方法，适合子类
'''



#1- 定义类
# class Tiger:
#     #1- 静态属性：这个特征属于整个类所有的实例--大家一样的特征
#     nickName = '老虎'
#     #2- 大家有些特征不是一样的----实例属性：每一个实例这个特征可以不一样
#     def __init__(self,inWeight):#初始化方法---只要创建实例，这个方法会自动调用
#         # print(self,'----我被执行了----',inWeight)
#
#         self.weight = inWeight# t1.weight = 100  t2.weight = 200
#
#         #self--本身  谁用就是谁自己
#
#     def create(self,inAge):#必须自己调用才可以有age属性
#         self.age = inAge
#
# #创建实例---使用t1变量，方便后续使用实例对象t1
# # t1 = Tiger()
# # print(t1.nickName)#1、实例.属性  2、类.属性---print(Tiger.nickName) 修改：Tiger.nickName = ‘其他值’
#
# t1 = Tiger(100)
# print(t1.weight)
#
# t2 = Tiger(200)
# print(t2.weight)
# # print(t1)


# class Tiger:
#     def roar(self):
#         print('父类-Tiger-的实例方法')
#
#     @staticmethod
#     def tell():
#         print('父类Tiger-的静态方法')
#
# class Sheep:
#     def roar(self):
#         print('父类-Sheep-的实例方法')
#
#     @staticmethod
#     def tell():
#         print('父类-Sheep-的静态方法')
#
# class SouTiger(Tiger,Sheep):
#     def roar(self):
#         print('子类的实例方法')
#
#     @staticmethod
#     def tell():
#         print('子类的静态方法')
#
# s1 = SouTiger()#创建子类、
# #1- 直接使用，就直接调用子类自己的方法
# s1.roar()
# #调用父类的实例方法---第一个父类优先
# super(SouTiger,s1).roar()
# #调用父类的静态方法---第一个父类优先
# super(SouTiger,s1).tell()
#
# super(Tiger,s1).tell()
#
# #那么我们要调用第2个父类的方法---super(你要调用的那个父类的前一个父类-类名,s1).roar()
# #1- 调用第2个父类的实例方法
# super(Tiger,s1).roar()
# #2-调用第2个父类的静态方法
# super(Tiger,s1).tell()


# 普通用户---父类--查看个人信息操作
# 自动化学员---子类---重写
#
# 好处：用户对象.查看数据()

# 日志代码：
import logging
from logging.handlers import RotatingFileHandler
import datetime
print(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S'))
STYLE = {
        'fore':
        {   # 前景色
            'black'    : 30,   #  黑色
            'red'      : 31,   #  红色
            'green'    : 32,   #  绿色
            'yellow'   : 33,   #  黄色
            'blue'     : 34,   #  蓝色
            'purple'   : 35,   #  紫红色
            'cyan'     : 36,   #  青蓝色
            'white'    : 37,   #  白色
        },

        'back' :
        {   # 背景
            'black'     : 40,  #  黑色
            'red'       : 41,  #  红色
            'green'     : 42,  #  绿色
            'yellow'    : 43,  #  黄色
            'blue'      : 44,  #  蓝色
            'purple'    : 45,  #  紫红色
            'cyan'      : 46,  #  青蓝色
            'white'     : 47,  #  白色
        },

        'mode' :
        {   # 显示模式
            'mormal'    : 0,   #  终端默认设置
            'bold'      : 1,   #  高亮显示
            'underline' : 4,   #  使用下划线
            'blink'     : 5,   #  闪烁
            'invert'    : 7,   #  反白显示
            'hide'      : 8,   #  不可见
        },

        'default' :
        {
            'end' : 0,
        },
}


def UseStyle(string, mode = '', fore = '', back = ''):

    mode  = '%s' % STYLE['mode'][mode] if STYLE['mode'].get(mode) else ''

    fore  = '%s' % STYLE['fore'][fore] if STYLE['fore'].get(fore) else ''

    back  = '%s' % STYLE['back'][back] if STYLE['back'].get(back) else ''

    style = ';'.join([s for s in [mode, fore, back] if s])

    style = '\033[%sm' % style if style else ''

    end   = '\033[%sm' % STYLE['default']['end'] if style else ''

    return '%s%s%s' % (style, string, end)


'''
debug：最细微的信息记录到debug中，这个级别就是用来debug的，看程序在哪一次迭代中发生了错误，比如每次循环都输出一些东西用debug级别
info：级别用于routines，也就是输出start finish 状态改变等信息
warn：输出一些相对重要，但是不是程序bug的信息，比如输入了错误的密码，或者连接较慢
error：输出程序bug，打印异常信息
critical：用于处理一些非常糟糕的事情，比如内存溢出、磁盘已满，这个一般较少使用
'''
class Logger:
    def __init__(self,inLevel='DEBUG',inName=__name__):
        self.logger = logging.getLogger(inName)
        self.logger.setLevel(inLevel)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def addHand(self,source):
        self.logger.addHandler(source)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)#

    def critical(self, msg):
        self.logger.critical(msg)

class FileLogger(Logger):#log文件输出类

    def __init__(self, logName):
        Logger.__init__(self, inLevel='DEBUG', inName=__name__)
        self.loggerName = logName
        self.rHandler = RotatingFileHandler("{}_{}.log".format(self.loggerName,datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')),maxBytes = 1*1024,backupCount = 3,encoding='utf-8')
        self.rHandler.setFormatter(self.formatter)
        self.addHand(self.rHandler)

class ConsoleLogger(Logger):#控制台输出日志类

    def __init__(self):
        Logger.__init__(self, inLevel='DEBUG', inName=__name__)
        self.console = logging.StreamHandler()
        self.console.setFormatter(self.formatter)
        self.addHand(self.console)
    def debug(self, msg):
        self.logger.debug(UseStyle(msg, fore = 'black'))#黑色

    def info(self, msg):
        self.logger.info(UseStyle(msg, fore = 'blue'))#蓝色

    def warning(self, msg):
        self.logger.warning(UseStyle(msg, fore = 'yellow'))#黄色

    def error(self, msg):
        self.logger.error(UseStyle(msg, fore = 'red'))#红色

    def critical(self, msg):
        self.logger.critical(UseStyle(msg, fore = 'purple'))#紫红色



# log = ConsoleLogger()
log = FileLogger('songqin_vip_xt')
log.debug('调试')
log.info('信息')
log.warning('警告')
log.error('错误')
log.critical('糟糕')
