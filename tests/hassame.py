#/usr/bin/env python3

# программа ищет одинаковые элементы
# (C) М.Колодин, 2021-06-23, 2021-06-25 1.4

# функции для поиска

def has1(l):
    """ классический вариант,
    сравниваем каждый элемент списка с каждым после него
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
    и сравниваем длины до и после
    """
    return len(l) != len(set(l))

def has3(l):
    """ сортируем список,
    а потом сравниваем только рядом стоящие элементы
    """
    ll = sorted(l)
    for i in range(0, len(ll)-1):
        if ll[i] == ll[i+1]:
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

def has5(l):
    """ работаем как со стеком с доступом вглубь -
    с подсчётом числа вхождений вершины в глубине стека
    """
    ll = l.copy()
    while ll:
        e = ll.pop()
        if ll.count(e):
            return True
    return False

def has6(l):
    """ применяем обычные словари
    """
    d = {}
    for e in l:
        if e in d:
            return True
        d[e] = 1
    return False

from collections import defaultdict

def has7(l):
    """ применяем словари с инициализацией по умолчанию (defaultdict)
    """
    if not l: return False
    d = defaultdict(int)
    for e in l:
        d[e] += 1
    f = list(filter(lambda x: x>1, d.values()))
    return len(f) > 0

def has8(l):
    """ применяем множества
    """
    s = set()
    for e in l:
        if e in s:
            return True
        s |= {e}
    return False

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
            try:
                test(l, hasf)
            except:
                print("*** Exception!")

# запуск тестов

ls = [
    [1, 1, 2, 3],
    [1, 2, 3],
    [],
    [1, 2, 3, 2, 1, 2, 3],
    ["this", "is", "a", "program"],
    "here we go again and again".split(),
    "Return the number of times x appears in the list".split(),
    [1, 0, -1, "hello", "world", "привет", "мир"]
    ]

hasfs = has1, has2, has3, has4, has5, has6, has7, has8

tests()
