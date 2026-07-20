#!/usr/bin/env python3

# программа ищет максимумы и минимумы в списке
# (C) М.Колодин, 2021-06-25, 2021-10-06 1.3

# -------------------------------------- подготовка

import random

rang = range(10)

def makerand(size=10, lower=-100, upper=100):
    """ сделать список из size элементов,
    минимальное значение lower,
    максимальное значение upper
    """
    return [random.randint(lower, upper) for _ in range(size)]

def head(s):
    """ напечатать заголовок
    """
    sep = "---------------------------------"
    print(f"\n{sep}\n{s}\n{sep}\n")

def test(f):
    """ запустить функцию на тест """
    for i in rang:
        a = makerand()
        print(a)
        print(f(a))

# -------------------------------------- запуски функций

head("найти максимум")

def getmax1(a):
    """ найти максимум """
    if not a: return None
    return max(a)

print(getmax1([]))
test(getmax1)

def getmax2(a):
    """ найти максимум """
    if not a: return None
    m = a[0]
    for e in a:
        if e > m:
            m = e
    return m

print(getmax2([]))
test(getmax1)

head("найти минимум, нетривиально")

def getmin2(a):
    """ найти минимум """
    if not a: return None
    m = a[0]
    for e in a:
        if e < m:
            m = e
    return m

test(getmin2)

head("найти минимум и максимум за 1 проход")

def getall1(a):
    """ найти максимум и минимум """
    if not a: return None
    mi = ma = a[0]
    for e in a:
        if e > ma: ma = e
        if e < mi: mi = e
    return mi, ma

test(getall1)

head("найти максимум по модулю")

def maxmod1(a):
    """ найти максимум по модулю """
    return sorted(a, key=lambda x: abs(x), reverse=True)[0] if a else None

test(maxmod1)

head("найти максимум и минимум по модулю")

def minmaxmod1(a):
    """ найти минимум и максимум по модулю за 1 проход """
    if not a: return None
    m = sorted(a, key=lambda x: abs(x))
    return m[0], m[-1]

test(minmaxmod1)

def minmaxmod2(a):
    """ найти минимум и максимум по модулю за 1 проход """
    if not a: return None
    return sorted(a, key=lambda x: abs(x))[0: len(a): len(a)-1]

test(minmaxmod2)

# ================= the end.
