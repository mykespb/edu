#!/usr/bin/env python3
# ls-subarraymaxavg.py
# (C) Mikhail Kolodin, 2023
# 2023-01-28 2023-01-28 1.1
# LeetCode problem

from random import randint

# EPS = 1e-5    # not important

def avg(arr: list[int]) -> float:
    if len(arr) == 0: return 0
    return sum(arr) / len(arr)

def subarray(arr: list[int], k: int):
    la = len(arr)
    if not la: return 0

    maxavg = None
    for i in range(la-k+1):
        val = avg(arr[i : i+k])
        if not maxavg:
            maxavg = val
        else:
            if val > maxavg:
                maxavg = val

    return maxavg

def tests(count: int = 1):
    for rep in range(count):
        array = [randint(-10, 10) for _ in range(10)]
        k = randint(1, len(array)-1)
        print(f"test {rep+1}: {array=}, max sum = {subarray(array, k)}")

tests(10)

nums = [1, 12, -5, -6, 50, 3]
k = 4
print(f"+test 1: {nums=}, {k=}, result={subarray(nums, k)}")

nums = [5]
k = 1
print(f"+test 1: {nums=}, {k=}, result={subarray(nums, k)}")

# Максимальное среднее подмассива
# (https://leetcode.com/problems/maximum-average-subarray-i/description/)
# Сложность: Лёгкая
# Условие задачи: дается целочисленный массив nums, состоящий из n элементов и целого числа k.
# Найдите непрерывный подмассив, длина которого равна k, который имеет максимальное среднее значение, и верните это значение. Будет принят любой ответ с ошибкой вычисления менее 10-5.
# Пример:
# Ввод: nums = [1,12,-5,-6,50,3], k = 4
# Вывод: 12.75000
# Объяснение:
# Ввод:  nums = [5], k = 1
# Вывод: 5.00000

# test 1: array=[-1, -8, -9, -8, -8, -1, 8, 9, 4, -4], max sum = -1.125
# test 2: array=[-8, -2, -7, 9, -9, -7, -2, -1, 0, -5], max sum = -2.6666666666666665
# test 3: array=[8, -10, -3, -10, -10, -2, -7, -9, 4, 6], max sum = 8.0
# test 4: array=[-4, -8, 7, 7, -2, -6, -4, 4, 10, -5], max sum = 0.4
# test 5: array=[5, -6, 9, -5, 2, 0, 1, 0, -7, -2], max sum = 1.1666666666666667
# test 6: array=[-1, 3, 9, 5, 8, -3, 6, -10, -5, -1], max sum = 9.0
# test 7: array=[-5, 4, -5, -2, 0, -4, 0, 3, 9, -9], max sum = 2.0
# test 8: array=[7, 6, 6, -5, 4, -2, -4, -9, -8, -9], max sum = 1.7142857142857142
# test 9: array=[-3, 9, -3, 10, 5, -2, -7, 2, 0, 0], max sum = 1.75
# test 10: array=[6, -10, 7, 5, 9, 4, -4, 4, 2, -7], max sum = 6.25
# +test 1: nums=[1, 12, -5, -6, 50, 3], k=4, result=12.75
# +test 1: nums=[5], k=1, result=5.0
