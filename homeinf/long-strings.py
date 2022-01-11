#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-11-25 2022-01-11 1.1
# long-strings.py

# упражнения с длинными строками
# ~ в каждой строке найти самое короткое и самое длинное слово
# ~ учитываются только буквы, без знаков препинания
# ~ и кириллица, и латиница

ls = """Какие нервные лица - быть беде;
Я помню, было небо, я не помню где;
Мы встретимся снова, мы скажем "Привет", -
В этом есть что-то не то;
Рок-н-ролл мертв, а я еще нет,
Рок-н-ролл мертв, а я;
Те, что нас любят, смотрят нам вслед.
Рок-н-ролл мертв, а я еще нет.
"""

alfa = "abcdefghijklmnopqrstuvwxyz" + "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
chars = alfa + " "

# ~ print (ls)

for i, l in enumerate(ls.split("\n")):
    # ~ print (i, l)
    l = l.strip()
    if not l:
        continue

    s = ""
    for c in l.lower():
        if c in chars:
            s += c

    print(s)

    longlen = shortlen = -1
    shortword = longword = ""

    for word in s.split():
        alen = len(word)
        if longlen == -1 or alen > longlen:
            longlen = alen
            longword = word
        if shortlen == -1 or alen < shortlen:
            shortlen = alen
            shortword = word

    print("короткое:", shortword, ", букв:", shortlen)
    print("длинное: ", longword,  ", букв:", longlen)
