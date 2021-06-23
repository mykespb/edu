#/usr/bin/env python3

# программа ищет одинаковые элементы
# (C) М.Колодин, 2021-06-23, 1.0

# функции для поиска

def has1(l):
    """ классический вариант,
    сравниваем каждый элемент списка с каэжым после него
    """
    lenl = len(l)
    for i in range(0, lenl-1):
        for j in range(i+1, lenl):
            if l[i] == l[j]:
                return True
    return False

def has2(l):
    """ преобразуем ко множеству,
    тем самым удаляем повторы,
    и сравниаем длины до и после
    """
    return len(l) != len(set(l))

def has3(l):
    """ сортируем список,
    а потом сравниваем только рядом стоящие элементы
    """
    l.sort()
    for i in range(0, len(l)-1):
        if l[i] == l[i+1]:
            return True
    return False

from collections import Counter

def has4(l):
    """ используем класс Счётчик,
    преобразуем список к счётчику,
    берём наиболее часто встречающееся значние,
    если оно появилось более 1 раза, то успех
    """
    if not l: return False
    return Counter(l).most_common(1)[0][1] > 1

# утилиты для тестирования

def test(l, hasf):
    """ один тест - список и функция
    """
    print("\n----------------------\ntesting", hasf.__name__, "for list", l)
    print(hasf(l))

def tests():
    """ диспетчер тестов -- каждый список с каждой функцией
    """
    for hasf in hasfs:
        for l in ls:
            test(l, hasf)

# запуск тестов

ls = [
    [1, 1, 2, 3],
    [],
    [1, 2, 3],
    [1, 2, 3, 2, 1, 2, 3],
    "this is a program".split(),
    "here we go again and again".split()
    ]

hasfs = has1, has2, has3, has4

tests()
