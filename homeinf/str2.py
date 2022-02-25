#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-02-25 2022-02-25 1.0
# str2.py

# ~ в данном тексте найти английские имена, записанные по-английски,
# ~ и распечатать те из них, которые содержат хотя бы две
# ~ одинаковые буквы.

names = '''
1 Olivia Оливия
2 Ava Ава
3 Amelia Амелия
4 Emily Эмили
5 Jessica Джессика
6 Isla Айла
7 Isabella Изабелла
8 Poppy Поппи
9 Mia Мия
10 Sophie Софи
11 Lily Лили
12 Ruby Руби
13 Evie Иви
14 Grace Грейс
15 Ella Элла
16 Sophia София
17 Chloe Хлое
18 Scarlett Скарлетт
19 Freya Фрейя
20 Isabelle Изабель
21 Phoebe Фиби
22 Alice Элис
23 Ellie Элли
24 Bethany Бетани
25 Maryam Мериэм
26 Heidi Хайди
27 Paige Пейдж
28 Faith Фейт
29 Rose Роуз
30 Ivy Айви
31 Florence Флоренс
32 Hurriet Харриэт
33 Maddison Мэдисон
34 Zoe Зоуи
1 Samuel Самуэль
2 Jack Джек
3 Joseph Джозеф
4 Harry Гарри
5 Alfie Алфи
6 Jacob Джейкоб
7 Thomas Томас
8 Charlie Чарли
9 Oscar Оскар
10 James Джеймс
11 William Уильям
12 Joshua Джошуа
13 George Джордж
14 Ethan Итан
15 Noah Ноа
16 Archie Арчи
17 Henry Генри
18 Leo Лео
19 John Джон
20 Oliver Оливер
21 David Дэвид
22 Ryan Райэн
23 Dexter Декстер
24 Connor Коннор
25 Albert Альберт
26 Austin Остин
27 Stanley Стэнли
28 Theodore Теодор
29 Owen Оуэн
30 Caleb Калеб
'''

import string

letters = string.ascii_lowercase
chars = letters + " "

s = names.lower()

so = ""
for c in s:
    if c in chars:
        so += c

s = so
del so

def good(name):
    """есть ли в имени одинаковые буквы"""
    ln = len(name)
    if ln < 2:
        return False
    for c1 in range(ln-1):
        for c2 in range(c1+1, ln):
            if name[c1] == name[c2]:
                return True
    return False
    

for word in s.split():
    if good(word):
        print(word, end=', ')


# ~ olivia, ava, amelia, jessica, isabella, poppy, lily, evie, ella, scarlett, isabelle, phoebe, ellie, maryam, heidi, florence, hurriet, maddison, harry, william, george, david, dexter, connor, theodore,
