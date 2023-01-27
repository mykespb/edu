#!/usr/bin/env python3
# ls-ispower2.py
# (C) Mikhail Kolodin, 2023
# 2023-01-27 2023-01-27 1.1
# LeetCode problem

# Степень двойки (https://leetcode.com/problems/power-of-two)
# Сложность: Лёгкая
# Условие задачи: даётся целое число n, необходимо проверить, является ли число степенью двойки или же нет.  
# Пример:
# Ввод: n = 1
# Вывод: true

def check(n: int) -> bool:
    if n <= 0:
        return False
    if n < 3:
        return True
    if n % 2 == 1:
        return False
    return check(n//2)

# tests

print(1, check(1))
print(2, check(2))
print(3, check(3))
print(4, check(4))
print(100, check(100))
print(128, check(128))
print(0, check(0))
print(-1, check(-1))
print(-2, check(-2))
