#!/usr/bin/env python
# Mikhail Kolodin, 2023
# 2023-02-06 2023-02-07 1.2
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
    # ~ arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    return arr

arr = make()
print(arr)

# ~ б. решение

def solve1(arr: list[int]) -> int:
    """найти недостающее, используем операцию проверки вхождения"""

    print("solve1:", end=" ")
    al = len(arr)
    for el in range(al+1):
        if el not in arr:
            print("не хватает", el)
            return el

def solve2(arr: list[int]) -> int:
    """найти недостающее, используем сортировку"""

    print("solve2:", end=" ")
    arr.sort()
    al = len(arr)
    for i in range(al):
        if arr[i] != i:
            print("не хватает", i)
            return i
    else:
            print("не хватает", al)
            return al

def solve3(arr: list[int]) -> int:
    """найти недостающее, используем сумму"""

    print("solve3:", end=" ")
    al = len(arr)
    need_sum = al * (al+1) // 2
    have_sum = sum(arr)
    num = need_sum - have_sum
    print("не хватает", num)
    return num
    
        
# ~ в. тестирование

solve1(arr)
solve2(arr)
solve3(arr)
