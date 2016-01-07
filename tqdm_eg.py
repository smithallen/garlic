#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: smithallen
# @Date:   2016-01-06 15:31:31
# @Last Modified by:   smithallen
# @Last Modified time: 2016-01-06 15:42:54
'''
how to use tqdm to instantly make your loops show a smart progress meter
tqdm can be found in https://github.com/tqdm/tqdm
'''

import time
from tqdm import tqdm, trange

for i in tqdm(range(100)):
    time.sleep(0.1)

for i in trange(10, desc='1st loop', leave=True):
    for j in trange(5, desc='2nd loop', leave=True, nested=True):
        for k in trange(100, desc='3nd loop', leave=True, nested=True):
            time.sleep(0.01)
