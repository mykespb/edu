#!/usr/bin/env python
# Mikhail Kolodin, 2023
# 2023-02-06 2023-02-07 1.1
# ya-arr-wo-num.py

# ~ Задача из яндекса.
# ~ На входе массив целых чисед, перемешанных,
# ~ одно число улалили,
# ~ найти его.

# ~ а. подготовка данных

from random import randint, shuffle

def make(num: int =10) -> list[int]:
    """подготовка данных"""

    arr = [i for i in range(num)]
    ex = randint(0, num-1)
    del arr[ex]
    shuffle(arr)
    return arr

arr = make()
print(arr)

# ~ б. решение

def solve1(arr: list[int]) -> int:
    """найти недостающее"""

    al = len(arr)
    for el in range(al):
        if el not in arr:
            print("не хватает", el)
            return el

def solve2(arr: list[int]) -> int:
    """найти недостающее"""

    arr.sort()
    al = len(arr)
    for i in range(al):
        if arr[i] != i:
            print("не хватает", i)
            return i
            
# ~ в. тестирование

solve1(arr)
solve2(arr)
