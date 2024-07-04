#/usr/bin/env python

# Mikhail Kolodin, prod2grups.py, 2023-08-3-, 2023-08-30, 1.0

# Есть набор чисел.
# Надо разбить его на 2 группы так, чтобы произведения чисел в них были одинаковы.
# Найти количество уникальных пар.

from math import prod
from itertools import compress

def rev(s: str) -> list[int]:
    """reverse binary string to int list"""

    sout = []
    for c in s:
        sout.append( 1 if c == '0' else 0 )

    return sout


def sepa(ints: list[int]) -> None :
    """разделяет на 2 группы, печатает всё подходящее, считает количество"""

    print(f"{ints=}")
    lena = len(ints)
    if lena < 2:
        print("solutions: none")
        return
    
    res = []

    for n in range(1, 2**lena-1):
        
        leftpattern = [int(x) for x in list(f"{n:0{lena}b}")]
        rightpattern = [x for x in rev(list(f"{n:0{lena}b}"))]
        left = list(compress(ints, leftpattern))
        right = list(compress(ints, rightpattern))
        # print(f"{leftpattern=}, {left=}, {rightpattern=}, {right=}")

        if prod(left) == prod(right):
            res.append((left, right))

    ores = []
    for e in res:
        if (e[0], e[1]) not in ores and (e[1], e[0]) not in ores:
            ores.append(e)

    print("number of solutions:", len(ores))
    print(f"solutions: {ores}")


sepa([2, 4, 8])
sepa([2, 4, 6, 10, 22, 25, 40, 66])
sepa([1])
sepa([])

