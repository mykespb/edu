#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2024-11-02 2024-11-02 2.1
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

# ~ -----------------------------------
# ~ реализация на генераторах
# ~ -----------------------------------

def fibgen(n=10):
    """выдаём n чисел"""

    yield 1
    yield 1

    f1, f2 = 1, 1
    
    for i in range(n-2):
        f1, f2 = f2, f1 + f2
        yield f2


def fibgen_test(n):
    for i in fibgen(n):
        print(i, end=", ")
    print()

fibgen_test(15)

# ~ -----------------------------------
# ~ реализация на генераторах - трибоначи
# ~ -----------------------------------

def tribgen(n=10):
    """выдаём n чисел"""

    yield 1
    yield 1
    yield 1

    t1, t2, t3 = 1, 1, 1
    
    for i in range(n-3):
        t1, t2, t3 = t2, t3, t1 + t2 +t3
        yield t3


def tribgen_test(n=10):
    for i in tribgen(n):
        print(i, end=", ")
    print()

tribgen_test(15)

# ----------------------------------
