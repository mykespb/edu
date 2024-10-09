#!/usr/bin/env python
# Mikhail Kolodin, 2024
# mat-filler.py
# 2024-10-09 2024-10-09 1.1
# fill matrix

import random
from pprint import pp

# 0. better print

def pmat(m):
    """print matrix"""

    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end = " ")
        print()

#1. fill from ul corner

def fill1(size=3):
    
    return [ [ i+j for j in range(size) ] for i in range(size) ]

pmat(fill1(5))

# ~ 0 1 2 3 4 
# ~ 1 2 3 4 5 
# ~ 2 3 4 5 6 
# ~ 3 4 5 6 7 
# ~ 4 5 6 7 8 
