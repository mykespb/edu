#! /usr/bin/env python3
# python3, quicksort
# myke 2019-01-27 1.2
# non-swap version of quicksort,
# with magic creation of qsorted subarrays

import random

LEN = 10        # array length
TNUM = 10       # # of tests to do

tests = [ [random.randint (1, 10) for i in range(LEN)] for j in range(TNUM) ]

def run():
    """ run all tests """
    for test in tests:
        print ("\n--------------------------------\n")
        print ("from", test)
        res = dotest (test)
        print ("to  ", res)

def dotest (a):
    """ do qsort """

    if len (a) < 2: return a[:]

    pivot = a[len(a) // 2]

    left  = [x for x in a if x <  pivot]
    mid   = [x for x in a if x == pivot]
    right = [x for x in a if x >  pivot]

    res = dotest(left) + mid + dotest(right)

    return res

run()


# ~ --------------------------------

# ~ from [5, 1, 7, 4, 10, 3, 2, 3, 9, 5]
# ~ to   [1, 2, 3, 3, 4, 5, 5, 7, 9, 10]

# ~ --------------------------------

# ~ from [7, 3, 10, 8, 5, 4, 9, 10, 7, 10]
# ~ to   [3, 4, 5, 7, 7, 8, 9, 10, 10, 10]

# ~ --------------------------------

# ~ from [8, 7, 3, 9, 9, 6, 5, 8, 6, 5]
# ~ to   [3, 5, 5, 6, 6, 7, 8, 8, 9, 9]

# ~ --------------------------------

# ~ from [9, 2, 10, 1, 1, 10, 8, 5, 8, 3]
# ~ to   [1, 1, 2, 3, 5, 8, 8, 9, 10, 10]

# ~ --------------------------------

# ~ from [6, 3, 2, 3, 4, 10, 6, 7, 5, 8]
# ~ to   [2, 3, 3, 4, 5, 6, 6, 7, 8, 10]

# ~ --------------------------------

# ~ from [1, 10, 3, 10, 9, 8, 6, 4, 2, 8]
# ~ to   [1, 2, 3, 4, 6, 8, 8, 9, 10, 10]

# ~ --------------------------------

# ~ from [10, 5, 9, 6, 10, 1, 10, 1, 9, 6]
# ~ to   [1, 1, 5, 6, 6, 9, 9, 10, 10, 10]

# ~ --------------------------------

# ~ from [5, 9, 5, 8, 4, 6, 7, 9, 9, 5]
# ~ to   [4, 5, 5, 5, 6, 7, 8, 9, 9, 9]

# ~ --------------------------------

# ~ from [6, 7, 4, 9, 8, 10, 3, 2, 6, 1]
# ~ to   [1, 2, 3, 4, 6, 6, 7, 8, 9, 10]

# ~ --------------------------------

# ~ from [1, 8, 6, 9, 1, 2, 6, 7, 1, 1]
# ~ to   [1, 1, 1, 1, 2, 6, 6, 7, 8, 9]


