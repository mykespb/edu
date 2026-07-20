#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# nums-by-3.py 2025-08-11 2025-08-11 2.2

# ~ В случайном списке натуральных чисел найти самое большое число, которое состоит из нечётного количества цифр и делится на 3.

import random

lst = [ random.randint(1, 100_500) for _ in range(10)]
print(lst)

def main():

    good = [ n for n in lst if n % 3 == 0 and len(str(n)) % 2 ]
    print("ответ:", max(good) if good else "нет таких чисел")

main()
