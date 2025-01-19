#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-01-19 2025-01-20 1.3
# australia.py

# ~ Есть информация об Австралии.
# ~ Узнать, где больше территория, где население,
# ~ сколько там чего (штатов, территорий).

# ~ Учебное: отрабатываем именованные кортежи.

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
            head = Portion( *( line.strip().split('\t') ))
        else:
            portion = Portion( *( line.strip().split('\t') ))
            info.append(portion)

    # ~ print(f"{head=}")
    # ~ print(f"{info=}")
    

def discover():
    """совершить открытия"""

    print(data)

    # 1. что там есть? типы областей

    regions = set()

    for line in info:
        if line.type != 'нет':
            regions.add(line.type)

    print(f"\n{regions=}")

    # 2. у кого самая большая территория?

    max_terr = list( filter(
        lambda x: x.territory ==
        max( line.territory for line in info if line.type in ('штат', 'территория')),
        info))[0]

    print(f"\nДанные: {max_terr=}\nназвание области: {max_terr.name}")

    # 3. у кого самое большое население?

    max_pop = list( filter(
        lambda x: x.population ==
        max( line.population for line in info if line.type in ('штат', 'территория')),
        info))[0]

    print(f"\nДанные: {max_terr=}\nназвание области: {max_pop.name}")

    # 4. у кого самая большая плотность населения?

    max_density = max(info[:-1],
        key = lambda line: int(line.population) / int(line.territory))

    print(f"\nДанные: {max_density=}\nназвание области: {max_density.name}")

    print()

def main():
    """всё узнать и напечатать"""

    prepare()
    discover()

main()


# -------------------------------------------------
# результаты

# ~ №	Название	Тип адм. ед.	Столица	Население, чел. (2021)	Площадь, км²
# ~ 1	Австралийская столичная территория	территория	Канберра	454499	2358
# ~ 2	Виктория	штат	Мельбурн	6503491	227444
# ~ 3	Западная Австралия	штат	Перт	2660026	2527013
# ~ 4	Квинсленд	штат	Брисбен	5156138	1729742
# ~ 5	Новый Южный Уэльс	штат	Сидней	8072163	801150
# ~ 6	Северная территория	территория	Дарвин	232605	1347791
# ~ 7	Тасмания	штат	Хобарт	557571	68401
# ~ 8	Южная Австралия	штат	Аделаида	1781516	984321
# ~ 0	Всего	нет	нет	25422788	7688220

# ~ regions={'территория', 'штат'}

# ~ Данные: max_terr=Portion(number='8', name='Южная Австралия', type='штат', capital='Аделаида', population='1781516', territory='984321')
# ~ название области: Южная Австралия

# ~ Данные: max_terr=Portion(number='8', name='Южная Австралия', type='штат', capital='Аделаида', population='1781516', territory='984321')
# ~ название области: Новый Южный Уэльс

# ~ Данные: max_density=Portion(number='1', name='Австралийская столичная территория', type='территория', capital='Канберра', population='454499', territory='2358')
# ~ название области: Австралийская столичная территория

# -------------------------------------------------
