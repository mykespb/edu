#!/usr/bin/env python
# Miklhail (myke) Kolodin
# math / fact-zeros.py
# 2026-07-21 2026-07-21 1.1
# сколькими нулями заканчивается n! ?

def zeros(n):
    """сколько нулей?"""

    if n < 5:
        return 0

    z = 0
    for i in range(5, n+1):
        while i % 5 == 0:
            i //= 5
            z += 1

    return z


def test(n):
    """1 тест"""

    print(f"{n:4}! заканчивается {zeros(n):4} нулями")


def tests():
    """много тестов"""

    nabor = 1, 2, 5, 10, 15, 16, 20, 25, 50, 100, 101, 200, 1000

    for n in nabor:
        test(n)


tests()
