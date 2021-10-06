#!/usr/bin/env python3
# coding: utf-8

# simply  know parameters of platform used, from python dis-list, corrected
# 2014-06-21, 2019-01-27
# 2021-05-16
# 2021-10-06

import platform

def print_sysinfo():

    print('Python version  :', platform.python_version())
    print('compiler        :', platform.python_compiler())

    print('system          :', platform.system())
    print('release         :', platform.release())
    print('machine         :', platform.machine())
    print('processor       :', platform.processor())
    #print('CPU count      :', mp.cpu_count())
    print('interpreter     :', platform.architecture()[0])
    print('\n\n')

print_sysinfo()

# ~ myke@myke-asus ~/prog/python/test $ ./machtest1.py
# ~ Python version  : 2.7.15rc1
# ~ compiler        : GCC 7.3.0
# ~ system          : Linux
# ~ release         : 4.15.0-43-generic
# ~ machine         : x86_64
# ~ processor       : x86_64
# ~ interpreter     : 64bit

# ~ myke@myke-asus ~/prog/python/test $ python3 ./machtest1.py
# ~ Python version  : 3.6.7
# ~ compiler        : GCC 8.2.0
# ~ system          : Linux
# ~ release         : 4.15.0-43-generic
# ~ machine         : x86_64
# ~ processor       : x86_64
# ~ interpreter     : 64bit

# 2021-05-17
# ~ Python version  : 3.8.5
# ~ compiler        : GCC 9.3.0
# ~ system          : Linux
# ~ release         : 5.4.0-73-generic
# ~ machine         : x86_64
# ~ processor       : x86_64
# ~ interpreter     : 64bit

# 2021-10-06
# Python version  : 3.10.0
# compiler        : GCC 9.3.0
# system          : Linux
# release         : 5.4.0-88-generic
# machine         : x86_64
# processor       : x86_64
# interpreter     : 64bit

