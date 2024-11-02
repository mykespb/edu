#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-03-13 2024-10-30 1.2
# langage.py

# ~ Дан текст,
# ~ в котором построчно написаны
# ~ название языка программирования,
# ~ год его разработки,
# ~ автор или коллектив - разработчик;
# ~ всё это - через пробелы.
# ~ Распечатать список вида
# ~ год - язык,
# ~ причём в историческом порядке -
# ~ от самого старого
# ~ к самому новому.

langs = """
C++ 1983 Страуструп, Бьёрн
Java 1995 Джеймс Гослинг и Sun Microsystems
C# 2000 Андерс Хейлсберг
Delphi 1986 Андерс Хейлсберг
Modula-2 1978 Никлаус Вирт
Pascal 1970 Никлаус Вирт
Oberon 1986 Никлаус Вирт
Smalltalk 1969 Алан Кэй, Адель Голдберг, Дэн Ингаллс, Xerox PARC
Erlang 1986 Джо Армстронг
Fortran 1957 Джон Бэкус, IBM
Groovy 2003 Джеймс Стрэкен
Ruby 1995 Мацумото, Юкихиро
Scala 2004 Одерски, Мартин
C 1972 Деннис Ритчи
Simula 1967 Кристен Нюгор и Оле-Йохан Даль
Algol68 1964 Адриан ван Вейнгаарден, Барри Майо и Грегори Пек
Ada 1980 Жан Ишбиа
Python 1991 Гвидо ван Россум
"""

langl = []
for l in langs.strip().split("\n"):
    ls = l.split(maxsplit=2)
    langl.append((ls[1], ls[0]))
langl.sort()
for l in langl:
    print(l[0], '-', l[1])


# ~ 1957 - Fortran
# ~ 1964 - Algol68
# ~ 1967 - Simula
# ~ 1969 - Smalltalk
# ~ 1970 - Pascal
# ~ 1972 - C
# ~ 1978 - Modula-2
# ~ 1980 - Ada
# ~ 1983 - C++
# ~ 1986 - Delphi
# ~ 1986 - Erlang
# ~ 1986 - Oberon
# ~ 1991 - Python
# ~ 1995 - Java
# ~ 1995 - Ruby
# ~ 2000 - C#
# ~ 2003 - Groovy
# ~ 2004 - Scala
