#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-01-19 2025-01-19 0.1
# australia.py

# ~ Есть информация об Австралии.
# ~ Узнать, где больше территория, где население,
# ~ сколько там чего (штатов, территорий).

# ~ Учебное: отрабатываем именованные кортежи

# -------------------------------------------------
# тексты

data = """
№	Название	Тип адм. ед.	Столица	Население, чел. (2021)	Площадь, км²
1	Австралийская столичная территория	территория	Канберра	454499	2358
2	Виктория	штат	Мельбурн	6503491	227444
3	Западная Австралия	штат	Перт	2660026	2527013
4	Квинсленд	штат	Брисбен	5156138	1729742
5	Новый Южный Уэльс	штат	Сидней	8072163	801150
6	Северная территория	территория	Дарвин	232605	1347791
7	Тасмания	штат	Хобарт	557571	68401
8	Южная Австралия	штат	Аделаида	1781516	984321
0	Всего	нет	нет	25422788	7688220
"""

# -------------------------------------------------
# импорты и настройки

from collections import namedtuple

# -------------------------------------------------
# узнавалка

def prepare():
    """подготовить данные"""

    global info, head
    info = []

    Portion = namedtuple('Portion', 'number name type capital population territory')

    for num, line in enumerate(data.strip().splitlines('\t')):
        if num == 0:
            head = line.strip().split()
        else:
            # ~ portion = Portion(*('number name type capital population territory' .split()))
            portion = Portion( *( line.strip().split('\t') ))
            info.append(portion)

    print(f"{info=}")
    

def discover():
    """совершить открытия"""

    print(data)

    # 1. что там есть? типы областей

    regions = set()

    for line in info:
        if line.type != 'нет':
            regions.add(line.type)

    print(f"{regions=}")

def main():
    """всё узнать и напечатать"""

    prepare()
    discover()

main()

# -------------------------------------------------
# результаты


# -------------------------------------------------
