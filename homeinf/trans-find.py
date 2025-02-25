#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# trans-find.py
# 2025-02-25 2025-02-25 1.0

# ~ Криптопереводы
# ~ -------------------------------

# ~ Есть много записей о переводах, в т.ч. на одинаковые суммы. 
# ~ Отследить все цепочки.
# ~ (Записи о транзакциях упорядочены по времени.)
# ~ Часть 2. Поиск цепочек транзакций.

from collections import defaultdict
# ~ from copy import deepcopy
import os
import pickle
from pprint import pprint
# ~ from random import randint as ri, choice as ch
import datetime
# ~ from uuid import uuid4 as uuid

fname = 'tmp/transacts.pickle'


def finder():
    """поиск цепочек"""

    if os.path.exists(fname):
        with open(fname, 'rb') as file:
            transx = pickle.load(file)

    print(f"данные прочитаны, размер: {len(transx)}")

    blocks = defaultdict(list)

    for item in transx:
        blocks[item[3]] .append(item)

    print(blocks.keys())

    for k, v in blocks.items():

        if (lv := len(v)) > 1:
            print("\nБлок:", k, ", длина:", lv)
            for b in v:
                print(b)


finder()
