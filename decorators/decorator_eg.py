#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: smithallen
# @Date:   2016-01-06 16:22:54
# @Last Modified by:   smithallen
# @Last Modified time: 2016-01-06 17:42:49
'''
decorator use both no parametered and parametered
'''


def decorator1(func):
    '''
    wrapper func
    '''
    def __newfunc(*args, **kwargs):
        print "do something before func"

        ret = func(*args, **kwargs)

        print "do something after func"

        return ret

    return __newfunc


def foo(x, y, z=0):
    return x + y + z

foo = decorator1(foo)
print foo(1, 2, 3)


@decorator1
def foo_1(x, y, z=0):
    return x + y + z

print foo_1(1, 2, 3)
