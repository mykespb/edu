#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2021-11-16 2021-11-26 2.1
# populaty.py

# ~ В некотором лесу, в некотором бору живёт популяция популятов.
# ~ Наблюдательные биологи пронаблюдали и заметили,
# ~ что если популятов больше нормы (или ровно норма),
# ~ то к следующему сезону лишние вымирают и их остаётся
# ~ на 10% меньше от прежнего (депопулируют),
# ~ а если меньше нормы, то они прирастают на 10% (популируют).
# ~ Показать размер популяции популятов за 10 лет
# ~ (если поначалу была как раз норма).

import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
# ~ print (locale.getdefaultlocale())

# зададим начальное значение популяции
print ("year\tpopulation")
pop = 1.0
print ("%d\t%f" % (0, pop))

# перебираем по годам
for year in range(1, 11):
    if pop >= 1.:
        pop *= 0.9
    elif pop < 1.:
        pop *= 1.1
    # ~ print (f"{year}\t{pop:,.6f}")
    # ~ print ("{:d}\t{:-,f}" .format (year, pop))
    print (f"{year:d}\t{locale.format_string('%.6f', pop)}")

# ~ https://stackoverflow.com/questions/55379722/how-to-format-a-float-with-a-comma-as-decimal-separator-in-an-f-string
