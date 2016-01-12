#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: smithallen
# @Date:   2016-01-05 16:31:45
# @Last Modified by:   smithallen
# @Last Modified time: 2016-01-06 16:32:23

'''
show how to use singleton
'''
import threading

# use decorator


def singleton(custom_class):
    instances = dict()
    lock = threading.Lock()

    def _singleton(*args, **kwargs):

        try:
            lock.acquire()
            if custom_class not in instances:
                instances[custom_class] = custom_class(*args, **kwargs)
            return instances[custom_class]
        except Exception, e:
            raise e
        finally:
            lock.release()

    return _singleton


@singleton
class MyClass1(object):
    pass


def test_MyClass1():
    '''
    test decorator
    '''
    myclass1_one = MyClass1()
    myclass1_another = MyClass1()
    print id(myclass1_one) == id(myclass1_another)

# ============================================

# use metaclass


class Singleton(type):
    _instances = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class MyClass2(object):
    __metaclass__ = Singleton


def test_MyClass2():
    '''
    test metaclass
    '''
    myclass2_one = MyClass2()
    myclass2_another = MyClass2()
    print id(myclass2_one) == id(myclass2_another)

# ==============================================
# over write __new__


class MyClass3(object):
    __instance = None

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(MyClass3, cls).__new__(cls, *args, **kwargs)

        return cls.__instance


def test_MyClass3():
    '''
    test over write __new__
    '''
    myclass3_one = MyClass3()
    myclass3_another = MyClass3()
    print id(myclass3_one) == id(myclass3_another)

# ==========================================================
'''
最简单有效的方法
使用import,因为模块只初始化一次，且import机制是线程安全的，保证了
在并发状态下，模块也只有一个实例。
'''


if __name__ == '__main__':
    test_MyClass1()
    test_MyClass2()
    test_MyClass3()
