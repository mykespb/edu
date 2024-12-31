#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2024
# 2024-12-30 2024-12-30 1.0
# pass-prompter.py

# ~ Подсказки для создания паролей.

# ~ Многие с трудом придумывают пароли.
# ~ Поможем им.
# ~ Пусть пароли все будут такими:
# ~ cvcvdddd либо vcvcdddd
# ~ где v = volwel, c = consonant, d = digit (не 0),
# ~ все латинские, регистр произвольный.

from random import choice, random

vowels     = "aeiouyAEIOUY"
consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
digits     = "123456789"

def make_pass():
    """сделать пароль"""

    out = ( ( choice(vowels) + choice(consonants) + choice(vowels) + choice(consonants)
        if random() < .5
        else choice(consonants) + choice(vowels) + choice(consonants) + choice(vowels) ) +
        choice(digits) + choice(digits) + choice(digits) + choice(digits) )

    return out


def test_make_pass(times=1):
    """тестируем пароль"""

    for rept in range(times):
        print(make_pass())


test_make_pass(20)
