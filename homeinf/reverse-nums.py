#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-08-18 2025-08-18 1.0
# reverse-nums.py

# ~ Поэлементный переворот
# ~ -----------------------------------------

# ~ В случайном списке натуральных чисел перевернуть все числа,
# ~ т.е. записать их в обратном порядке.
# ~ (Нули можно оставить)

import random

lst = [ random.randint(1, 1000) for _ in range(10) ]
print("source numbers:  ", lst)


def main():

    print("reversed numbers:", [ int(str(x)[::-1]) for x in lst ] )


main()
