# -*- coding: utf-8 -*-
# @Author: smithallen
# Project: garlic
# File: print_color.py

'''
from http://jyotiska.github.io/blog/posts/adding_color_to_python_output.html
'''


class styles:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'


if __name__ == "__main__":
    print styles.BLUE + "hello, this is a test string" + styles.ENDC
    print styles.GREEN + styles.BOLD + "hello, this is a test string" + styles.ENDC
    print styles.WARNING + styles.UNDERLINE + "hello, this is a test string" + styles.ENDC
