#!/usr/bin/env python

# list-comp-ex.py
# examples for lists comprehensions
# Mikhail (myke) Kolodin, 2024
# 2024-10-06 2024-10-06 0.1

import random
from pprint import pp

# ~ # task
# ~ stroka = "We are not afraid today"

# ~ # solution
# ~ lst = [len(word) for word in stroka.split() if word]

# ~ print(f"lengths for <{stroka}> are {lst}")

# ~ # task
# ~ # multiplication table

# ~ # solution

# ~ mt = [[ i * j for j in range(1, 10) ] for i in range(1, 10) ]

# ~ pp(mt)

# task
# relation between row number and column number

# solution

# ~ rel = [[ i / j for j in range(1, 10) ] for i in range(1, 10) ]
# ~ pp(rel)

# ~ for i in range(1, 10):
    # ~ for j in range(1, 10):
        # ~ print("%10.5f" % rel[i-1][j-1], end="")
    # ~ print()

   # ~ 1.00000   0.50000   0.33333   0.25000   0.20000   0.16667   0.14286   0.12500   0.11111
   # ~ 2.00000   1.00000   0.66667   0.50000   0.40000   0.33333   0.28571   0.25000   0.22222
   # ~ 3.00000   1.50000   1.00000   0.75000   0.60000   0.50000   0.42857   0.37500   0.33333
   # ~ 4.00000   2.00000   1.33333   1.00000   0.80000   0.66667   0.57143   0.50000   0.44444
   # ~ 5.00000   2.50000   1.66667   1.25000   1.00000   0.83333   0.71429   0.62500   0.55556
   # ~ 6.00000   3.00000   2.00000   1.50000   1.20000   1.00000   0.85714   0.75000   0.66667
   # ~ 7.00000   3.50000   2.33333   1.75000   1.40000   1.16667   1.00000   0.87500   0.77778
   # ~ 8.00000   4.00000   2.66667   2.00000   1.60000   1.33333   1.14286   1.00000   0.88889
   # ~ 9.00000   4.50000   3.00000   2.25000   1.80000   1.50000   1.28571   1.12500   1.00000

# task для каждого числа в списке получить количество чисел в том же списке, которые меньше его

# solution

# ~ lst = [random.randint(-99, 99) for _ in range(10)]
# ~ print(f"{lst=}")

# ~ less = [ len( [el for el in lst if el < v ] ) for v in lst ]
# ~ print(f"{less=}")

# ~ lst=[-34, 64, 80, -29, -45, -49, 57, 45, 15, 39]
# ~ less=[2, 8, 9, 3, 1, 0, 7, 6, 4, 5]

# task получить все возможные числа из цифр 3, 5, 7

# solution

digs = 3, 5, 7

comb = [ i*100+j*10+k for i in digs for j in digs for k in digs ]
print(comb)

# [333, 335, 337, 353, 355, 357, 373, 375, 377, 533, 535, 537, 553, 555, 557, 573, 575, 577, 733, 735, 737, 753, 755, 757, 773, 775, 777]
