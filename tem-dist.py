#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# tem-dist.py
# 2020-05-24 2020-05-25 0.2
# (C) Mikhail (myke) Kolodin, 2020
#
# program scans current directory and puts into subdirectories fiels with names
# that are compatible with patterns set in file tem-dist.tpl

__version__ = "0.2"
__date__    = "2020-05-25"

import os, os.path
import pprint

cwd = os.getcwd()

tpl_file = 'tem-dist.tpl'
tpls = []
no_tpl = 0
good_exts = "pdf txt djv djvu doc docx".split()

files = []

def main(args):
    """ main dispatcher """

    print (f"This is tem-dist, ver. {__version__} of {__date__}")
    print (f"current directoory is {cwd}")
    get_tpl()
    get_files()
    scan_all()
    print_report()
    return 0

def get_tpl():
    """ get list of templates"""

    global no_tpl
    if (os.path.isfile (tpl_file)):
        print (f"file {tpl_file} exists ok, working")
        with open (tpl_file) as tplfile:
            for tplka in tplfile:
                tpl = tplka.strip()
                if tpl.startswith("#"): continue
                if len(tpl) == 0: continue

                no_tpl += 1
                pat, dir = tpl.split(maxsplit=1)
                print (no_tpl, tpl, "=>", pat, dir)

                tpls.append((tuple(pat.split(",")), dir))

    else:
        print (f"file {tpl_file} does not exist, quitting")
        raise "no template file"
    pass

def get_files():
    """ get current files list """
    global files

    files = os.listdir('.')
    if files:
        print (f"ok, got {len(files)} files to test")
    else:
        print ("alas, no files found in current directory")

def scan_all():
    """ scan all files names and move them to subdi\rectories
    according to their names, comapred to all compex templates"""

    for myfile in files:
        print (myfile, end="")
        ext = myfile.split('.')[-1]
        if myfile.startswith('.'):
            print (" - is a dot-file, skipping")
            continue
        if os.path.isdir(myfile):
            print  (" - is directory, skipping")
            continue
        if ext not in good_exts:
            print (" - probably not a documentation file, skipping")
            continue
        print (f" - processing file {myfile}")


def print_report():
    """ print what we did"""

    print ("\nTemplates read: ")
    pprint.pprint (tpls)

    print ("\nFiles to scan", files)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

