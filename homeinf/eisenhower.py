#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-21 2025-02-21 1.0
# eisenhower.py

# ~ Матрица Эйзенхауэра
# ~ ---------------------------------------

# ~ Дела бывают:
# ~ а. срочные и несрочные
# ~ б. важные и неважные.

# ~ Построить матрицу для работы с ними:
# ~ 1. добавление дел,
# ~ 2. удаление дел,
# ~ 3. перенос из одной группы в любую другую.

# ~ Работа в текстовом режиме.

# ~ Вся база автосохраняется на диске в формате pickle.

import os
import pickle

def work():
    """вся работа"""

    print("\n***** Матрица Эйзенхауэра *****")

    db = 'tmp/eisenhower.pickle'

    groups = {0: 'срочные важные',
        1: 'срочные неважные',
        2: 'несрочные важные',
        3: 'несрочные неважные'}

    if os.path.exists(db):
        with open(db, 'rb') as file:
            data = pickle.load(file)

        if len(data):
            maxnum = max( [ p[1] for p in data ] )
        else:
            maxnum = 0
            
    else:
        data = []
        maxnum = 0

    while True:

        # ~ print(data)

        for igroup, group in groups.items():
            print(f"\n----- {igroup} : {group} -----\n")

            gdata = sorted( [ x for x in data if x[0] == igroup] )

            for ielem, num, elem in gdata:
                print(f"дело {num}. {elem}")

        cmd = input('\nвведите команду или "?": ')

        if cmd == '?':
            print("""
Управление матрицей Эйзенхауэра:
?                - получение этой справки,
+группа дело     - добавление дела в группу ([св]),
-номер           - удаление дела с указанным номером,
=номер группа    - перемещение дела с указанным номером в группу [св],
.                - выход
""")

        elif cmd == '.':

            with open(db, 'wb') as file:
                pickle.dump(data, file)
            
            break

        elif cmd.startswith('+'):
            g, d = cmd.strip().split(maxsplit=1)
            maxnum += 1
            
            if g == '+св' or g == '+вс':
                data.append([0, maxnum, d])
            elif g == '+с':
                data.append([1, maxnum, d])
            elif g == '+в':
                data.append([2, maxnum, d])
            else:
                data.append([3, maxnum, d])

        elif cmd.startswith('-'):
            did = int(cmd.strip().split()[0][1:])
            for i in range(len(data)):
                if data[i][1] == did:
                    del data[i]
                    break                    

        elif cmd.startswith('='):
            did, *togroup = cmd.strip().split()
            did = int(did[1:])

            if not togroup:
                togroup = ''
            else:
                togroup = togroup[0]
            
            if togroup == 'вс':
                togroup = 0
            elif togroup == 'св':
                togroup = 0
            elif togroup == 'с':
                togroup = 1
            elif togroup == 'в':
                togroup = 2
            else:
                togroup = 3

            for i in range(len(data)):
                if data[i][1] == did:
                    data[i][0] = togroup
                    break                    

        else:
            print('Для получения справки нажмите "?", а для выхода - "."')

    print('\nСпасибо за работу с нашей программой!\n')

work()

# ~ https://ru.wikipedia.org/wiki/%D0%9C%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0_%D0%AD%D0%B9%D0%B7%D0%B5%D0%BD%D1%85%D0%B0%D1%83%D1%8D%D1%80%D0%B0
# ~ https://skillbox.ru/media/management/matritsa_eyzenkhauera/?admitad_uid=f8bc7ddb28931a5c0198dcb961c5d966&utm_source=admitad&utm_medium=cpa&utm_campaign=affiliate&utm_content=58&utm_term=f8bc7ddb28931a5c0198dcb961c5d966
# ~ https://trends.rbc.ru/trends/education/60a519599a7947430a73ff6b
# ~ https://ru.wikipedia.org/wiki/%D0%AD%D0%B9%D0%B7%D0%B5%D0%BD%D1%85%D0%B0%D1%83%D1%8D%D1%80,_%D0%94%D1%83%D0%B0%D0%B9%D1%82_%D0%94%D1%8D%D0%B2%D0%B8%D0%B4
