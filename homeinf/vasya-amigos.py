#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2026-05-05 2026-05-05 1.0
# vasya-amigos.py

# ~ Васёк пришёл в новую школу и ищет себе друзей.
# ~ Он хочет дружить только с теми, у кого в имени есть хотя бы одна буква из его имени.
# ~ "С остальными,- говорит он,- у меня нет ничего общего".
# ~ Есть список учеников.
# ~ Поможем Ваську найти себе друзей.

man = "Васёк"

klass = "Ябедка Ёксель Добро Шлямза Годно Апчко Куцко Сиротка Думец Зёма Топло"


def amigos(who, they):
    who = who.lower()
    they = they.lower().split()

    good = [guy.capitalize() for guy in they if any( [bukva in guy for bukva in who] )]

    return good


print(amigos(man, klass))
