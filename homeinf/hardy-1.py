#!/usr/bin/env python
# 
# # hardy.py (C) M.Kolodin 2022
# 2022-06-10 2022-06-10 3.6
# find 2 pairs for 1729

# ~ Любопытный факт: 1729 — это самое маленькое положительное число, которое можно представить в виде суммы кубов двух положительных чисел двумя способами. Исторический анекдот связывает это число с индийским математиком Сринивасой Рамануджаном, который рассказал о нём своему наставнику Готфри Харолду Харди.
# ~ Харди часто навещал Рамануджана, когда тот, умирая, находился в больнице в Патни. Именно в одно из таких посещений произошёл «инцидент» с номером такси. Харди приехал в Патни на такси, воспользовавшись своим излюбленным транспортным средством. Он вошёл в палату, где лежал Рамануджан. Начинать разговор Харди всегда было мучительно трудно, и он произнёс свою первую фразу: «Если не ошибаюсь, то номер такси, на котором я приехал, 1729. Мне кажется, это скучное число». На что Рамануджан тотчас же ответил: «Нет, Харди! О нет! Это очень интересное число. Это самое малое из чисел, представимых в виде суммы двух кубов двумя различными способами».

import math

# ~ pair: i=1^3 * j=12^3 = 1729
# ~ pair: i=9^3 * j=10^3 = 1729

def pairs0с(NUM = 1729):
    """Найти 2 пары кубов"""

    print("\npairs0\n")
    count = 0
    limit = NUM
    for i in range(1, limit):
        for j in range(i, limit):
            count += 1
            if i**3 + j**3 == NUM:
                print(f"pair ({i},{j}): {i} ^ 3 * {j } ^ 3 = {NUM}")
    print(f"{count=:_}")

pairs0с()

def pairs1с(NUM = 1729):
    """Найти 2 пары кубов"""

    print("\npairs1\n")
    count = 0
    limit = math.isqrt(NUM)
    for i in range(1, limit):
        for j in range(i, limit):
            count += 1
            if i**3 + j**3 == NUM:
                print(f"pair ({i},{j}): {i} ^ 3 * {j } ^ 3 = {NUM}")
    print(f"{count=:_}")

pairs1с()

def pairs2с(NUM = 1729):
    """Найти 2 пары кубов"""

    print("\npairs2\n")
    count = 0
    limit = int(round(pow(NUM, 1/3))) + 1
    for i in range(1, limit):
        for j in range(i, limit):
            count += 1
            if i**3 + j**3 == NUM:
                print(f"pair ({i},{j}): {i} ^ 3 * {j } ^ 3 = {NUM}")
    print(f"{count=:_}")

pairs2с()


# ~ pairs0

# ~ pair (1,12): 1 ^ 3 * 12 ^ 3 = 1729
# ~ pair (9,10): 9 ^ 3 * 10 ^ 3 = 1729
# ~ count=1_493_856

# ~ pairs1

# ~ pair (1,12): 1 ^ 3 * 12 ^ 3 = 1729
# ~ pair (9,10): 9 ^ 3 * 10 ^ 3 = 1729
# ~ count=820

# ~ pairs2

# ~ pair (1,12): 1 ^ 3 * 12 ^ 3 = 1729
# ~ pair (9,10): 9 ^ 3 * 10 ^ 3 = 1729
# ~ count=78
