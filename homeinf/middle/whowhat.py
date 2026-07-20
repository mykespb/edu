#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-05-30 2025-05-30 2.1
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
        lot.append( (pers_from, pers_to, thing, price-tax) )
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
                    print(f"{pers_from} sold {thing} to {pers_to} for ${price:_} with tax {(price - tax) * 100 / price :.2f}% as ${price - tax}")

    

def main():
    """запускаем..."""

    lot = gen()
    solve(lot)


main()

# ~ result:
# ~ William sold crown to Nina for $37_719 with tax 8.52% as $3215
# ~ Victoria sold lamp to Michael for $76_265 with tax 10.54% as $8035
# ~ Jane sold crown to Mason for $40_507 with tax 13.50% as $5469
# ~ Charlotte sold flower to Milana for $83_070 with tax 0.77% as $641
# ~ Milana sold lamp to Pamela for $8_579 with tax 16.76% as $1438
# ~ David sold flower to Nina for $54_621 with tax 2.90% as $1583
# ~ Sonya sold flower to Victoria for $36_571 with tax 12.23% as $4474
# ~ Reece sold computer to Jane for $82_011 with tax 17.61% as $14446
# ~ Pamela sold cat to Emily for $72_681 with tax 16.56% as $12039
# ~ Alex sold boat to David for $73_470 with tax 19.68% as $14458
