#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-05-21 2025-05-22 1.0
# rect-waves.py

# ~ Волны в прямоугольнике
# ~ -----------------------------
# ~ Берём случайный прямоугольник (напр., 20х30).
# ~ В случайном месте ставится цифра 1.
# ~ Вокруг неё - 2. И т.п.
# ~ После 9 идёт 1, потом 2 (ставим только цифры, 0 пропускаем).

from random import randint

DEFAULT_WIDTH  = 30
DEFAULT_HEIGHT = 20

def make(width = DEFAULT_WIDTH, height = DEFAULT_HEIGHT):
    """make rectangle"""

    return [ [ 0 for j in range(width) ] for i in range(height) ]
    

def solve(arr):
    """put all digits"""

    height = len(arr)
    width = len(arr[0])
    print(f"{width=}, {height=}")
    
    y = randint(0, height-1)
    x = randint(0, width-1)
    print(f"{x=}, {y=}")

    digitold = arr[y][x] = 1
    digitnew = 2
    need = True

    while need:
        need = False

        for row in range(height):
            for col in range(width):
                if arr[row][col] == digitold:

                    for plus in ((-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)):
                        prow, pcol = plus
                        qrow = (row+prow) % height
                        qcol = (col+pcol) % width

                        if not arr[qrow][qcol]:
                            arr[qrow][qcol] = digitnew
                            need = True

        digitold = digitnew
        digitnew = (digitnew+1) % 10
        if not digitnew:
            digitnew = 1


def test():
    """run tests"""

    arr = make()
    # ~ show(arr, "before")

    solve(arr)
    show(arr, "circles")


def show(arr, title):
    """show array"""

    print(f"\n------------------------ {title} ---------------------\n")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()


test()


# ~ width=30, height=20
# ~ x=13, y=11

# ~ ------------------------ circles ---------------------

# ~ 5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 8 7 7 7 7 7 7 7 7 7 7 7 7 7 8 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 8 7 6 6 6 6 6 6 6 6 6 6 6 7 8 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 8 7 6 5 5 5 5 5 5 5 5 5 6 7 8 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 8 7 6 5 4 4 4 4 4 4 4 5 6 7 8 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 8 7 6 5 4 3 3 3 3 3 4 5 6 7 8 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 8 7 6 5 4 3 2 2 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 8 7 6 5 4 3 2 2 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 8 7 6 5 4 3 3 3 3 3 4 5 6 7 8 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 8 7 6 5 4 4 4 4 4 4 4 5 6 7 8 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 8 7 6 5 5 5 5 5 5 5 5 5 6 7 8 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 8 7 6 6 6 6 6 6 6 6 6 6 6 7 8 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 8 7 7 7 7 7 7 7 7 7 7 7 7 7 8 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 9 1 2 3 4 5 6 7 6 
# ~ 5 4 3 2 1 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9 1 2 3 4 5 6 7 6 
