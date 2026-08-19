#!/usr/bin/env python
# Miklhail (myke) Kolodin
# math / fact-zeros.py
# 2026-07-21 2026-08-18 1.2
# сколькими нулями заканчивается n! ?

def zeros(n):
    """сколько нулей?"""

    if n < 5:
        return 0

    z = 0
    for i in range(5, n+1):
        n = i
        while n % 5 == 0:
            n //= 5
            z += 1

    return z


def test(n):
    """1 тест"""

    print(f"{n:4}! заканчивается {zeros(n):_} нулями")


def tests():
    """много тестов"""

    nabor = 1, 2, 5, 6, 10, 15, 16, 20, 24, 25, 50, 100, 101, 124, 125, 200, 1000, 1_000_000, 10_000_000

    for n in nabor:
        test(n)


tests()
