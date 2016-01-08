#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yujinlun
# @Date:   2016-01-08 10:51:39
# @Last Modified by:   smithallen
# @Last Modified time: 2016-01-08 11:16:36

'''
use yield to make generator
'''


def fabonacci():
    '''
    fabonacci function
    '''
    a = 1
    b = 2

    while True:
        yield a
        tmp = a
        a = b
        b = tmp + b

count = 1
foo = fabonacci()
while count <= 10:
    print foo.next()
    count = count + 1

# ============================
print "=" * 10


def fabonacci2():
    a = 1
    b = 2
    while True:
        yield a
        a, b = b, a + b

foo2 = fabonacci2()

for i in xrange(10):
    print foo2.next()
