#!/usr/bin/env python

# loto.py
# (C) Mikhail (myke) Kolodin, 2021
# 2022-01-10 2022-01-10 1.0

# ~ примитивный вариант примитивной игры

import random, collections

NUMPLAYERS = 4    # сколько игроков

ALLNAMES = """
A Alfa
B Bravo
C Charlie
D Delta
E Echo
F Foxtrot
G Golf
H Hotel
I India
J Juliett
K Kilo
L Lima
M Mike
N November
O Oscar
P Papa
Q Quebec
R Romeo
S Sierra
T Tango
U Uniform
V Victor
W Whiskey
X X-ray
Y Yankee
Z Zulu
""".split()

NAMES = {ALLNAMES[i]: ALLNAMES[i+1] for i in range(0, len(ALLNAMES), 2)}

PLAYERS = list(NAMES.values())

# ~ print(PLAYERS)

LIMIT   = 90     # до скольки бочонки и номера
ONCARD  = 15     # сколько чисел на карточке

def play():
    """раунд игры"""

    players = sorted(random.sample(PLAYERS, NUMPLAYERS))
    print("\nиграют:", players, "\n")

    topick = list(range(1, LIMIT+1))

    boxes = []
    for pl in range(NUMPLAYERS):
        boxes.append(sorted(random.sample(topick, ONCARD)))

    for pl in range(NUMPLAYERS):
        print(players[pl], "=>", boxes[pl])
    print()

    random.shuffle(topick)
    # ~ print("порядок:", topick)

    need = True
    while topick and need:
        shout = topick.pop(0)
        print("сыграло:", shout, end="")

        for pl in range(NUMPLAYERS):
            if shout in boxes[pl]:
                print(", есть у", players[pl], end="")
                boxes[pl].remove(shout)

                if len(boxes[pl]) == 0:
                    print("\nвыиграл", players[pl])
                    need = False

        print()

play()
