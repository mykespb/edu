#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2026-04-19 2026-04-19 2.0
# eo-line.py

# ~ "even-odd in line"

# ~ Дан случайный недлинный список целых.
# ~ Выдать список такой же длины,
# ~ в котором каждое число заменено
# ~ на 0, если сумма его соседей в исходном списке чётная
# ~ (соседей считаем по кругу),
# ~ и на 1, если она нечётна.

from random import randint


def make() -> list:
    """make array to count"""

    return [ randint(1, 99) for _ in range(10) ]


def main1(arr) -> list:
    """remake with evens and odds count"""

    lng = len(arr)

    out = [ 0 for _ in range(lng)]

    for i in range(lng):
        if (arr[ (i-1) % lng] + arr[ (i+1) % lng ]) % 2:
            out[i] = 1

    return out


def main2(arr) -> list:
    """remake with evens and odds count"""

    lng = len(arr)

    out = [ 0 for _ in range(lng)]

    for i in range(lng):
        out[i] = (arr[ (i-1) % lng] + arr[ (i+1) % lng ]) % 2

    return out


def main3(arr) -> list:
    """remake with evens and odds count"""

    lng = len(arr)

    out = []

    for i in range(lng):
        out.append( (arr[ (i-1) % lng] + arr[ (i+1) % lng ]) % 2 )

    return out


arr = make()
print(arr)

out = main1(arr)
print(out)

out = main2(arr)
print(out)

out = main3(arr)
print(out)
