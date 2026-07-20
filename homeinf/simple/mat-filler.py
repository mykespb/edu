#!/usr/bin/env python
# Mikhail Kolodin, 2024
# mat-filler.py
# 2024-10-09 2024-10-11 1.3
# fill matrix

import random
from pprint import pp

# 0. better print

def pmat(m, width=4):
    """print matrix"""

    for i in range(len(m)):
        for j in range(len(m[0])):
            print(f"%{width}d" % m[i][j], end = " ")
        print()

# 1. fill from ul corner

def fill1(size=3):
    
    return [ [ i+j for j in range(size) ] for i in range(size) ]

pmat(fill1(5))

   # ~ 0    1    2    3    4 
   # ~ 1    2    3    4    5 
   # ~ 2    3    4    5    6 
   # ~ 3    4    5    6    7 
   # ~ 4    5    6    7    8 


# 2. fill from center as cross

def fill2(size=3):

    center = size // 2
    return [ [ min( abs(center - i), abs(center - j)) for j in range(size) ] for i in range(size) ]

# ~ pmat(fill2(5))

   # ~ 2    1    0    1    2 
   # ~ 1    1    0    1    1 
   # ~ 0    0    0    0    0 
   # ~ 1    1    0    1    1 
   # ~ 2    1    0    1    2 

