#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-03-17 2022-03-17 1.1
# arr-2-sum.py

# ~ Дан список с упорядоченныи целыми числами и ещё одно целое число.
# ~ Найти пару чисел в списке, сумма которых равна этому числу,
# ~ либо сказать, что таких чисел нет;
# ~ если решений несколько, показать одно любое.

# ~ В нашем случае надо воспользоваться доп. функцией give_me_task(),
# ~ которая сгенерирует случайное задание.

# --------------- готовим -----------------

from random import randint, shuffle

def give_me_task(diap=10, lmin=5, lmax=15):
    """
    создать задание.
    diap: целые числа д.б. в диапазоне от -diap .. +diap,
    lmin: minimal length of list,
    lmax: maximal length of list
    """

    arr = [randint(-diap, diap) for _ in range(randint(lmin, lmax))]
    num = sum(arr[:2])
    shuffle(arr)
    arr.sort()

    if not randint(0, 9):
        num += 1

    return arr, num

def tests(times=5):
    """
    протестировать создание списка
    """

    for i in range(times):
        print(give_me_task())

# ~ tests()

# --------------- решаем -----------------

def ver1():
    """попытка 1"""

    arr, num = give_me_task()
    print("список:", arr, ", число:", num)

    for i in range(len(arr)):
        if (num - arr[i]) in (arr[:i] + arr[i+1:]):
            print("решение: ", arr[i], ", ", num-arr[i])
            break
    else:
        print("нет решений")

ver1()
