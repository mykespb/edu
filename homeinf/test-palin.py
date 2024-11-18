#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-12-04 2021-12-04 1.2
# test-palin.py

# ~ проверить, является ли фраза палиндромом
# ~ хорошо бы сразу прокрутить несколько примеров

stroki = """
Лёша на полке клопа нашёл
караван ван драм пан
А роза упала на лапу Азора.
Аргентина манит негра
Я иду съ мечемъ судия
силен несил
Я - арка края
Молебен о коне белом
О, лета тело!
Лег на храм, и дивен и невидим архангел
они, топот, инок,
боком комок лом
Но не речь, а черен он.
Идем, молод, долом меди.
Чин зван мечем навзничь.
Голод, чем меч долог?
Пал, а норов худ и дух ворона лап.
А что? Я лов? Воля отча!
Яд, яд, дядя!
виноват тинотав
Иди, иди!
мужик ел жмых
сам сидел леди спел
Мороз в узел, лезу взором.
Солов зов, воз волос.
Колесо. Жалко поклаж. Оселок.
Сани, плот и воз, зов и толп и нас.
Горд дох, ход дрог.
И лежу. Ужели?
Зол, гол лог лоз.
И к вам и трем с смерти мавки.
сноб бос и голос
Signa te signa, temere me tangis et angis,
Roma tibi subito motibus ibit amor.
Sum summus mus
"""

print ("""
----------------------------------------------
                 ПАЛИНДРОМЫ
----------------------------------------------
""")

for afrase in stroki.split("\n"):
    frase = afrase.strip()
    if not frase:
        continue

    frase = frase.lower()
    frase = (frase
        .replace(" ", "")
        .replace("\t", "")
        .replace(".", "")
        .replace(",", "")
        .replace(":", "")
        .replace(";", "")
        .replace("!", "")
        .replace("?", "")
        .replace("-", "")
        .replace("ь", "")
        .replace("ъ", "")
        )

    if frase == frase[::-1]:
        print ("да: ", afrase)
    else:
        print ("нет:", afrase)
