#!/usr/bin/env python

# Mikhail Kolodin
# 2022-04-11 2022-04-12 v.1.1

# make non-intersecting rectangles in big rectangle area

from mkrects import getrect, show

def mysolver(a):
    """solve - finf rects"""
    
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
                
            elif a[y-1][x] == 0 and a[y][x-1] == 0:
                num += 1
                
    return num


def mytest():
    """default test"""
    rect = getrect()
    show(rect)
    print("found rects:", mysolver(rect))


if __name__ == "__main__":
    mytest()
