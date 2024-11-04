#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2024-11-04 2024-11-04 0.1
# hilldown.py

# ~ Дан прямоугольный массив (списков списков).
# ~ Поставить в каждую клетку высоту над уровнем моря, начиная с 0 от краёв,
# ~ и повышая на 1 на каждый шаг к центру.

def gen(rows=5, cols=5):
    """создаёт массив"""

    return [ [ 0 for j in range(cols) ] for i in range(rows) ]


def solve1(a):
    """решение 1"""

    rows = len(a)
    cols = len(a[0])
    top = max(rows, cols) // 2 + 1

    return top


def main():
    """запуск"""

    a = gen()
    print(solve1(a))


main()
