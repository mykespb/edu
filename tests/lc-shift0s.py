#!/usr/bin/env python3
# ls-shift0s.py
# (C) Mikhail Kolodin, 2023
# 2023-01-27 2023-01-28 1.2
# LeetCode problem

# Сдвиг нулей
#  (https://leetcode.com/problems/move-zeroes/submissions/)Сложность: Лёгкая
# Условие задачи: дан массив, необходимо переместить все нулевые элементы к концу массива, к его правой границе. 
# Решение должно изменять исходный массив, не используя дополнительной памяти. 
# Пример:
# Ввод: nums = [0,1,0,3,12]
# Вывод: [1,3,12,0,0]
# Ввод: nums = [0]
# Вывод: [0]

def shift0(arr: list[int]) -> list[int]:
    print("input:", arr, end=" --> ")
    zeros = sum(map(lambda x: x==0, arr[:]))
    # print("zeros:", zeros)
    la = len(arr)

    left = 0
    while left < la:
        if arr[left]:
            left += 1
            continue
        if not any(arr[left:]):
            break
        arr[left : la-1] = arr[left+1: la]
        arr[-1] = 0
        if arr[left]:
            left += 1

    print("result:", arr)

# tests 

shift0([1])
shift0([1, 0, 2])
shift0([1, 0, 0, 3, 4])
shift0([0, 1, 2])
shift0([0, 1, 0, 2, 0])
shift0([0, 1, 0, 2, 0, 3, 4, 0, 5, 0, 6, 0])
shift0([0, 1, 2, 0, 3, 4, 5, 6])
shift0([0])
shift0([0, 0])
shift0([0, 0, 0])
shift0([0, 0, 0, 1, 2, 3, 0])

# input: [1] --> result: [1]
# input: [1, 0, 2] --> result: [1, 2, 0]
# input: [1, 0, 0, 3, 4] --> result: [1, 3, 4, 0, 0]
# input: [0, 1, 2] --> result: [1, 2, 0]
# input: [0, 1, 0, 2, 0] --> result: [1, 2, 0, 0, 0]
# input: [0, 1, 0, 2, 0, 3, 4, 0, 5, 0, 6, 0] --> result: [1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0, 0]
# input: [0, 1, 2, 0, 3, 4, 5, 6] --> result: [1, 2, 3, 4, 5, 6, 0, 0]
# input: [0] --> result: [0]
# input: [0, 0] --> result: [0, 0]
# input: [0, 0, 0] --> result: [0, 0, 0]
# input: [0, 0, 0, 1, 2, 3, 0] --> result: [1, 2, 3, 0, 0, 0, 0]
