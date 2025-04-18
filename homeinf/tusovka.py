#!/usr/bin/env python

# Mikhail (myke) Kolodin
# 2025-01-17 2025-01-17 1.1
# tusovka.py

# ~ Где тусуемся?

# ~ Даны наборы типичных имён по разным странам
# ~ (имена могут быть более чем в одной стране, напр., "Михаил").
# ~ Дан список имён с тусовки.
# ~ Определить, в какой стране тусуемся.
# ~ Т.е. откуда большинство имён.

# ---------------------------------------------
# импорты и установки

from collections import Counter
from pprint import pprint

# ---------------------------------------------
# примеры

str_lands = """
Россия Валера Димон Вован Витёк Вика Виктор Иван Ивашка Иванушка Тёма Яша Саша Александр Феликс Михаил
Сербия Михаил Драган Ратибор Деян Жарко Данка Милован Станко Леонид Сара
Англия Джон Джонни Дина Андрю Боб Бонни Вика Виктор Майк Ник Альберт Алекс Александр Арнольд Карл Денни Феликс Генри Ян Кит Мартин Нелл Томас
Израиль Яша Бени Мойша Изя Аарон Авдей Залман Захария Натан Наум Семён Сеня Савва Ян Осип Иосиф Иса Иуда Сара
Япония Акайо Акихиро Арису Горо Торо Макото Майко Кэтсу Ми Йошито
Китай Ли Си Гуй Ин Ксиу Дзен Бэй Лань Йи Да Джинг Канг Цю Фу Ню Ся Чао
"""

str_tustus = """
Яша Толик Чико Вика Да Майко Сара Михаил
Канг Цю Яша Фу Дзен
Томми Томас Авдей Бэй Джонни Ник Карл
Йошито Торо Поро Коро Наро Фаро Горо Арису Торо Алекс Ян Си Ми Фа Соль Эйнштейн
"""

# ---------------------------------------------
# программа

def prepare():
    """подготовка данных, перевод в рабочий формат"""

    global lands, tustus

    lands = {}

    for land in str_lands.strip().splitlines():
        landname, *names = land.strip().split()
        lands[landname] = names

    tustus = str_tustus.strip().splitlines()

    print("----------------------------------------------")
    print("страны: ")
    pprint(lands, width=120)
    print("\nтусовки:")
    pprint(tustus, width=120)
    print("----------------------------------------------")
    
# ---------------------------------------------
# тестирование

def detect(test):
    """определить страну"""

    cnt = Counter()

    for name in test.strip().split():
        for country in lands:
            if name in lands[country]:
                cnt[country] += 1

    cmc = cnt.most_common(1)

    return cmc[0][0]
    
# ----------------------------------------------

def testone(num, test):
    """тестирование одного текста"""

    print(f"""
сходка:    {num}
тусовщики: {test}
страна:    {detect(test)}""")

# ----------------------------------------------

def tests():
    """тестирование всех текстов"""

    for num, test in enumerate(tustus, 1):
        testone(num, test)

prepare()
tests()

# ---------------------------------------------
# результаты

# ~ сходка:    1
# ~ тусовщики: Яша Толик Чико Вика Да Майко Сара Михаил
# ~ страна:    Россия

# ~ сходка:    2
# ~ тусовщики: Канг Цю Яша Фу Дзен
# ~ страна:    Китай

# ~ сходка:    3
# ~ тусовщики: Томми Томас Авдей Бэй Джонни Ник Карл
# ~ страна:    Англия

# ~ сходка:    4
# ~ тусовщики: Йошито Торо Поро Коро Наро Фаро Горо Арису Торо Алекс Ян Си Ми Фа Соль Эйнштейн
# ~ страна:    Япония

# ---------------------------------------------
