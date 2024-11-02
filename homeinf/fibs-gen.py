#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2024-11-02 2024-11-02 1.0
# fibs-gen.py
# ~ числа Фибоначчи, генераторы

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

# ~ fib()
# ~ fib(100)
# ~ fib(0)

def fingen(n=10):
    """выдаём n чисел"""

    f1, f2 = 0, 1
    
    for i in range(n):
        f1, f2 = f2, f1 + f2
        yield f2


def fingen_test(n):
    for i in fingen(n):
        print(i, end=", ")
    print()

fingen_test(5)

