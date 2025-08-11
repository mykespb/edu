#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# nums-by-3.py 2025-07-24 2025-07-28 1.3

# ~ В случайном списке натуральных чисел найти самое большое число, которое состоит из нечётного количества цифр и делится на 3.

import random

lst = [ random.randint(1, 100_500) for _ in range(100)]
print(lst)

def check(n):

    return (n % 3 == 0) and ( len(str(n)) % 2 == 1)


def main():

    print("ответ:", max(
        [ n for n in lst if check(n) ]
        ))


main()
