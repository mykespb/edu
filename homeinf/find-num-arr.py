#!/usr/bin/env python3
# (C) Mikhail Kolodin, 2025
# find-num-arr.py
# 2025-11-18 2025-12-05 1.1

# ~ Дан упорядоченный список натуральных чисел.
# ~ Определить, есть ли в нём заданное число.
# ~ Ищем методом половинного деления (дихотомия).

from random import randint

def make(size=32) -> list:
    """make a list"""

    arr = [randint(1, 2*size) for _ in range(size)]
    arr.sort()
    return arr


def check(arr: list, num: int) -> bool:
    """check array for num"""
    
    left = 0
    size = len(arr)
    right = size - 1

    were = (left, right)

    while left < right:
        # ~ print(f"{left=}, {right=}")
        middle = left + (right - left) // 2
        if arr[middle] == num:
            return True
        if arr[middle] > num:
            right = middle
        else:
            left = middle

        if were == (left, right): break
        were = (left, right)
        

    return False
    

def main():
    """do it"""

    arr = make()
    print("array is", arr)

    for num in 1, 0, 2, 5, 10, 16, 25, 31, 32:
        print("---------------------------------------------")
        print(f"search for {num}:")
        has = check(arr, num)
        print(f"result: {has}")


main()
