#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-06-06 2026-06-06 1.0
# permut.py

# ~ Сделать свой генератор перестановок и протестировать

from math import log10
from random import randint
from itertools import permutations

# ~ общий генератор данных

def make():
    return sorted([ randint(100, 999) for _ in range(10) ])


# ~ генератор перестановок 

def permut(lst : list):

    if len(lst) == 0:
        yield []
    else:
        for i in range(len(lst)):
            current_element = lst[i]
            remaining_elements = lst[:i] + lst[i + 1 :]

            for p in permut(remaining_elements):
                yield [current_element] + p

# Пример использования:
# ~ items = ["A", "B", "C"]
# ~ for p in permut(items):
    # ~ print(p)

# Результат:
# ['A', 'B', 'C']
# ['A', 'C', 'B']
# ['B', 'A', 'C']
# ['B', 'C', 'A']
# ['C', 'A', 'B']
# ['C', 'B', 'A']


def perm2(x : int):

    lst = list(str(x))
    for p in permut(lst):
        yield p
    
# ~ perm2(123)

# ~ тестирование

perm = perm2

def solver(x : int):

    for p in perm(x):
        num = int("".join(p))
        if num % 7 == 0:
            print(f"{x} as {num} = 7 * {num // 7}")
            break
    else:
        print(f"{x} failed")

# ~ solver(123)


def main():
    seq = make()
    for num in seq:
        sol = solver(num)

main()


# ---------------------------------------

# ~ problem:  [226, 231, 347, 407, 502, 796, 838, 896, 899, 971] => [231, 796, 896, 971]
# ~ divisors: {231: (231, 33.0), 796: (679, 97.0), 896: (896, 128.0), 971: (917, 131.0)}

# ~ https://docs.python.org/3/library/itertools.html#itertools.permutations

# ~ https://docs.python.org/3/library/functions.html#int
# ~ https://docs.python.org/3/library/stdtypes.html
# ~ https://www.w3schools.com/python/ref_func_str.asp
