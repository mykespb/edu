#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-04-15 2025-04-15 0.1
# study-means.py

# ~ Проверить практически на примерах, что среднее квадратическое
# ~ всегда больше, чем среднее арифметическое.

from math import sqrt
from random import random

def make(leng=10, val=100.):
    """создать последовательность"""

    return [ random() * val for _ in range(leng)]


def s_arithm(seq):
    """вычисляем среднее арифметическое"""

    return sum(seq) / len(seq)


def s_sqaure(seq):
    """вычисляем среднее арифметическое"""

    summa = 0.
    for i in range(len(seq)):
        summa += seq[i] ** 2 / len(seq)
    return sqrt(summa)


def test():
    """выполнить 1 тест"""

    seq = make()
    sa  = s_arithm(seq)
    sk  = s_sqaure(seq)

    print(f"{seq=} : {sa=}, {sk=} => { 'yes :)' if sa <= sk else 'no :('}")


def tests(num=1):
    """выполнить много тестов (1)"""

    for i in range(num):
        test()

tests(10)
