#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-26 2024-12-26 1.0
# best-flat.py

# ~ а. создаётся случайный список квартир
# ~ б. надо найти из продающихся самую дешевую
# ~ в. самую большу по площади
# ~ г. оптимальную
# ~ (если вообще есть из чего выбирать :) )

from pprint import pp
from random import choice, randint

# площадь квартиры, м^2
SIZE_FROM = 25
SIZE_TO   = 250

# цена квартиры, тыс. руб.
PRICE_FROM = 1_000
PRICE_TO   = 30_000


def generate(limit : int = 100) -> list:
    """создать набор квартир,
    общим число до limit
    """

    table = []

    for i in range(1, limit+1):
        table.append( dict(number = i,
            size  = randint(SIZE_FROM, SIZE_TO),
            price = randint(PRICE_FROM, PRICE_TO) ))

    return table


def find_best(table : list, reason : str) -> list:
    """найти лучшую квартиру по некоторому критерию
    """

    return []


def main() -> None:
    """диспетчер
    """

    flats = generate()
    pp(flats)


main()
