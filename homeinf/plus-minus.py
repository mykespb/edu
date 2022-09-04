#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-09-04 2022-09-04 0.1
# plus-minus.py

# ~ выставляем оценки ученикам по плюсам и минусам

import random

marks = {
    "+++": 5,
    "++-": 4,
    "+--": 3,
    "---": 2
    }

def tests(times=1, size=1):
    """make all tests"""
    
    for num in range(times):
        test(num, size)
        

def gen(size=1):
    """generate sequence of + and - groups"""

    out = ""
    for i in range(size):
        out += random.choice("+-") + random.choice("+-") + random.choice("+-")
    return out
    

def test(num, size):
    """make 1 test"""

    arr = gen(size)
    out = []

    for portion in range(len(arr) // 3):
        i0 = portion * 3
        i1 = (portion+1) * 3

        index = list(arr[i0:i1])
        index.sort()
        index = "".join(index)
        out += [marks[index]]

    print("student", num, "got", arr, "marks", out)

tests(10, 10)
