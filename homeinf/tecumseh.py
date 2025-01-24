#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-01-19 2025-01-24 2.5
# tecumseh.py

# ---------------------------------------------
# исходные данные

info = """
Избран	Имя	Срок	Причина смерти	Дата смерти
1840	Уильям Гаррисон	первый	умер от воспаления лёгких	4 апреля 1841
1860	Авраам Линкольн	второй	убит (пулевое ранение головы), когда уже был переизбран на второй срок в 1864 году	15 апреля 1865
1880	Джеймс Гарфилд	первый	убит (пулевое ранение + халатность врачей, умер через три месяца после покушения)	19 сентября 1881
1900	Уильям Мак-Кинли	второй	убит (пулевое ранение + гангрена, умер через неделю после покушения)	14 сентября 1901
1920	Уоррен Гардинг	первый	умер от сердечного приступа или инсульта (неясно)	2 августа 1923
1940	Франклин Рузвельт	четвёртый	умер от кровоизлияния в мозг, когда был переизбран на четвёртый срок в 1944 году	12 апреля 1945
1960	Джон Кеннеди	первый	убит (пулевое ранение головы)	22 ноября 1963
1980	Рональд Рейган	первый	было неудачное покушение. Умер через пятнадцать лет после ухода с должности от болезни Альцгеймера	5 июня 2004
2000	Джордж Уокер Буш	второй	в первый срок его жизни ничего не угрожало. На втором сроке было неудачное покушение.	жив
2020	Джо Байден	первый		жив"""

# ~ Проклятие Текумсе (англ. Tecumseh’s curse), известно также как проклятие президентов США, президентское проклятие — легенда о проклятии, некогда произнесённом умирающим индейским вождём племени шауни Текумсе за нарушение белыми договора. Проклятие заключается в том, что каждый американский президент, избранный в год, без остатка делящийся на 20, умрёт или будет убит до окончания срока президентских полномочий.
# ~ https://www.youtube.com/shorts/ZxS9hvTVhdk

# ---------------------------------------------
# импорты и установки

# ~ from pprint import pprint

# ---------------------------------------------
# программа

# ~ 0. подготовка данных

def prepare():
    """подготовка
    """

    global data
    # ~ global data, headers

    data = []

    for num, line in enumerate(info.strip().splitlines()):
        if num:
            data.append(line.strip().split('\t'))

    # ~ for num, line in enumerate(info.strip().splitlines()):
        # ~ if num == 0:
            # ~ headers = line.strip().split('\t')
        # ~ else:
            # ~ data.append(line.strip().split('\t'))

    # ~ for line in (info.strip().splitlines():
        # ~ data.append(line.strip().split('\t'))
    # ~ data = data[1:]
            
# ---------------------------------------------
# ~ 1. разобрать даты инаугураций по векам

def say_when():
    """показать, в какие годы в какие века происходили инаугурации.
    00е годы относим к след. веку, поскольку инаугурация и срок идёт с января.
    """

    # ~ pprint(data)

    print("\nКогда случилось?\n")
    
    cent = 0
    for d in data:
        if (cnew := d[0][:2]) != cent:
            cent = cnew
            print(f"век: {int(cent)+1}")
        print(f"\tгод: {d[0]}")

# ---------------------------------------------
# ~ 2. показать результаты и причины смертей

def say_why():
    """показать, почему умер или выжил
    """

    print("\nЧто случилось?\n")
    reasons = "неудачное покушение,убит,умер".split(',')

    for d in data:
        for reason in reasons:
            if reason in d[3].lower():
                print(f"в {d[0]} избран президент {d[1]}, результат: {reason}")
                break

    print()

# ---------------------------------------------
# тестирование

prepare()
say_when()
say_why()

# ---------------------------------------------
# результаты

# ~ Когда случилось?

# ~ век: 19
	# ~ год: 1840
	# ~ год: 1860
	# ~ год: 1880
# ~ век: 20
	# ~ год: 1900
	# ~ год: 1920
	# ~ год: 1940
	# ~ год: 1960
	# ~ год: 1980
# ~ век: 21
	# ~ год: 2000
	# ~ год: 2020

# ~ Что случилось?

# ~ в 1840 избран президент Уильям Гаррисон, результат: умер
# ~ в 1860 избран президент Авраам Линкольн, результат: убит
# ~ в 1880 избран президент Джеймс Гарфилд, результат: убит
# ~ в 1900 избран президент Уильям Мак-Кинли, результат: убит
# ~ в 1920 избран президент Уоррен Гардинг, результат: умер
# ~ в 1940 избран президент Франклин Рузвельт, результат: умер
# ~ в 1960 избран президент Джон Кеннеди, результат: убит
# ~ в 1980 избран президент Рональд Рейган, результат: неудачное покушение
# ~ в 2000 избран президент Джордж Уокер Буш, результат: неудачное покушение

# ---------------------------------------------

# ~ См. https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D0%BA%D0%BB%D1%8F%D1%82%D0%B8%D0%B5_%D0%A2%D0%B5%D0%BA%D1%83%D0%BC%D1%81%D0%B5

# ---------------------------------------------
