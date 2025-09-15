#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-08-19 2025-09-15 1.2
# many-zeros.py

# ~ Больше нулей
# ~ -----------------------------------------

# ~ В случайном списке натуральных чисел найти те, в записи которых больше всего нулей.

# ~ Если их несколько, то
# ~ (а) показать одно любое,
# ~ (б) показать все, списком, в любом порядке.
# ~ Если их нет, явно об этом сказать.


import random

# нормальный тест
lst = [ random.randint(1, 1_000_000) for _ in range(10) ]

# пустой тест: нет данных
#lst = []

# тест с данными, но без нулей
#lst = [1, 2, 4, 8]

print("числа:", lst)


def count_zeros(e):

    nz = str(e).count('0')
    return (nz, e)
    

def main():

    if not lst:
        print("no data")
        return
        
    reorder = sorted(map(count_zeros, lst), reverse=True)
    how_many = reorder[0][0]

    if how_many:
        print("максимум нулей:", how_many)
        print("одно:", reorder[0][1])
        print("все:", *[e[1] for e in reorder if e[0]==how_many], sep=", ")

    else:
        print("no zeros")


main()


# ~ числа: [772279, 725039, 592353, 521347, 5376, 455235, 335460, 674640, 444234, 698074]
# ~ максимум нулей: 1
# ~ одно: 725039
# ~ все:, 725039, 698074, 674640, 335460
