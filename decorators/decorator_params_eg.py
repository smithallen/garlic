#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: smithallen
# @Date:   2016-01-06 17:44:34
# @Last Modified by:   yujinlun
# @Last Modified time: 2016-01-07 09:34:50
'''
decorator with params
'''


def decorator(argument):
    '''
    decorator with params
    '''
    def _real_decorator(func):
        '''
        wrapper func
        '''
        print "use decorator param x:{0}".format(argument)

        def __newfunc(*args, **kwargs):
            print args
            print kwargs
            print "do something before func"
            ret = func(*args, **kwargs)
            print "do something after func"
            return ret
        return __newfunc

    return _real_decorator


@decorator(10)
def foo(x, y, z=0):
    return x + y + z


print foo(1, y=2, z=3)
