#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-05-30 2025-05-30 1.0
# powers-2vs3.py

# ~ Квадраты и кубы

# ~ Список нечётной длины заполнен исключительно квадратами и кубами,
# ~ причём нет чисел больше 1_000_000. А чего больше?

from random import randint

def make(lol = 11):
    """заполнить"""

    return [ randint(1, 100) ** randint(2, 3) for _ in range(lol) ]


def solve(lon):
    """решить"""

    print(*lon, sep = ", ")
    llon = len(lon)

    cubes = [ i*i*i for i in range(1, 100) ]

    only_cubes = list( filter(lambda x: x in cubes, lon) )
    # ~ print(only_cubes)
    loc = len(only_cubes)

    if loc <= llon // 2:
        print(f"больше квадратов ({llon - loc} из {llon})")
    else:
        print(f"больше кубов ({loc} из {llon})")
       


def main():
    """поехали..."""

    lon = make()
    solve(lon)


main()


# ~ 8649, 941192, 1600, 961, 9216, 729, 8100, 551368, 2809, 729, 830584
# ~ больше квадратов (6 из 11)
