#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# trans-gen.py
# 2025-02-24 2025-02-25 1.0

# ~ Криптопереводы
# ~ -------------------------------

# ~ Есть много записей о переводах, в т.ч. на одинаковые суммы. 
# ~ Отследить все цепочки.
# ~ (Записи о транзакциях упорядочены по времени.)
# ~ Часть 1. Создание цепочек транзакций.

from copy import deepcopy
import os
import pickle
from pprint import pprint
from random import randint as ri, choice as ch
import datetime
from uuid import uuid4 as uuid

fname = 'tmp/transacts.pickle'


def generate(trans = 500, usernum = 100):
    """создать trans случайных транзакций между usernum пользователями"""

    users = [ uuid().hex for _ in range(usernum)]
    print(users)

    dt = datetime.datetime(2010, 1, 1)
    print(f"{dt=}")

    transx = []

    for rept in range(trans // 5):

        delta = datetime.timedelta(
            days = ri(1, 50),
            hours = ri(1, 23),
            minutes = ri(1, 59),
            seconds = ri(1, 59)
            )

        dt += delta

        amount = ri(1, 10_000_000)

        u_from = ch(users)
        u_to   = ch(users)

        if u_from == u_to:
            continue

        transx.append( (dt, u_from, u_to, amount) )

    transbase = deepcopy(transx)

    # ~ for rept in range(trans * 4 // 5):
    for rept in range(trans // 2):

        dt, u_from, u_to, amount = ch(transbase)
        done = [u_from, u_to]

        for again in range(ri(5, 9)):

            delta = datetime.timedelta(
                days = ri(1, 50),
                hours = ri(1, 23),
                minutes = ri(1, 59),
                seconds = ri(1, 59)
                )

            dt += delta

            u_next = ch(users)

            frommers = set( [x[1] for x in transx] )

            if u_next in done or u_to in frommers:
                continue

            done.append(u_next)

            transx.append( (dt, u_to, u_next, amount) )

            u_to = u_next

    transx.sort()

    pprint(transx)

    with open(fname, 'wb') as file:
        pickle.dump(transx, file)

generate()
