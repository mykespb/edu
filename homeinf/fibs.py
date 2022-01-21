#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2022-01-21 2022-01-21 0.1
# fibs.py
# ~ числа Фибоначчи, просто

def fib(n=10):
    """печатаем n чисел"""

    if n < 1:
        print(f"неправильные данные: не бывает ({n}) чисел!")
        return

    print(1, end=" ")

    if n == 1:
        return

    f1 = 0
    f2 = 1

    for i in range(n-1):
        f3 = f1 + f2
        print(f3, end=" ")
        f1, f2 = f2, f3

    print()

fib()
fib(100)
fib(0)
