#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-04-08 2025-04-08 0.1
# same-temps.py

# ~ Сошлась погода

# ~ В первый день месяца в Москве было тепло, а в Питере холодно.
# ~ На протяжении нескольких дней в Москве холодало, а в Питере теплело.
# ~ Определить день, когда в Москве и Питере температуры были максимально близки.

from random import random

def make():
    global msk, spb

    TMIN_MSK = 0. 
    TMAX_MSK = 25.
    TMIN_SPB = 10.
    TMAX_SPB = 20.
    VAR      = 1.
    DAYS     = 10

    msk = [ TMAX_MSK + random() * VAR - (TMAX_MSK - TMIN_MSK) * d / DAYS for d in range(DAYS)]
    spb = [ TMIN_SPB + random() * VAR + (TMAX_SPB - TMIN_SPB) * d / DAYS for d in range(DAYS)]
    
    print("\nmsk:", end=" ")
    for e in msk:
        print(f"{e:05.2f}", end=", ")

    print("\nspb:", end=" ")
    for e in spb:
        print(f"{e:05.2f}", end=", ")

    print('\n\n')

def solve():
    global msk, spb

    


def main():
    make()
    solve()


main()
