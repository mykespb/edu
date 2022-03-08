#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-03-07 2022-03-07 1.0
# list-zavod.py

# ~ Дан список сотрудников, их должностей и зарплат вида
# ~ zavod = [[”Иванов И.И.”, ”директор”, 1000000], [”Петров П.П.”, ”инженер”, 1000],  [”Сидоров С.С.”, ”инженер”, 1100],  [”Кузькин К.К.”, ”инженер”, 900],  [”Ничевохин Н.Н.”, ”стажёр”, 100]]
# ~ Найдите среднюю и медианную зарплаты.
# ~ Сделайте выводы.
# ~ Примечание. Среднее здесь - это среднее арифметическое. Медиана - это такое число в списке, что половина остальных значений больше него, а другая половина - меньше.

zavod = [["Иванов И.И.", "директор", 1000000], ["Петров П.П.", "инженер", 1000],  ["Сидоров С.С.", "инженер", 1100], ["Кузькин К.К.", "инженер", 900], ["Ничевохин Н.Н.", "стажёр", 100]]

def avg(zav):
    """считаем среднее"""
    summa = 0
    for e in zav:
        summa += e[2]
    return int(summa / len(zav))

def less(zav, e):
    """сколько зарплат меньше е"""
    num = 0
    for v in zav:
        if v[2] < e:
            num += 1
    return num

def greater(zav, e):
    """сколько зарплат больше е"""
    num = 0
    for v in zav:
        if v[2] > e:
            num += 1
    return num

def mean(zav):
    """считаем медиану"""
    lm = []
    for v in zav:
        e = v[2]
        lv = less(zav, e)
        gv = greater(zav, e)
        if abs(lv - gv) <= 1:
            return e
    

print(f"завод: {zavod}"
    f"\n\nсредняя зарплата:   {avg(zavod) : 10_}"
    f"\nмедианная зарплата: {mean(zavod) : 10_}"
    )
