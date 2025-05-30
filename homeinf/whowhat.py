#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-05-30 2025-05-30 2.0
# ~ whowhat.py 
# ~ Кто что купил?
# ~ Есть список сделок, причём указаны как покупатели, так и покупки, вещи, деньги.
# ~ Показать, кто кому что продал.
# ~ Причём продающий = получивший деньги - платит налог, и суммы не совпадают.

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
        tax       = randint(1, price // 5)
        lot.append( (pers_from, pers_to, thing, tax) )
        lot.append( (pers_to, pers_from, thing, -price) )

    shuffle(lot)
    return lot


def solve(lot):
    """показать, кто что у кого купил"""

    # ~ pprint(lot)

    for first in lot:
        if first[3] > 0:
            pers_from, pers_to, thing, tax = first
            for second in lot:
                if second[:3] == (pers_to, pers_from, thing):
                    price = -second[-1]
                    print(f"{pers_from} sold {thing} to {pers_to} for ${price:_} with tax ${tax:_}")

    

def main():
    """запускаем..."""

    lot = gen()
    solve(lot)


main()

# ~ result:
# ~ Zoe sold chair to Isla for $24_480 with tax $4_346
# ~ Rachel sold car to Mila for $6_302 with tax $170
# ~ Uma sold dog to Jake for $80_560 with tax $2_678
# ~ Michael sold chair to Alla for $92_838 with tax $3_553
# ~ Boris sold boat to Laura for $56_735 with tax $5_182
# ~ Isla sold goat to Lily for $95_572 with tax $14_024
# ~ Reece sold phone to Helen for $58_276 with tax $1_898
# ~ Charlie sold jewel to Jacob for $24_015 with tax $1_697
# ~ Helen sold voyage to Jake for $87_846 with tax $14_020
# ~ Heather sold lamp to Lily for $68_473 with tax $1_847
