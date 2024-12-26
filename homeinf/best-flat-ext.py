#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-26 2024-12-26 2.3
# best-flat-ext.py

# ~ а. создаётся случайный список квартир
# ~ после этого, только среди продающихся
# ~ б. надо найти самую случайную :)
# ~ в. надо найти самую дешевую
# ~ г. самую большу по площади
# ~ д. оптимальную (по отношению площадь / цена, т.е. стоимость кв. метра)
# ~ (если вообще есть из чего выбирать :) )

from pprint import pp
from random import choice, randint

# площадь квартиры, м^2
SIZE_FROM = 25
SIZE_TO   = 250

# цена квартиры, тыс. руб.
PRICE_FROM = 1_000
PRICE_TO   = 30_000

# вероятность того, что квартира продаётся
SELL_PROB = 75


def generate(limit : int = 100) -> list:
    """создать набор квартир,
    общим число до limit
    """

    assert 1 <= limit <= 1_000_000, "Number of flats should be between 1 and 1_000_000."
    
    table = []

    for i in range(1, limit+1):
        table.append( dict(
            number = i,
            size   = randint(SIZE_FROM, SIZE_TO),
            price  = randint(PRICE_FROM, PRICE_TO),
            listed = randint(0, 100) <= SELL_PROB,
            ))

    return table


def find_best(table : list, reason : str) -> list:
    """найти лучшую квартиру по некоторому критерию
    ("random", "size", "price", "optimal")
    """

    sell = list(filter(lambda x: x['listed'], table))
    
    if not sell:
        return {'error': 'no flats being sold'}

    if len(sell) == 1:
        return sell[0]

    methods = {
        "random":  lambda x: randint(0, 1000),
        "size":    lambda x: x['size'],
        "price":   lambda x: -x['price'],
        "optimal": lambda x: x['size'] / x['price'],
        }

    return sorted(
        sell,
        key = methods[reason],
        reverse = True) [0]


def main() -> None:
    """диспетчер
    """

    flats = generate()
    # ~ flats = generate(-1)
    # ~ flats = generate(1_000)
    # ~ flats = generate(1_000_000)
    # ~ pp(flats)

    print(f"best random flat:  {find_best(flats, 'random')}")
    print(f"best sized flat:   {find_best(flats, 'size')}")
    print(f"best priced flat:  {find_best(flats, 'price')}")
    print(f"best optimal flat: {find_best(flats, 'optimal')}")


main()


# ~ best random flat:  {'number': 99, 'size': 123, 'price': 9956, 'listed': True}
# ~ best sized flat:   {'number': 14, 'size': 250, 'price': 26331, 'listed': True}
# ~ best priced flat:  {'number': 7, 'size': 129, 'price': 1804, 'listed': True}
# ~ best optimal flat: {'number': 93, 'size': 206, 'price': 2789, 'listed': True}

# ~ best random flat:  {'error': 'no flats being sold'}
# ~ best sized flat:   {'error': 'no flats being sold'}
# ~ best priced flat:  {'error': 'no flats being sold'}
# ~ best optimal flat: {'error': 'no flats being sold'}
