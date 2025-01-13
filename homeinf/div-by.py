#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2025-01-03 2025-01-13 1.2
# div-by.py

# ~ Какое из произведений натуральных чисел до 100 больше -
# ~ тех, которые делятся нацело на 3, или тех, которые на 4?

def make_seq(limit = 10):
    """сделать ряд для обработки"""

    return [ i for i in range(1, limit+1) ]


def divby(limit = 10, num = 1):
    """сделать ряд для обработки:
    натуральные числа до limit включительно, которые делятся на num"""

    # ~ return [ i for i in range(1, limit+1) if i % num == 0]
    return [ i for i in range(1, limit+1, num) ]


def prod(seq):
    """вычислить произведение"""

    res = 1
    for e in seq:
        res *= e
    return res


def main(till = 10):
    """посчитать до  till"""

    row3 = divby(till, 3)
    row4 = divby(till, 4)

    print(f"{row3=}, {row4=}")

    prod3 = prod(row3)
    prod4 = prod(row4)

    print(f"{prod3=}, {prod4=}")
    
    if prod3 > prod4:
        print("произведение для 3 больше")
    elif prod3 < prod4:
        print("произведение для 4 больше")
    else:
        print("произведения равны")


main(10)


# ~ row3=[1, 4, 7, 10], row4=[1, 5, 9]
# ~ prod3=280, prod4=45
# ~ произведение для 3 больше
