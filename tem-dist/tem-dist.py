#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# tem-dist.py
# 2020-05-24 2021-05-15 1.11
# (C) Mikhail (myke) Kolodin, 2020
#
# program scans current directory and puts into subdirectories fiels with names
# that are compatible with patterns set in file tem-dist.tpl

__version__ = "1.11"
__date__    = "2021-05-15"

import os, os.path, pathlib
import pprint
import shutil

cwd = os.getcwd()

tpl_file = 'tem-dist.tpl'
tpls = []
no_tpl = 0
good_exts = "epubl pdf txt djv jpeg djvu doc docx epub fb2 arj zip rar lzh tar png gif jpg xml bmp pic mp3 mp4 avi 7z xz pptx ppt xls xlsx odt odp odx flv html htm mobi mht mhtml chm md gz".split()

files = []

def main(args):
    """ main dispatcher """

    print (f"This is tem-dist by myke, ver. {__version__} of {__date__}")
    print (f"current directoory is {cwd}")
    get_tpl()
    get_files()
    scan_all()
    print_report()
    return 0

def get_tpl():
    """ get list of templates"""

    global no_tpl
    progpath = os.path.dirname(__file__)
    tplpath = progpath + '/' + tpl_file
    if os.path.isfile (tplpath):
        print (f"file {tplpath} exists ok, working")
        with open (tplpath) as tplfile:
            for tplka in tplfile:
                tpl = tplka.strip()
                if tpl.startswith("#"): continue
                if len(tpl) == 0: continue

                no_tpl += 1
                pat, dir = tpl.split(maxsplit=1)
                print (no_tpl, tpl, "=>", pat, dir)

                tpls.append((tuple(pat.split(",")), dir))

    else:
        print (f"file {tplpath} does not exist, quitting")
        raise "no template file"

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

    good, bad = 0, 0

    for myfile in files:
        print (f"\n{myfile}", end="")

        ext = (myfile.split('.')[-1]).lower()
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
        subfile = myfile.lower()
        for tpl in tpls:
            for word in tpl[0]:
                if word not in subfile:
                    break
            else:
                if not tpl[1]: break
                original  = cwd + "/" + myfile
                targetdir = cwd + "/" + tpl[1]
                target    = cwd + "/" + tpl[1] + "/" + myfile
                print (f"! file {myfile} goes to {tpl[1]}\n! {original} -> {target}")
                if not os.path.isdir(targetdir):
                    pathlib.Path(targetdir).mkdir(parents=True, exist_ok=True)
                shutil.move (original, target)
                good += 1
                break

        else:
            original  = cwd + "/" + myfile
            targetdir = cwd + "/etc"
            target    = cwd + "/etc/" + myfile
            print (f"! file {myfile} goes to etc\n{original} -> {target}")
            if not os.path.isdir(targetdir):
                pathlib.Path(targetdir).mkdir(parents=True, exist_ok=True)
            shutil.move (original, target)
            bad += 1

    print (f"\nResult: {good} file(s) and {bad} bad file(s)\n")

def print_report():
    """ print what we did"""
    pass

#    print ("\nTemplates read: ")
#    pprint.pprint (tpls)
#    print ("\nFiles to scan", files)


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

