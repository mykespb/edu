#!/usr/bin/env python3
# python3, mergesort
# myke 2019-01-27 1.0

# make 10 tests of merge sorting with 2 random lists of random size

import random

def filler():
    """ fill testing complect """
    return [random.randint(0, 9) for x in range (random.randint (0,5)) ]

def tester():
    """ run tests """
    for num  in range(10):
        a = sorted (filler())
        b = sorted (filler())
        c = merge (a, b)
        d = sorted (a+b)
        print ("\nsource a=", a, "\nsource b=", b, "\nsorted c=", c, "\ngood   d=", d)

def merge (a, b):
    """ merge 2 arrays """

    lena = len(a)
    lenb = len(b)
    ai = bi = 0
    c = []

    while ai < lena and bi < lenb:
        av = a[ai]
        bv = b[bi]
        if av < bv:
            c += [av]
            ai += 1
        else:
            c += [bv]
            bi += 1
    if ai < lena:
        c += a[ai:lena]
    elif bi < lenb:
        c += b[bi:lenb]

    return c

tester()


# ~ source a= []
# ~ source b= [5, 7]
# ~ sorted c= [5, 7]
# ~ good   d= [5, 7]

# ~ source a= [6]
# ~ source b= [1, 6, 7, 9, 9]
# ~ sorted c= [1, 6, 6, 7, 9, 9]
# ~ good   d= [1, 6, 6, 7, 9, 9]

# ~ source a= [2, 2, 3]
# ~ source b= [1, 1, 3, 6]
# ~ sorted c= [1, 1, 2, 2, 3, 3, 6]
# ~ good   d= [1, 1, 2, 2, 3, 3, 6]

# ~ source a= [7, 7, 9, 9]
# ~ source b= [4]
# ~ sorted c= [4, 7, 7, 9, 9]
# ~ good   d= [4, 7, 7, 9, 9]

# ~ source a= [0, 4, 8, 9]
# ~ source b= [4, 6, 6, 9, 9]
# ~ sorted c= [0, 4, 4, 6, 6, 8, 9, 9, 9]
# ~ good   d= [0, 4, 4, 6, 6, 8, 9, 9, 9]

# ~ source a= []
# ~ source b= [0, 1, 4, 5]
# ~ sorted c= [0, 1, 4, 5]
# ~ good   d= [0, 1, 4, 5]

# ~ source a= []
# ~ source b= [0, 5, 9]
# ~ sorted c= [0, 5, 9]
# ~ good   d= [0, 5, 9]

# ~ source a= [2, 6, 8, 9, 9]
# ~ source b= []
# ~ sorted c= [2, 6, 8, 9, 9]
# ~ good   d= [2, 6, 8, 9, 9]

# ~ source a= []
# ~ source b= [0, 1, 2, 7, 7]
# ~ sorted c= [0, 1, 2, 7, 7]
# ~ good   d= [0, 1, 2, 7, 7]

# ~ source a= [3, 6, 9, 9, 9]
# ~ source b= [3, 8, 9]
# ~ sorted c= [3, 3, 6, 8, 9, 9, 9, 9]
# ~ good   d= [3, 3, 6, 8, 9, 9, 9, 9]

