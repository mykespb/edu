#!/python3.10

# Mikhail (myke) Kolodin, 2021
# 2021-10-21 2021-10-21 1.0
# retext.py
# Заменить во входном тексте указанное слово на случайный вариант
# из предложенного набора заменителей.
# Параметры - в командной строке.

import re, random, sys

t1 = """
here we go again and we know:
here we do the same
"""

def redo(text: str, aword: str, subs: list) -> str:
    """ заменятель """
    return re.sub(f'(\W{aword}\W)', " "+random.choice(subs)+" ", text)

def test1():
    """ тестировщик """
    w = "we"
    s = ["they", "he", "she"]
    print(w, "->", s, "\n", t1, "\n", redo(t1, w, s))

test1()

