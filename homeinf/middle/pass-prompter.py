#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-31 2024-12-31 1.1
# pass-prompter.py

# ~ Подсказки для создания паролей.

# ~ Многие с трудом придумывают пароли.
# ~ Поможем им.
# ~ Пусть пароли все будут такими:
# ~ cvcvdddd либо vcvcdddd
# ~ где v = volwel, c = consonant, d = digit (не 0),
# ~ все латинские, регистр произвольный, но у всех букв одинаковый.

from random import choice, random

vowels     = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxz"
digits     = "123456789"

def make_pass():
    """сделать пароль"""

    out = ( ( choice(vowels) + choice(consonants) + choice(vowels) + choice(consonants)
        if random() < .5
        else choice(consonants) + choice(vowels) + choice(consonants) + choice(vowels) ) +
        choice(digits) + choice(digits) + choice(digits) + choice(digits) )

    if random() < .5:
        out = out.upper()

    return out


def test_make_pass(times=1):
    """тестируем пароль"""

    for rept in range(times):
        print(make_pass())


test_make_pass(10)
