#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# filing-sizes.py
# 2025-02-25 2025-02-25 1.1

# работа с файлами. учебное
# адаптировано для работы с interview.cups
# найти все файлы размером более 1КБ

import os

path = './tmp/'

def get_files(limit: int = 1000):
    """распечатать большие файлы"""

    dir_list = os.listdir(path)
    print("\nshowing all files", *dir_list, sep=", ", end="\n\n")

    cnt = 0
    for afile in dir_list:
        size = os.path.getsize(path + afile)
        if size > limit:
            print(f"big file: '{afile}' has size of {size} bytes")
            cnt +=1

    if cnt:
        print(f"\n{cnt} - big files found\n")
    else:
        print(f"\nno big files found\n")
        

get_files()


# ~ showing all files, transacts.pickle, arithm-seq.txt, intext.txt, eisenhower.pickle, outtext.txt
# ~ big file: transacts.pickle has size of 7068 bytes
