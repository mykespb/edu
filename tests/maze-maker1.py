#!/usr/bin/env python3
# maze-maker1.py
# (C) Mikhail Kolodin, 2024
# 2024-11-11 2024-11-11 1.0

# Сгенерировать проходимый лабиринт заданного размера.
# Идём с (0, 0) до (край, край) сверху-слева вниз-вправо.

# Обозначения:  0 = пусто, 1 = стена.

# Идея: сначала обеспечить проходимость,
# а потом почти случайно заполнить остальную плоскость.


from random import randint
from itertools import product


def maker(size : int = 5) -> list[list[int]]:
    """make maze"""
    
    # step 1 - create list
    
    ms = size - 1
    opts = 0, 1
    
    a = [ [ 0  for _ in range(size) ] for _ in range(size) ]
    
    # step 2 make a path
    
    i, j = 0, 0
    while 1:
        # if i >= size or j >= size:
        #     break
        a[i][j] = 2
        if i == ms and j == ms:
            break
        if randint(0, 1):
            if i < ms:
                i += 1
        else:
            if j < ms:
                j += 1
    
    # make random filling
    
    for i, j in product(range(size), range(size)):
        if a[i][j] == 0:
            a[i][j] = randint(0, 1)
    
    # clean 

    for i, j in product(range(size), range(size)):
        if a[i][j] == 2:
            a[i][j] = 0
    
    return a
    

def mprint(a, width=4):
    """напечатать матрицу"""
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"%{width}d" % a[i][j], end="")
        print()
    

def main():
    a = maker()
    mprint(a)

    
main()


# results:

#    0   0   1   1   1
#    0   0   1   0   0
#    1   0   0   0   0
#    0   0   0   1   1
#    0   0   0   0   0
   
#    0   0   0   0   0
#    0   0   0   1   0
#    0   0   0   0   0
#    0   1   0   0   0
#    1   1   0   0   0
   
#    0   0   0   0   1
#    0   1   1   1   1
#    0   1   1   0   0
#    0   1   1   0   0
#    0   0   0   0   0
   