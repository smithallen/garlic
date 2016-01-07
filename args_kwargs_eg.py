#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: smithallen
# @Date:   2016-01-06 17:58:53
# @Last Modified by:   smithallen
# @Last Modified time: 2016-01-07 11:50:34
'''
use *args and **kwargs
*args: arbitrary number positional arguments as a tuple
**kwargs: arbitrary number keyword arguments as a dictionary

positional arguments MUST before keyword arguments
'''


def foo(x, *args, **kwargs):
    print x
    print args
    print kwargs


foo(1, 2, 3, 4, y=10, z=20)

'''
outputs:
1
(2, 3, 4)
{'y': 10, 'z': 20}
'''
