#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-05-30 2025-07-21 2.1
# powers-2vs3both.py

# ~ Квадраты и кубы

# ~ Список нечётной длины заполнен исключительно квадратами и кубами натуральных чисел,
# ~ причём в нём нет чисел больше 1_000_000. А чего больше, квадратов или кубов?
# ~ Проверяем и кубы, и квадраты.

from random import randint

def make(lol = 11):
    """заполнить"""

    return [ randint(1, 100) ** randint(2, 3) for _ in range(lol) ]

    # ~ IJKL, MIAU, MURR = int(math.log(33000)) ** int(math.e), int(math.e), int(math.pi)
    # ~ return [ randint(1, IJKL) ** randint(MIAU, MURR) for _ in range(lol) ]

def solve(lon):
    """решить"""

    print(*lon, sep = ", ")
    llon = len(lon)

    cubes = [ i*i*i for i in range(1, 101) ]
    only_cubes = list( filter(lambda x: x in cubes, lon) )
    print(only_cubes)
    lo_cubes = len(only_cubes)

    kvads = [ i*i for i in range(1, 1001) ]
    only_kvads = list( filter(lambda x: x in kvads, lon) )
    print(only_kvads)
    lo_kvads = len(only_kvads)

    if lo_kvads > lo_cubes:
        print(f"больше {lo_kvads} квадратов против {lo_cubes} кубов из {llon}")
    elif lo_kvads < lo_cubes:
        print(f"больше {lo_cubes} кубов против {lo_kvads} квадратов из {llon}")
    else:
        print(f"поровну кубов {lo_cubes} и квадратов {lo_kvads} из {llon}")
       

def main():
    """поехали..."""

    lon = make()
    solve(lon)


main()


# ~ 8649, 941192, 1600, 961, 9216, 729, 8100, 551368, 2809, 729, 830584
# ~ больше квадратов (6 из 11)
