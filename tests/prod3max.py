#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-12-14 2022-12-14 1.0
# prod3max.py

# даны случайные числа [-100 .. 100],
# найти произведение 3 макс различных чисел

from random import randint
from math import prod

MINVAL = -100   # мин. число
MAXVAL = 100    # макс. число
LEN    = 10     # длина массива
SUB    = 3      # длина вырезки
TESTS  = 10     # сколько тестов

def doit():
    """ выполнить 1 тест """

    arr = [randint(MINVAL, MAXVAL) for _ in range(LEN)]
    print("исходный массив", arr)

    vals = sorted(list(set(arr)), reverse=True)[:SUB]
    res  = prod(vals)
    print("числа:", vals, ", произведение:", res)

# выполнить все тесты
for test in range(1, TESTS+1):
    print("\nтест №", test)
    doit()


# примечание:
# если различных чисел менее 3, возьмутся только различные, пусть их 2 или 1
# (меньше 1 быть не может :) )

# ~ тест № 1
# ~ исходный массив [44, 64, 26, 98, 60, 0, -69, 100, -60, -10]
# ~ числа: [100, 98, 64] , произведение: 627200

# ~ тест № 2
# ~ исходный массив [-72, 29, -48, -43, 76, 12, -20, 48, 47, -40]
# ~ числа: [76, 48, 47] , произведение: 171456

# ~ тест № 3
# ~ исходный массив [-24, 24, -14, -14, -49, 71, 74, -53, 42, 1]
# ~ числа: [74, 71, 42] , произведение: 220668

# ~ тест № 4
# ~ исходный массив [-63, -74, -53, -75, 61, -68, -25, 47, -31, 4]
# ~ числа: [61, 47, 4] , произведение: 11468

# ~ тест № 5
# ~ исходный массив [30, -57, -37, -66, 88, -1, 18, 37, 83, -80]
# ~ числа: [88, 83, 37] , произведение: 270248

# ~ тест № 6
# ~ исходный массив [67, 54, -68, -52, -54, -87, -62, -77, -74, 13]
# ~ числа: [67, 54, 13] , произведение: 47034

# ~ тест № 7
# ~ исходный массив [-97, 84, 89, -45, -34, 28, 97, -81, -74, -35]
# ~ числа: [97, 89, 84] , произведение: 725172

# ~ тест № 8
# ~ исходный массив [-4, -5, -42, -62, -64, -94, 83, 36, -58, -82]
# ~ числа: [83, 36, -4] , произведение: -11952

# ~ тест № 9
# ~ исходный массив [73, -12, 67, -74, -94, -93, -51, 58, 27, -32]
# ~ числа: [73, 67, 58] , произведение: 283678

# ~ тест № 10
# ~ исходный массив [27, -86, -97, 52, -17, 52, 46, 78, -51, -88]
# ~ числа: [78, 52, 46] , произведение: 186576

