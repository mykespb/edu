#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-05-03 2022-05-03 1.0
# bestsq.py

# ~ Есть квадрат 10х10, заполненный числами  от 0 до 9.
# ~ Найти подквадрат 2х2 с максимальной суммой
# ~ (если несколько, то любой).

# генерация случайного квадрата

from random import randint as ri
from pprint import pp

# поиск

def summa(q, i, j):
    """найти сумму в миниквдрате с верхней левой координатой i, j"""

    return q [i][j] + q [i][j+1] + q [i+1][j] + q [i+1][j+1]


def best(q):
    """обработать весь квадрат"""

    bs = bi = bj = -1    # лучшая сумма и её координаты

    for i in range(9):
        for j in range(9):
            if (s := summa(q, i, j)) > bs:
                bs = s
                bi = i
                bj = j

    return bs, bi, bj

# запуск тестов

def test(raz=1):
    """тестируем raz"""

    for r in range(raz):
        print(f"\n-------------- {r+1} раз -------------------\n")
        q = [[ri(0, 9) for i in range(10)] for j in range(10)]
        pp(q)
        bs, bi, bj = best(q)
        print(f"\nлучшая сумма {bs} в квадрате с вершиной {bi} и {bj}")


test()


# ~ пример работы

# ~ -------------- 1 раз -------------------

# ~ [[3, 4, 1, 2, 2, 6, 3, 1, 7, 7],
 # ~ [9, 4, 5, 2, 7, 1, 1, 0, 0, 5],
 # ~ [6, 4, 7, 2, 5, 6, 2, 1, 9, 3],
 # ~ [5, 4, 6, 8, 0, 4, 1, 8, 6, 9],
 # ~ [9, 7, 3, 4, 1, 2, 8, 1, 2, 8],
 # ~ [6, 7, 4, 5, 7, 5, 8, 3, 3, 6],
 # ~ [0, 8, 4, 1, 5, 3, 4, 4, 1, 0],
 # ~ [8, 3, 1, 2, 9, 5, 0, 1, 0, 3],
 # ~ [0, 7, 3, 0, 2, 5, 8, 2, 6, 7],
 # ~ [1, 2, 7, 2, 3, 2, 4, 6, 8, 4]]

# ~ лучшая сумма 29 в квадрате с вершиной 4 и 0