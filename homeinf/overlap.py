#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2022-01-21 2022-04-14 1.1
# overlap.py

# ~ бывает, что конец одного слова совпадает с началом другого слова.
# ~ тогда слова можно наложить друг на друга.

# ~ напр.,
# ~ аспирант + антенна = аспирантенна

# ~ среди заданных пар слов найти самые длинные наложения
# ~ (пар слов - несколько, порядок слов проивольный)

data = """
аспирант антенна
пират вампир
гатино шпагат
утренник перламутр
питон тонна
хозяин колхоз
"""

def obepary(s1, s2):
    para (s1, s2)
    para (s2, s1)

def para (s1, s2):
    maxnal = min(len(s1), len(s2))

    for nal in reversed(range(1, maxnal+1)):
        if s1[-nal:] == s2[:nal]:
            print(s1 + s2[nal:])
            return    

def stroka (s):
    s = s.strip()
    if s:
        print ("\nстрока:", s)
        obepary (*s.split())
    
def tests():
    for el in data.split("\n"):
        stroka(el)

tests()


# ~ строка: аспирант антенна
# ~ аспирантенна
# ~ антеннаспирант

# ~ строка: пират вампир
# ~ вампират

# ~ строка: гатино шпагат
# ~ шпагатино

# ~ строка: утренник перламутр
# ~ перламутренник

# ~ строка: питон тонна
# ~ питонна

# ~ строка: хозяин колхоз
# ~ колхозяин
