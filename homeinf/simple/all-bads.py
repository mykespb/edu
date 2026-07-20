#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2026-03-22 2026-03-22 1.0
# all-bads.py
# Плохие идеи для питона

# ~ --- sum ---

# ~ def sum():
    # ~ s = 1+   2 +3+   4 +5 + 9+8  +7  +6
    # ~ return s

# ~ ps = sum(); print(ps)


# ~ - использование имени станд. функции, имя теперь в программе недоступно
# ~ - неравномерная запись выражения
# ~ - выражение лучше записывать по порядку, напр., по возрастанию, иначе легко что-нибудь пропустить
# ~ - можно сократить
# ~ - диапазон можно передать как парамитр, иначе функция может применяться только для одного вычисления
# ~ - то, что мы узнали о возможности записи нескольких команд в 1 строку, не значит, что так и надо поступать;
# ~ обычно пишут по общим правилам
# ~ - полезно делать описание функции в строке документирования
# ~ - print(sum(range(10)))


# ~ --- подсчёт нужных чисел в списке ---

from random import randint

# ~ заполнить списорк
lst = []
for i in range(100):
    numba = randint(-999, 999)
    lst = lst + [numba]

print(lst)

# ~ найти положительные

ckolka = 0
for nummer in range(100):
    cislox = lst  [nummer]
    if cislox == 0 or cislox < 0:
        plus = 0
    else:
        ckolka = ckolka  + lst [nummer]

print(ckolka)


# ~ - i не используется;
# ~ либо используем,
# ~ либо _,
# ~ либо другой способ,
# ~ напр., list comprehension:
    # ~ RANGE = 999
    # ~ LENGTH = 100
    # ~ lst = [randint(_RANGE, +RANGE) for _ in range(LENGTH)]
# ~ - не нужна отдельнная переменная numba
# ~ и её имя похоже имя станд. библиотеки
# ~ и лучше append

# ~ - что считаем??? количество чисел, их сумму или формируем список положительных???
# ~ - плохие имена переменных
# ~ or не нужен, лучше <=
# ~ а ещё лучше оставить только истинную часть
# ~ - лишняя переменная plus
# ~ - избыточная повторная выборка ckolka в 48


# ~ --- найти общие числа двух списков ---

lst1 = lst2 = []

for i in range(10):
    lst1.append(randint(1, 9))

for i in range(10):
    lst2.append(randint(1, 9))

lst_rezultiruyuschij = []
for pervy in range(10):
    for vtaroi in range(10):
        if lst1[pervy] == lst2[vtaroi]:
            lst_rezultiruyuschij.append(lst1[pervy])

print(lst1)
print(lst2)
print(lst_rezultiruyuschij)


# ~ работает неправильно

# ~ надо(1)

lst1 = [randint(1, 9) for _ in range(10)]
lst2 = [randint(1, 9) for _ in range(10)]
lst_res = []

for e in lst1:
    if e in lst2:
        lst_res.append(e)

print(lst1)
print(lst2)
print(lst_res)

# ~ надо(2)

lst1 = [randint(1, 9) for _ in range(10)]
lst2 = [randint(1, 9) for _ in range(10)]

lst_res = [ e for e in lst1 if e in lst2]

print(lst1)
print(lst2)
print(lst_res)

