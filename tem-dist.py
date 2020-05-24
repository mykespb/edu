#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# tem-dist.py
# 2020-05-24 0.1
# (C) Mikhail (myke) Kolodin, 2020
#
# program scans current directory and puts into subdirectories fiels with names
# that are compatible with patterns set in file tem-dist.tpl

__version__ = "0.1"
__date__    = "2020-05-24"

tpls = []
files = []

def main(args):
    """ main dispatcher """

    print (f"This is tem-dist, ver. {__version__} of {__date__}")
    get_tpl()
    get_files()
    scan_all()
    print_report()
    return 0

def get_tpl():
    pass

def get_files():
    pass

def scan_all():
    pass

def print_report():
    pass

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
