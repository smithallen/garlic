#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: smithallen
# @Date:   2016-01-06 16:17:47
# @Last Modified by:   smithallen
# @Last Modified time: 2016-01-06 16:22:13
'''
Magic decorator syntax for asynchronous code in Python 2.7
https://github.com/madisonmay/Tomorrow
'''
import time
import requests

from tomorrow import threads


urls = [
    'http://google.com',
    'http://facebook.com',
    'http://youtube.com',
    'http://baidu.com',
    'http://yahoo.com',
]


@threads(5)
def download(url):
    return requests.get(url)

if __name__ == "__main__":
    start = time.time()
    responses = [download(url) for url in urls]
    html = [response.text for response in responses]
    print html
    end = time.time()
    print "Time: %f seconds" % (end - start)
