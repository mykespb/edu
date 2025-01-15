#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2025
# 2025-01-15 2025-01-15 1.0
# matrix-nums.py

# ~ Найти максимальное число из цифр

# ~ Есть прямоугольная матрица десятичных цифр. 
# ~ Многие клетки заполнены нулями.
# ~ Ненулевые клетки образуют натуральные числа.
# ~ Найти максимальное.

# ~ извесно, что:
# ~ 1. записи чисел не конфликтуют, т.е. не накладываются друг на друга никоим образом,
# ~ кроме предписанного.

# ~ варианты:
# ~ +а. Числа записаны просто по горизонтали.
# ~ +б. Числа могут быть записаны по кругу, т.е. из крайнего правого столбца переходят в крайний левый.
# ~ -в. Числа могут быть записаны только по вертикали.
# ~ -г. Числа могут быть записаны и по горизонтали, и по вертикали, но они не пересекаются.
# ~ -д.... или пересекаются.
# ~ (+) реализовано, (-) варианты на дз

# --------------------------------------
# установки и импорты

HEIGHT = 20                 # высота матрицы
WIDTH  = 80                 # ширина матрицы
LENGTH = 10                 # макс длина числа
NUMBER = HEIGHT             # количество чисел

from random import randint as ri

# --------------------------------------
# генерация

def genmatrix():
    """создать случайную матрицу с числами"""

    global mat

    # матрица
    mat = [ [ 0 for x in range(WIDTH) ] for y in range(HEIGHT) ]

    # числа разместим с перехлёстом, в каждой строчке
    ipos = ri(0, WIDTH-1)
    
    for inum in range(NUMBER):
        
        for i in range(ri(1, 9)):
            dig = ri(1,9)
            mat[inum][(ipos + i) % WIDTH] = dig
        
        ipos = (ipos + ri(LENGTH, LENGTH+30)) % WIDTH


# --------------------------------------
# поиск

def gde():
    """найти все, выбрать лучшее"""

    best = 0         # значение
    bi = bj = -1     # координаты начала

    for j in range(HEIGHT):
        for i in range(WIDTH):
            ii = i
            if mat[j][ii]:
                if ii == 0:
                    while mat[j][ii % WIDTH]:
                        ii -= 1
                nova = 0
                starti = ii
                while mat[j][ii % WIDTH]:
                    nova = nova * 10 + mat[j][ii % WIDTH]
                    ii += 1
                if nova > best:
                    best = nova
                    starti = bi = ii
                    bj = j                    
                break

    return best, bj, starti
    

# --------------------------------------
# вывод и запуск

def show():
    """показ матрицы"""

    for j in range(HEIGHT):
        print(f"{j:02d} ", end="")
        for i in range(WIDTH):
            print(mat[j][i], end="")
        print()
    print()


def main():
    genmatrix()
    show()

    best, bj, bi = gde()
    print(f"наибольшее число {best} найдено в позиции {bj}, {bi % WIDTH}")


main()

# --------------------------------------
# результаты

# ~ 00 00000000000000000000000000000000000000053690000000000000000000000000000000000000
# ~ 01 00000000000000000000000000000000000000000000000000000007998149000000000000000000
# ~ 02 00000000023847600000000000000000000000000000000000000000000000000000000000000000
# ~ 03 00000000000000000000000000000000000002410000000000000000000000000000000000000000
# ~ 04 00000000000000000000000000000000000000000000000000000000000005997100000000000000
# ~ 05 00000000000000007000000000000000000000000000000000000000000000000000000000000000
# ~ 06 00000000000000000000000000000000000000000006792985300000000000000000000000000000
# ~ 07 00000000000000000000000000000000000000000000000000000000000000049852150000000000
# ~ 08 00000000050000000000000000000000000000000000000000000000000000000000000000000000
# ~ 09 00000000000000000000000000000000000089754123000000000000000000000000000000000000
# ~ 10 00000000000000000000000000000000000000000000002852496700000000000000000000000000
# ~ 11 00001733370000000000000000000000000000000000000000000000000000000000000000000000
# ~ 12 00000000000000000318710000000000000000000000000000000000000000000000000000000000
# ~ 13 00000000000000000000000000000000000000000000000000000025850000000000000000000000
# ~ 14 00000000000000000000000000000000000000000000000000000000000000000000000001572000
# ~ 15 00000000000000000000745334266000000000000000000000000000000000000000000000000000
# ~ 16 00000000000000000000000000000000000000000000000099000000000000000000000000000000
# ~ 17 42357752000000000000000000000000000000000000000000000000000000000000000000000004
# ~ 18 00000000000000000000000000000000000636670000000000000000000000000000000000000000
# ~ 19 00000000000000000000000000000000000000000000000000000000000000004936695160000000

# ~ наибольшее число 745334266 найдено в позиции 15, 64

# --------------------------------------
