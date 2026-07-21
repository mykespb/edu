#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-08-16 2025-08-18 1.2

# ~ grow-nums.py

# ~ Растущие числа
# ~ ------------------------------------

# ~ Назовём натуральное число растущим, если в его записи каждая последующая цифра
# ~ строго больше предыдущей.

# ~ Дан список натуральных чисел.
# ~ Найти в нём растущие числа и показать их в порядке возрастания суммы их цифр,
# ~ либо указать, что таких чисел нет.

# ~ Напр., для 123, 11, 22, 564, 956, 235
# ~ ответ:  123, 235

# ~ grow-nums.py
  
import random

lst = [ random.randint(1, 1000) for _ in range(10) ]
print("source list:", lst)


def is_grow(x):
    """check if number x is growing"""

    seq = str(x)

    for i in range(len(seq) - 1):
        if seq[i] >= seq[i+1]:
            return False

    return True


def sum_dig(x):
    """calculate sum of digits"""

    return sum (map (int, (str(x)) ))
    

def main():
    """solve all"""

    good =  [ x for x in lst if is_grow(x) ]

    if good:
        good.sort(key = sum_dig)
        print("grow list:", good)
    else:
        print("no grow nums")

main()


# results:

# ~ source ist: [778, 463, 454, 399, 867, 688, 693, 907, 987, 271]
# ~ no grow nums

# ~ source ist: [682, 988, 837, 977, 384, 829, 605, 908, 761, 34]
# ~ grow list: [34]

# ~ source ist: [488, 954, 28, 802, 611, 409, 56, 169, 279, 750]
# ~ grow list: [28, 56, 169, 279]
