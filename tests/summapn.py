#!/usr/bin/env python3

# программа ищет суммы положительных и отрицательных чисел в списке
# (C) М.Колодин, 2021-06-25, 2021-08-26 1.2

# -------------------------------------- подготовка

import random

ranger = range(10)

def makerand(size=10, low=-100, upp=100):
    """ сделать список из size элементов,
    минимальное допустимое значение lower,
    максимальное допустимое значение upper
    """
    return [random.randint(low, upp) for _ in range(size)]

def head(s):
    """ напечатать заголовок
    """
    sep = 20 * "-"
    print(f"\n{sep}\n{s}\n{sep}\n")

def test(f):
    """ запустить функцию на тест
    """
    sep = 20 * "-"
    print("\n", sep, "function:", f.__name__, sep, "\n")
    for i in ranger:
        a = makerand()
        print("in: ", a)
        print("out:", f(a))

# -------------------------------------- функция 1

def sumpn1(a):
    """функция sumpn1
    считает суммы + и - чисел
    """
    sump = sumn = 0
    for e in a:
        if e < 0:
            sumn += e
        else:
            sump += e
    return sumn, sump

test(sumpn1)

# -------------------------------------- функция 2

def sumpn2(a):
    """функция sumpn2 - тоже про суммы
    """
    return (
        sum([x for x in a if x<0]),
        sum([x for x in a if x>0])
        )

test(sumpn2)

# -------------------------------------- конец вызовов

print("\n\nпро функции: классы, имена, описания, вызовы:\n")
print(sumpn1)
print(type(sumpn1))
print(sumpn1.__name__)
print(sumpn1.__doc__)
print([-1, 0, 1], "-->", sumpn1([-1, 0, 1]))

# ~ про функции: классы, имена, описания, вызовы:

# ~ <function sumpn1 at 0x7fa676971790>
# ~ <class 'function'>
# ~ sumpn1
# ~ функция sumpn1
    # ~ считает суммы + и - чисел

# ~ [-1, 0, 1] --> (-1, 1)

# -------------------------------------- конец всего
