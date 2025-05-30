#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-05-30 2025-05-30 1.0
# ~ whowhat.py 
# ~ Кто что купил?
# ~ Есть список сделок, причём указаны как покупатели, так и покупки, вещи, деньги.
# ~ Показать, кто кому что продал.

from pprint import pprint
from random import shuffle, choice, randint

def gen(size=10):
    """создать список покупок"""

    names = "Oliver Boris Jack Jane Jacob Thomas Charlie Oscar James William Jake Connor Mason Kyle Joe David Harry Alex Anna Heather Sonya Pamela Zoe Emma Ava Emily Victoria Tracy Lily Charlotte Mia Isla Poppy Jessica Lucy Michael George Reece Callum Daniel Sarah Alla Dennis Helen Jake Mila Laura Nina Milana Nick Rose Rachel Tina Uma" . split()

    things = "box toy car flower jewel something computer lamp book voyage yacht cake phone chair baloon picture animal boat goat cat dog joke crown house" . split()

    lot = []
    for _ in range(size):
        pers_from = choice(names)
        pers_to   = choice(names)
        thing     = choice(things)
        price     = randint(100, 100_000)
        lot.append( (pers_from, pers_to, thing, price) )
        lot.append( (pers_to, pers_from, thing, -price) )

    shuffle(lot)
    return lot


def solve(lot):
    """показать, кто что у кого купил"""

    # ~ pprint(lot)

    for first in lot:
        if first[3] > 0:
            pers_from, pers_to, thing, price = first
            for second in lot:
                if second == (pers_to, pers_from, thing, -price):
                    # ~ print(f"{first=} {second=}")
                    print(f"{pers_from} sold {thing} to {pers_to} for ${price:_}")

    

def main():
    """запускаем..."""

    lot = gen()
    solve(lot)


main()

# ~ result:
# ~ Laura sold baloon to Jane for $10_764
# ~ Alla sold cake to Jane for $3_071
# ~ Callum sold boat to Milana for $41_349
# ~ Victoria sold yacht to Anna for $74_859
# ~ David sold baloon to Mason for $17_633
# ~ Harry sold computer to David for $21_586
# ~ Jake sold voyage to Victoria for $40_637
# ~ Lucy sold cake to Mila for $89_989
# ~ Isla sold car to Heather for $48_207
# ~ Uma sold computer to Michael for $82_748
