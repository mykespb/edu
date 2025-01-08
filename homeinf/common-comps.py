#!/usr/bin/env python
# myke 2022-05-08 2025-01-08 1.0
# common-comps.py

# ~ Несколько человек работали на разные компании.
# ~ Есть список человеков.
# ~ Переписать его как список компаний с сотрудниками,
# ~ а также найти те компании, где работало максимальное количество человек.

persons = """
John Apple Olivetti IBM
Lisa Apple Microsoft
Mikko CASIO Nokia
Monica Transdata Integrals Forever
Tanita IBM Olivetti
"""

from collections import defaultdict
from pprint import pprint

def recompany():
    """
    перестроить список человеков в список компаний с сотрудниками
    """

    comps = defaultdict(list)

    for person in persons.strip().splitlines():
        name, *where = person.split()

        for place in where:
            comps[place].append(name)

    return comps


def main():
    """
    запустить и посмотреть всё
    """

    comps = recompany()
    pprint(comps)


main()
