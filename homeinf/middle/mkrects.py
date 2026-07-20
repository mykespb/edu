#!/usr/bin/env python
# Mikhail Kolodin
# 2022-04-11 v.1.0

# make non-intersecting rectangles in big rectangle area

from copy import deepcopy
from math import isqrt
from random import randint

DEBUG = 0

BIGMAXWID = 50
BIGMINWID = 10
BIGMAXHIH = 20
BIGMINHIH = 10

def show(a):
    leny = len(a)
    lenx = len(a[0])
    print(f"array {leny} x {lenx}")
    for i in range(leny):
        for j in range(lenx):
            print(a[i][j], end="")
        print()

def makerect0(bminx=BIGMINWID, bmaxx=BIGMAXWID, bminy=BIGMINHIH, bmaxy=BIGMAXHIH):
    """make initial rect"""
    
    wid = randint(bminx, bmaxx)
    hih = randint(bminy, bmaxy)
    
    rect = [[0 for i in range(wid)] for j in range(hih)]
    
    return rect

def makerect1(aa):
    """make inner rects"""
    
    a = deepcopy(aa)
    maxy = len(a)
    maxx = len(a[0])
    
    many = isqrt(maxx * maxy)
    
    pmaxx = maxx*3//4
    pmaxy = maxy*3//4
    
    attmax = max(1, many)
    for attempt in range(attmax):
        
        x = randint(1, pmaxx)
        y = randint(1, pmaxy)
        xp = randint(x, maxx-2)
        yp = randint(y, maxy-2)
        
        if DEBUG: print("attempt:", attempt, "of", attmax, "with", x, y, xp, yp)
        
        good = True
        
        for i in range(y, yp+1):
            for j in range(x, xp+1):
                if a[i][j]:
                    good = False
                    break
        if not good:
            if DEBUG: print(0)
            continue
        
        if y>0:
            for j in range(x, xp+1):
                if a[y-1][j]:
                    good = False
                    break
        if not good:
            if DEBUG: print(1)
            continue
            
        if y<maxy-1:
            for j in range(x, xp+1):
                if a[y+1][j]:
                    good = False
                    break
        if not good:
            if DEBUG: print(2)
            continue
            
        if x>0:
            for i in range(y, yp+1):
                if a[i][x-1]:
                    good = False
                    break
        if not good:
            if DEBUG: print(3)
            continue
            
        if x<maxx-1:
            for i in range(y, yp+1):
                if a[i][x+1]:
                    good = False
                    break
        if not good:
            if DEBUG: print(4)
            continue
            
        for i in range(y, yp):
            for j in range(x, xp):
                a[i][j] = 1

    return a

def solver(a):
    """solve - find rects"""
    
    maxy = len(a)
    maxx = len(a[0])

    num = 0
    
    for y in range(maxy):
        for x in range(maxx):
            
            if not a[y][x]:
                continue
            
            if y == 0 and x == 0:
                num += 1
                
            elif y == 0 and a[0][x-1] == 0:
                num += 1
                
            elif x == 0 and a[y-1][0] == 0:
                num += 1
                
            # ~ elif a[y-1][x-1] == 0 and a[y-1][x] == 0 and a[y][x-1] == 0:
            elif a[y-1][x] == 0 and a[y][x-1] == 0:
                num += 1
                
    return num

def getrect():
    rect = makerect0()
    rect1 = makerect1(rect)
    return rect1

def test():
    """default test"""
    rect = makerect0()

    rect1 = makerect1(rect)
    show(rect1)

    print(__name__, "found rects:", solver(rect1))

if __name__ == '__main__':
    test()
