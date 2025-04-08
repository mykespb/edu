#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-04-08 2025-04-08 1.1
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
    VAR      = 3.
    DAYS     = 15

    msk = [ TMAX_MSK + random() * VAR - (TMAX_MSK - TMIN_MSK) * d / DAYS for d in range(DAYS)]
    spb = [ TMIN_SPB + random() * VAR + (TMAX_SPB - TMIN_SPB) * d / DAYS for d in range(DAYS)]
    
    print("\nmsk:", end=" ")
    for e in msk:
        print(f"{e:05.2f}", end=", ")

    print("\nspb:", end=" ")
    for e in spb:
        print(f"{e:05.2f}", end=", ")

    print('\n')

def solve():
    global msk, spb

    min_diff = 1e10

    for i in range(len(msk)):
        in_msk = msk[i]
        in_spb = spb[i]
        diff = abs( in_msk - in_spb)
        if diff < min_diff:
            min_diff = diff
            day = i
            best_msk = in_msk
            best_spb = in_spb

    print(f"ближайшие температуры были в {day} день:\nв Москве {best_msk}, а в Питере {best_spb},\nразница составила {abs(best_msk - best_spb)} градусов.\n")


def main():
    make()
    solve()


main()


# ~ msk: 26.07, 25.48, 21.93, 21.30, 20.08, 17.96, 17.32, 15.85, 13.10, 12.78, 08.62, 08.91, 06.53, 04.60, 04.20, 
# ~ spb: 11.73, 12.80, 13.50, 13.71, 14.66, 14.62, 16.97, 16.78, 15.59, 18.92, 17.90, 18.48, 20.92, 19.48, 20.10, 

# ~ ближайшие температуры были в 6 день:
# ~ в Москве 17.32103934215391, а в Питере 16.965328807245854,
# ~ разница составила 0.3557105349080558 градусов.
