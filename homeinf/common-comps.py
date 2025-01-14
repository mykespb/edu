#!/usr/bin/env python

# Mikhail (myke) Kolodin 2022-05-08 2025-01-14 1.5
# common-comps.py

# ~ Несколько человек работали на разные компании.
# ~ Есть список человеков.
# ~ Переписать его как список компаний с сотрудниками,
# ~ а также найти те компании, где работало максимальное количество человек.

persons = """
John Apple Olivetti IBM
Lisa Apple Microsoft
Mikko CASIO Nokia Olivetti
Monica Transdata Integrals Forever Microsoft
Tanita IBM Olivetti Grooming NeverMore Apple
"""

from collections import defaultdict

def recompany():
    """
    перестроить список человеков в список компаний с сотрудниками
    """

    comps = defaultdict(list)

    for person in persons.strip().splitlines():
        name, *where = person.strip().split()

        for place in where:
            comps[place].append(name)

    return comps


def find_mc(loc):
    """
    найти насыщенные сотрудниками компании
    """

    comps = []

    for name, workers in loc.items():
        comps.append( (name, len(workers) ))

    comps.sort( key = lambda x: x[1], reverse = True)

    return comps


def find_max(loc):
    """
    найти ведущую группу насыщенных сотрудниками компаний
    """

    size = -1
    comps = []

    for name, workers in loc.items():
        if (ll := len(workers)) > size:
            size = ll
            comps = [name]
        elif ll == size:
            comps.append(name)

    return size, comps


def main():
    """
    запустить и посмотреть всё
    """

    comps = recompany()
    
    print("\nКомпании и их сотрудники:")
    for key, value in comps.items():
        print(f"{key:20}", end="")
        print(*value, sep=", ", end="")
        print()

    mult_comps = find_mc(comps)
    
    print("\nКомпании по убыванию участников:")
    for comp, size in mult_comps:
        print(f"{comp:20}: {size:3}")

    size, comps = find_max(comps)
    
    print(f"\nКомпании с максимальным количеством участников: {size}\nтакие:", end=" ")
    
    for comp in comps:
        print(comp, end=", ")
    print("\n")


main()

# ------------------------------
# результат:

# ~ Компании и их сотрудники:
# ~ Apple               John, Lisa, Tanita
# ~ Olivetti            John, Mikko, Tanita
# ~ IBM                 John, Tanita
# ~ Microsoft           Lisa, Monica
# ~ CASIO               Mikko
# ~ Nokia               Mikko
# ~ Transdata           Monica
# ~ Integrals           Monica
# ~ Forever             Monica
# ~ Grooming            Tanita
# ~ NeverMore           Tanita

# ~ Компании по убыванию участников:
# ~ Apple               :   3
# ~ Olivetti            :   3
# ~ IBM                 :   2
# ~ Microsoft           :   2
# ~ CASIO               :   1
# ~ Nokia               :   1
# ~ Transdata           :   1
# ~ Integrals           :   1
# ~ Forever             :   1
# ~ Grooming            :   1
# ~ NeverMore           :   1

# ~ Компании с максимальным количеством участников: 3
# ~ такие: Apple, Olivetti, 
