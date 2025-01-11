#!/usr/bin/env python
# Mikhail (myke) Kolodin, 2024
# 2025-01-10 2025-01-10 1.4
# doctors.py

# ~ Два врача принимают клиентов по расписанию.
# ~ Вопросы:
# ~ 1. есть ли дни, когда работают оба?
# ~ 2. есть ли полностью неприёмные дни?

sched = """
Иванов пн ср пт сб
Петров вт ср сб
"""

# ----------------------------------

from collections import defaultdict

listdays = "пн вт ср чт пт сб вс" .split()
setdays  = set(listdays)

print(80*"-")

print(f"{listdays=}")
print(f"{setdays=}")

doctors = defaultdict(set)

for doctor in sched.strip().splitlines():
    name, *days = doctor.strip().split()
    doctors[name] = set(days)

print(f"{doctors=}")

print(80*"-")

# ~ print("1. общие дни:", doctors['Иванов'] & doctors['Петров'])

# ~ print("1. общие дни:", *(doctors['Иванов'] & doctors['Петров']))

print("1. общие дни:", end=" ")

# ~ print( *(doctors['Иванов'] & doctors['Петров']), sep=", ")

print( *sorted ( (doctors['Иванов'] & doctors['Петров']),
    key = lambda x: listdays.index(x)
    ), sep=", ")

# TODO: альтеративно: циклом

# TODO: альтеративно: ...

# ~ print("2. неприёмные дни:", alldays - (doctors['Иванов'] | doctors['Петров']))

# ~ print("2. неприёмные дни:", *(alldays - (doctors['Иванов'] | doctors['Петров'])))

print("2. неприёмные дни:", end=" ")

#print( *(alldays - (doctors['Иванов'] | doctors['Петров'])), sep=", ")

print( *sorted ( (setdays - (doctors['Иванов'] | doctors['Петров'])),
    key = lambda x: listdays.index(x)
    ),sep=", ")

# TODO: альтеративно: циклом

# TODO: альтеративно: ...

print(80*"-")


# ----------------------------------
# результаты:

# ~ --------------------------------------------------------------------------------
# ~ listdays=['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
# ~ setdays={'вс', 'вт', 'ср', 'сб', 'пн', 'чт', 'пт'}
# ~ doctors=defaultdict(<class 'set'>, {'Иванов': {'пн', 'пт', 'ср', 'сб'}, 'Петров': {'сб', 'вт', 'ср'}})
# ~ --------------------------------------------------------------------------------
# ~ 1. общие дни: ср, сб
# ~ 2. неприёмные дни: чт, вс
# ~ --------------------------------------------------------------------------------

# ----------------------------------
