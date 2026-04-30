#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-04-30 2026-04-30 1.1
# two-by-three.py

# ~ Даны (или получены случайно) 2 групы натуральных чисел по 6 чисел  в каждой.
# ~ Можно ли переставить в них числа так, чтобы последние 3 числа первой группы
# ~ и первые 3 числа из второй группы совпадали?
# ~ Показать все совпадения, или сказать, что их нет.
# ~ Одинаковые с точностью до перестановок чисел комбинации считать за одну.


from random import randint
from itertools import permutations

SIZE = 6
MIN  = 1
MAX  = 9

def make():
    return (
        [randint(MIN, MAX) for _ in range(SIZE)], 
        [randint(MIN, MAX) for _ in range(SIZE)]
        )

def comp(a, b):
    res = []  # left, common, right
    common = []

    for pl in permutations(a, 3):
        for pr in permutations(b, 3):
            if (pc := pl[-3:]) == pr[:3]:
                if (spc:= sorted(pc)) not in common:
                    common.append(spc)
                    res.append( (sorted(a[:3]), spc, sorted(b[3:]) ) )
    
    return res
    

def main():
    a, b = make()
    print("got:  ", a, b)
    res = comp(a, b)
    if not res:
        print("found: no solutions")
    else:
        for r in res:
            print("found:", r)

main()


# ~ got:   [7, 9, 2, 3, 9, 2] [1, 3, 2, 2, 8, 5]
# ~ found: [([2, 7, 9], [2, 2, 3], [2, 5, 8])]

# ~ got:   [4, 9, 3, 7, 3, 9] [6, 4, 1, 2, 1, 6]
# ~ found: no solutions

# ~ got:   [6, 4, 1, 2, 6, 3] [6, 3, 7, 2, 4, 2]
# ~ found: ([1, 4, 6], [2, 4, 6], [2, 2, 4])
# ~ found: ([1, 4, 6], [3, 4, 6], [2, 2, 4])
# ~ found: ([1, 4, 6], [2, 3, 6], [2, 2, 4])
# ~ found: ([1, 4, 6], [2, 3, 4], [2, 2, 4])
