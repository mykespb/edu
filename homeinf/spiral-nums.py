#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-08 2022-04-08 1.0
# spiral-nums.py

# ~ ДЗ1. Числа по спирали

# ~ Дано натуральное число n.
# ~ Создать квадратную матрицу (список списков) и заполнить её натуральными числами от 1 по возрастанию
# ~ вар. а) от левого верхнего угла по часовой стрелке до центра,
# ~ вар. б) от центра по часовой стрелке до краёв.
# ~ Пример вар.1 для n=3:
# ~ 1  2  3
# ~ 8  9  4
# ~ 7  6  5
# ~ вар.2 для n=3
# ~ 7  8  9
# ~ 6  1  2
# ~ 5  4  3

def pp(a):
    """печать красиво"""

    size = len(a)
    print(f"\n{size=}\n")
    for i in range(size):
        for j in range(size):
            print(f"{a[i][j]:5}", end=" ")
        print()

debug = 0

def deb(*v):
    global a, i, j, k
    if not debug: return
    print(*v)
    pp(a)


def goleft():
    global a, i, j, k, size
    k += 1
    j -= 1
    if i<0 or i>=size or j<0 or j>=size: return
    a[i][j] = k
    deb(k, i, j)
    
def goright():
    global a, i, j, k, size
    k += 1
    j += 1
    if i<0 or i>=size or j<0 or j>=size: return
    a[i][j] = k
    deb(k, i, j)
    
def goup():
    global a, i, j, k, size
    k += 1
    i -= 1
    if i<0 or i>=size or j<0 or j>=size: return
    a[i][j] = k
    deb(k, i, j)
    
def godown():
    global a, i, j, k, size
    k += 1
    i += 1
    if i<0 or i>=size or j<0 or j>=size: return
    a[i][j] = k
    deb(k, i, j)
    

def centerout(s=3):
    """от центра наружу, по часовой, размер=size"""
    global a, i, j, k, size
    size = s
    assert size>0 and size<30

    sq = size*size

    a = [[0 for i in range(size)] for j in range(size)]

    if size%2:
        # нечётное
        i = j = size // 2 
        a[i][j] = 1
        nums = 1
        k = 1

        while k < sq:
            for p in range(nums):
                goright()
            for p in range(nums):
                godown()
            nums += 1
            for p in range(nums):
                goleft()
            for p in range(nums):
                goup()
            nums += 1
        
    else:
        # чётное
        i = size // 2 - 1
        j = size // 2 
        a[i][j] = 1
        nums = 1
        k = 1

        while k < sq:
            for p in range(nums):
                godown()
            for p in range(nums):
                goleft()
            nums += 1
            for p in range(nums):
                goup()
            for p in range(nums):
                goright()
            nums += 1

    pp(a)
    

def borderin(s=3):
    """снаружи к центру, по часовой, размер=size"""
    global a, i, j, k, size
    size = s
    assert size>0 and size<30

    sq = size*size

    a = [[0 for i in range(size)] for j in range(size)]

    i = j = 0
    a[0][0] = 1
    nums = size-1
    k = 1

    if size%2:
        # нечётное
        for p in range(nums):
            goright()
        while k < sq:
            for p in range(nums):
                godown()
            for p in range(nums):
                goleft()
            nums -= 1
            for p in range(nums):
                goup()
            for p in range(nums):
                goright()
            nums -= 1
            
        
    else:
        # чётное
        for p in range(nums):
            goright()
        while k < sq:
            for p in range(nums):
                godown()
            for p in range(nums):
                goleft()
            nums -= 1
            for p in range(nums):
                goup()
            for p in range(nums):
                goright()
            nums -= 1

    pp(a)


for size in range(1, 7):
    centerout(size)
    borderin(size)
