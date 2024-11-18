#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-12-25 2021-12-25 0.1
# some5.py

# ~ дана строка с натуральными  числами.
# ~ выбрать из них и напечатать только те, которые делятся на 5.

data = """12 35 67 10050 99892432984293 3345 67 55 10
3224 54543 66 11 25   45      78 90
44 66 88
5345 65647 798789 24 0090
"""

for line in data.split('\n'):
    line = line.strip()
    if not line:
        continue

    empty = True
    
    for it in line.split():
        num = it.strip()

        if num.endswith(('0', '5')):
            print(num, end=", ")
            empty = False

    if empty:
        print("no good numbers")
    else:
        print()
