#!/usr/bin/env python

# possible-sum.py
# (C) Mikhail (myke) Kolodin, 2024
# 2024-12-16 2024-12-16 1.0

# Дан набор натуральных чисел и ещё одно натуральное число - требуемая сумма.
# Определить, можно ли, расставив знаки + или - перед числами из набора, получить заданную сумму.

LOW    = 1     # нижнее число
HIGH   = 9     # верхнее число
MANY   = 4     # сколько взять чисел

from random import randint

def solve(row, want):
    """решатель"""

    for it in range(2**MANY):

        bn = f"{it:0{MANY}b}"
        bl = list( map(int, bn))
        bm = list( map( lambda x: 1 if x else -1, bl))
        # print(f"{bn=}, {bl=}, {bm=}")

        prep = [row[i] * bm[i] for i in range(MANY)]
        calc = sum(prep)
        # print(f"{prep=}, {calc=}")
        
        if calc == want:
            return True, prep
        
    return False, []

    
def main(times=1):
    """организатор,
    запуск times раз"""
    
    for rept in range(1, times+1):
    
        row  = [ randint(LOW, HIGH) for _ in range(MANY)]
        want = randint(1, sum(row)) 

        print(f"\nПопытка {rept}.\nВзяли числа {row} и хотим получить сумму {want}.")
        
        res, resp = solve(row, want)
        if res:
            print("Получилось: сумма", resp, "равна", want)
        else:
            print("Не получилось.")
    
main(5)

# Попытка 1.
# Взяли числа [9, 1, 9, 3] и хотим получить сумму 3.
# Не получилось.

# Попытка 2.
# Взяли числа [2, 1, 1, 5] и хотим получить сумму 5.
# Получилось: сумма [-2, 1, 1, 5] равна 5

# Попытка 3.
# Взяли числа [3, 6, 2, 5] и хотим получить сумму 8.
# Не получилось.

# Попытка 4.
# Взяли числа [1, 9, 3, 6] и хотим получить сумму 2.
# Не получилось.

# Попытка 5.
# Взяли числа [6, 5, 2, 5] и хотим получить сумму 2.
# Получилось: сумма [-6, 5, -2, 5] равна 2
