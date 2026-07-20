#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-11-21 2021-11-21 1.0
# slogi.py
# ~ сколько слогов в словах строки

stroka = "Вместе весело шагать по просторам!"

vowels = "УЕЫАОЭЯИЮуеыаоэяиюЁё"

print(f"строка: {stroka}")

for slovo in stroka.split():

    vows = 0
    for letter in slovo:
        if letter in vowels:
            vows += 1

    print(f"слово: {slovo}, слогов: {vows}")
