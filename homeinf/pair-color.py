#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-01-18 2025-01-18 1.0
# pair-color.py

# ~ Собрать детей по парам.
# ~ --------------------------------------

# ~ Даны пары вида 
# ~ Ребенок - цвет костюма.
# ~ Всегда есть по паре детей каждого цвета.
# ~ Собрать детей по парам.

# ---------------------------------------------
# исходные данные

deti = """
Bob green
Mary yellow
Mike blue
Jane white
Jim yellow
Tom white
Lara green
Toma blue
"""

# ---------------------------------------------
# импорты и установки

from collections import defaultdict

# ---------------------------------------------
# программа

def gather():
    """собрать одноцветных"""

    children = deti.strip().splitlines()
    # ~ print(children)

    children = [ child.strip().split() for child in children ]
    # ~ print(children)

    pairs = defaultdict(list)

    for who, color in children:
        pairs[color].append(who)
    # ~ print(f"{pairs=}")

    for color, who in pairs.items():
        print(f"цвет: {color}, дети: ", end="")
        print(*who, sep=", ")

# ---------------------------------------------
# тестирование

gather()

# ---------------------------------------------
# результаты

# ~ цвет: green, дети: Bob, Lara
# ~ цвет: yellow, дети: Mary, Jim
# ~ цвет: blue, дети: Mike, Toma
# ~ цвет: white, дети: Jane, Tom

# ---------------------------------------------
