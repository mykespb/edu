#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# max-square-odd.py 2025-08-11 2025-08-11 1.0

# ~ В случайном списке целых чисел найти максимальный квадрат числа из тех, что стоят на нечётных позициях (с 0)

import random

lst = [ random.randint(-100, 100) for _ in range(10) ]
print(lst)

def main():

    print( max( [ x*x for x in [ lst[n] for n in range(len(lst)) if n % 2 ] ] ) )

main()

# ~ [99, -99, -9, 64, -9, -26, 3, 84, 63, -48]
# ~ 9801
