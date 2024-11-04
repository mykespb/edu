#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2024-11-04 2024-11-04 1.1
# hilldown.py

# ~ Дан квадратный массив (списков списков).
# ~ Поставить в каждую клетку высоту над уровнем моря, начиная с 0 от краёв,
# ~ и повышая на 1 на каждый шаг к центру.

def mprint(a, width=4):
    """напечатать матрицу"""
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(f"%{width}d" % a[i][j], end="")
        print()
        

def gen(size=5):
    """создаёт массив"""

    return [ [ 0 for j in range(size) ] for i in range(size) ]


def solve(a):
    """решение"""

    size = len(a)
    for i in range(size // 2 + 1):
        for j in range(size-i*2):
            a[i][i+j] = a[size-i-1][i+j] = a[i+j][i] = a[i+j][size-i-1] = i

    return a


def main(size=3):
    """запуск"""

    print("\nПоле", size, "порядка")
    a = gen(size)
    mprint(solve(a))


main()
main(5)
main(7)
main(9)


# ~ Поле 3 порядка
   # ~ 0   0   0
   # ~ 0   1   0
   # ~ 0   0   0

# ~ Поле 5 порядка
   # ~ 0   0   0   0   0
   # ~ 0   1   1   1   0
   # ~ 0   1   2   1   0
   # ~ 0   1   1   1   0
   # ~ 0   0   0   0   0

# ~ Поле 7 порядка
   # ~ 0   0   0   0   0   0   0
   # ~ 0   1   1   1   1   1   0
   # ~ 0   1   2   2   2   1   0
   # ~ 0   1   2   3   2   1   0
   # ~ 0   1   2   2   2   1   0
   # ~ 0   1   1   1   1   1   0
   # ~ 0   0   0   0   0   0   0

# ~ Поле 9 порядка
   # ~ 0   0   0   0   0   0   0   0   0
   # ~ 0   1   1   1   1   1   1   1   0
   # ~ 0   1   2   2   2   2   2   1   0
   # ~ 0   1   2   3   3   3   2   1   0
   # ~ 0   1   2   3   4   3   2   1   0
   # ~ 0   1   2   3   3   3   2   1   0
   # ~ 0   1   2   2   2   2   2   1   0
   # ~ 0   1   1   1   1   1   1   1   0
   # ~ 0   0   0   0   0   0   0   0   0

