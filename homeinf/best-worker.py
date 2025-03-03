#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-03-03 2025-03-03 1.0
# best-worker.py

# ~ Лучшие сотрудники

# ~ Есть список сотрудников компании,
# ~ у каждого есть коэффициент (0..1)
# ~ и указана его профессия.
# ~ Выбрать "минимальный состав компании",
# ~ т.е. по одному сотруднику с наивысшим коэффициентом.
# ~ (а за 1 проход? а не за 3.
# ~ (за 3:
# ~ 1. выбрать все профессии,
# ~ 2. по каждой: выбрать всех сотрудников,
# ~ 3. из них найти лучшего
# ~ )
# ~ (за 1: for p in staff.sorted(... key=itertools.itemgetter((2, 3))..)
# ~ )

from collections import defaultdict
from operator import itemgetter
from pprint import pprint
from random import choice, randint, random

hr = "\n" + 80 * "=" + "\n"

def maker():
    """make workers list"""

    MANY = 100

    names1 = "Alice Bob Kate Don Ann Franz Halle Ida Lana Mike Nil Oleg Petra Sarah Tina Uma Vika Will Yan Zara".split()
    namesl = "Arrow Boogie Chanes Dodge Eleph Gang Hora Innes Judas Kannie Lounas Medock Narrow Oswald Popov Quadrant Raven Statue Taran Ufolog Warrior Yankey Zulu".split()
    profs  = "Director Accountant Designer Philosopher Writer Assistant Washer Carrier Team_Leader Project_Leader Copyrighter".split()
    
    staff = [ ( choice(namesl), choice(names1), choice(profs), randint(20, 50), random() )
        for i in range(MANY) ]

    # ~ print(hr)
    # ~ pprint(staff)

    return staff


def solver(staff):
    """find the best"""

    # ~ print(hr)

    bests = defaultdict(tuple)

    for person in sorted(staff, key = itemgetter(2, 4)):
        bests[person[2]] = person
        # ~ print(person)

    # ~ print(hr)
    # ~ pprint(bests, width=100, compact=True)

    return bests


def main():
    """run it all"""
    
    staff = maker()
    bests = solver(staff)

    for prof, person in bests.items():
        print(f"{prof:20}", *person, sep = ", ")


main()

# ~ Accountant          , Oswald, Lana, Accountant, 33, 0.9909591298477523
# ~ Assistant           , Lounas, Will, Assistant, 30, 0.9958816919894039
# ~ Carrier             , Medock, Nil, Carrier, 27, 0.9938714912572284
# ~ Copyrighter         , Raven, Will, Copyrighter, 50, 0.9369938920478678
# ~ Designer            , Quadrant, Lana, Designer, 28, 0.9560078117833299
# ~ Director            , Eleph, Petra, Director, 50, 0.9392473274754977
# ~ Philosopher         , Boogie, Alice, Philosopher, 33, 0.6360360333680517
# ~ Project_Leader      , Innes, Zara, Project_Leader, 23, 0.9175725890282539
# ~ Team_Leader         , Judas, Oleg, Team_Leader, 35, 0.9468500506942112
# ~ Washer              , Taran, Alice, Washer, 26, 0.7931019662804607
# ~ Writer              , Warrior, Oleg, Writer, 25, 0.9442344331602278
