#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-26 2024-12-26 1.0
# best-flat.py

# ~ а. создаётся случайный список квартир
# ~ б. надо найти самую случайную :)
# ~ в. надо найти самую дешевую
# ~ г. самую большу по площади
# ~ д. оптимальную (по отношению площадь / цена, т.е. стоимость кв. метра)
# ~ (если вообще есть из чего выбирать :) )

# from pprint import pp
from random import randint

# площадь квартиры, м^2
SIZE_FROM = 25
SIZE_TO = 250

# цена квартиры, тыс. руб.
PRICE_FROM = 1_000
PRICE_TO = 30_000


def generate(limit: int = 100) -> list:
    """создать набор квартир,
    общим число до limit
    """

    assert 1 <= limit <= 1_000_000

    table = []

    for i in range(1, limit + 1):
        table.append(
            dict(
                number=i,
                size=randint(SIZE_FROM, SIZE_TO),
                price=randint(PRICE_FROM, PRICE_TO),
            )
        )

    return table


def find_best(table: list, reason: str) -> list:
    """найти лучшую квартиру по некоторому критерию"""

    methods = {
        "random": lambda x: randint(0, 1000),
        "size": lambda x: x["size"],
        "price": lambda x: -x["price"],
        "optimal": lambda x: x["size"] / x["price"],
    }

    return sorted(table, key=methods[reason], reverse=True)[0]


def main() -> None:
    """диспетчер"""

    flats = generate()
    # ~ flats = generate(1_000)
    # ~ flats = generate(1_000_000)
    # ~ pp(flats)

    print(f"best random flat:  {find_best(flats, 'random')}")
    print(f"best sized flat:   {find_best(flats, 'size')}")
    print(f"best priced flat:  {find_best(flats, 'price')}")
    print(f"best optimal flat: {find_best(flats, 'optimal')}")


main()
