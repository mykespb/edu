#!/usr/bin/env python

# Mikhail Kolodin
# 2022-04-18 2022-04-18 v.2.0

# make non-intersecting rectangles in big rectangle area
# version with less tests

from mkrects import getrect, show

def mysolver(aa):
    """solve - finf rects"""
    
    maxy = len(aa)
    maxx = len(aa[0])
    a = [[0 for i in range(maxx+1)] for j in range(maxy+1)]
    
    for i in range(maxy):
        for j in range(maxx):
            a[i+1][j+1] = aa[i][j]
    
    maxy = len(a)
    maxx = len(a[0])
    num = 0
    
    for y in range(1, maxy):
        for x in range(1, maxx):            
            if a[y][x] == 1 and a[y-1][x] == 0 and a[y][x-1] == 0:
                num += 1
                
    return num


def mytest():
    """default test"""
    rect = getrect()
    show(rect)
    print("found rects:", mysolver(rect))


if __name__ == "__main__":
    mytest()
