#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2025-01-07 2025-01-07 1.0
# linked.py

# ~ Города и дороги между ними образуют ненагруженный ненаправленный граф.
# ~ Есть набор дорог между городами.
# ~ Определить связность графа страны.

roads1 = """
СПб - Москва
Москва - Нижний
Нижний - Омск
Омск - Новосибирск
СПб - Выборг
Москва - Тверь
"""

roads2 = """
СПб - Москва
Москва - Нижний
Нижний - Омск
Омск - Новосибирск
СПб - Выборг
Москва - Тверь
Самара - Саратов
"""



def linked() -> bool:
    """определить связность карты-графа"""

    global passed, roads, cities, loc, mapa

    passed = set()

    # подготовка данных

    roads = []
    cities = set()

    for line in mapa.strip().split("\n"):
        # ~ print(f"{line=}")
        cfrom, _, cto = line.strip().split(" ")
        # ~ print(f"{cfrom=}, {cto=}")

        roads.append((cfrom, cto))
        roads.append((cto, cfrom))
        cities.add(cfrom)
        cities.add(cto)

    loc = sorted(cities)

    # ~ print(f"\n--------------------\n{roads=}\n{cities=}\n{loc=}")

    # решение

    plus(loc[0])

    return passed == cities


def plus(city):
    """добавить город и все за ним, рекурсивно"""

    global passed, roads, cities, loc, mapa

    passed.add(city)

    for nextone in [ place[1] for place in roads
        if place[0] == city and place[1] not in passed
        ] :
        plus(nextone)


def test_map() -> None:
    """оформить связность карты-графа"""

    print("\n---------------------------\nкарта:\n",
        mapa,
        "\nСвязность:", linked(), "\n" )


def main():
    """всё запустить"""

    global passed, roads, cities, loc, mapa

    mapa = roads1
    test_map()
    mapa = roads2
    test_map()


main()
