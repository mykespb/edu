#!/usr/bin/env python3.9

# div1016.py
# 2021-08-17 2021-08-17 1.6
# (C) Mikhail (myke) Kolodin

# задание из ЕГЭ:
# найти числа из диапазона [1016; 7937],
# которые делятся на 3
# и не делятся на 7, 17, 19, 27.
# найти количество их и макс из них.
# ответ: 2 эти целых числа

# ----------------------------------------- 1

# variant 1
# считаем, что данные переданы корректно
# (в условии не сказано, что может быть иначе),
# иначе нужно проверять, что даипазон задан и задан правильно
# (там только натуральные числа и второе больше первого),
# что списки делителей и неделителей заданы и там нет ни одного нуля.

# обобщённая функция: передаём ей как списки
# - диапазон для перебора (как сказано в задаче, границы включительно),
# - набор делителей, на которые требуемые числа должны делиться,
# - набор "неделителей", на которые не должны.
# выдаётся кортеж из 2 требуемых чисел
# либо (0, 0) при неудаче

print("вариант 1")

def howmany(scope=None, divs=None, nodivs=None):
    """ найти числа """

    if scope  == None:
        scope  = [1016, 7937+1]
    else:
        scope[1] += 1
    if divs   == None:
        divs   = [3]
    if nodivs == None:
        nodivs = [7, 17, 19, 27]

    # ~ print(f"{scope=}, {divs=}, {nodivs=}")

    res = []

    for n in range(*scope):
        if any([n % x for x in divs]):
            continue
        if any([n % x == 0 for x in nodivs]):
            continue
        res.append(n)

    if res:
        return len(res), max(res)
    else:
        return 0, 0

# ~ print(*howmany([1, 15], [3], [5]))
print(*howmany())

# ----------------------------------------- 2

# variant 2
# простое построение списка через генератор и печать результата

print("вариант 2")

nums = [i for i in range(1016, 7937+1) if i%3==0 and i%7 and i%17 and i%19 and i%27]
print(len(nums), max(nums))

# ----------------------------------------- 2a

# variant 2a
# однострочник

print("вариант 2a")

print(len(nums := [i for i in range(1016, 7937+1) if i%3==0 and i%7 and i%17 and i%19 and i%27]), max(nums))

# ----------------------------------------- вывод

# ~ вариант 1
# ~ 1568 7935
# ~ вариант 2
# ~ 1568 7935
# ~ вариант 2a
# ~ 1568 7935