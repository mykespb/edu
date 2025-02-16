#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-02-17 2025-02-17 1.1
# summer-januar.py

# ~ Летний январь

# ~ В детской песенке из фильма поётся:
# ~ "Это было прошлым летом
# ~ в середине января
# ~ в тридесятом королевстве,
# ~ там, где нет в помине короля..."

# ~ Даны координаты нескольких городов
# ~ и списки королевств.
# ~ Определить, в каком (каких) из городов могли честно и не сказочно петь эту песню.
# ~ Объяснить почему.

# ~ (решение: 'S' in city[0] and city[2] in kingdoms.split() и не GB - всё :)
# ~ это южное полушарие, королевство и не Великобритания)


cities = """
30 E 60 N,Saint Petersburg,RU
60 N 25 E,Helsinki,FI
59 N 18 E,Stockholm,SE
60 N 11 E,Oslo,NO
55 N 13 E,Kopenhagen,DK
34 N 15 E,Valetta,MT
35 S 149 E,Canberra,AU
41 S 175 E,Wellington,NZ
17 N 62 W,Basseterre,SKN
14 N 61 W,Castries,SL
15 S 48 W,Brasilia,BR
"""

kingdoms = "NZ AU SE GB NO DK CA SL SKN".strip().split()


for city in cities.strip().splitlines():
    where, name, country = city.strip().split(',')

    if 'S' in where and country in kingdoms and country != 'GB':
        print(f"city: {name}")


# результат:
# ~ city: Canberra
# ~ city: Wellington
