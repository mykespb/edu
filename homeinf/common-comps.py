#!/usr/bin/env python

# Mikhail (myke) Kolodin 2022-05-08 2025-01-12 1.2
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
Tanita IBM Olivetti Grooming NeverMore
"""

from collections import defaultdict, Counter
# ~ from pprint import pprint

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


def main():
    """
    запустить и посмотреть всё
    """

    comps = recompany()
    
    print("\nКомпании и их сотрудники:")
    # ~ pprint(dict(comps))
    for key, value in comps.items():
        print(f"{key:20}", end="")
        print(*value, sep=", ", end="")
        # ~ print(f"{key:20}", *value, end="")
        # ~ for it in value:
            # ~ print(it, end=", ")
        print()

    mult_comps = find_mc(comps)
    
    print("\nКомпании по убыванию участников:")
    for comp, size in mult_comps:
        print(f"{comp:20}: {size:3}")
    # ~ print(mult_comps, sep="\n", end="\n\n")


main()


# ~ Компании и их сотрудники:
# ~ Apple               John, Lisa
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
# ~ Olivetti            :   3
# ~ Apple               :   2
# ~ IBM                 :   2
# ~ Microsoft           :   2
# ~ CASIO               :   1
# ~ Nokia               :   1
# ~ Transdata           :   1
# ~ Integrals           :   1
# ~ Forever             :   1
# ~ Grooming            :   1
# ~ NeverMore           :   1
