#!/usr/bin/env python
# myke 2022-05-07 2022-05-10 1.1
# rus_rock.py

from rus_rock_data import *
from pprint import pp
import datetime

print("\nТема: Русский рок\n")

now = datetime.date.today().year
print("ныне год", now, "\n")

def prepare():
    """подготовить данные"""
    rock = []
    for group in rock_text.strip().split("\n"):
        since, till, name = group.split(" ", 2)
        since = int(since)
        if till == "пнв":
            till = int(now)
        else:
            till = int(till)
        rock.append([since, till, name])
    return rock

rock = prepare()
rock.sort()
pp(rock)

# ~ Тема: Русский рок

# ~ ныне год 2022 

# ~ [[1961, 2022, 'Удачное приобретение'],
 # ~ [1962, 1969, 'Интеграл'],
 # ~ [1964, 1966, 'Славяне'],
 # ~ [1964, 1969, 'Сокол'],
 # ~ [1966, 1979, 'Скоморохи'],
 # ~ [1966, 1984, 'Мифы'],
 # ~ [1969, 1990, 'Мозаика'],
 # ~ [1969, 1992, 'Диалог'],
 # ~ [1969, 2022, 'Машина времени'],
 # ~ [1969, 2022, 'Санкт-Петербург'],
 # ~ [1972, 2022, 'Аквариум'],
 # ~ [1977, 1991, 'Магнетик бэнд'],
 # ~ [1978, 2022, 'АукцЫон'],
 # ~ [1978, 2022, 'Земляне'],
 # ~ [1978, 2022, 'Пикник'],
 # ~ [1979, 1990, 'Автограф'],
 # ~ [1979, 2022, 'Воскресение'],
 # ~ [1979, 2022, 'Чёрный Кофе'],
 # ~ [1980, 1991, 'Урфин Джюс'],
 # ~ [1980, 2022, 'ДДТ'],
 # ~ [1980, 2022, 'Круиз'],
 # ~ [1980, 2022, 'Центр'],
 # ~ [1981, 1991, 'Зоопарк'],
 # ~ [1981, 1991, 'Кино'],
 # ~ [1982, 1997, 'Наутилус Помпилиус'],
 # ~ [1983, 1996, 'Секрет'],
 # ~ [1983, 2021, 'Звуки Му'],
 # ~ [1983, 2022, 'Алиса'],
 # ~ [1983, 2022, 'Браво'],
 # ~ [1983, 2022, 'Крематорий'],
 # ~ [1983, 2022, 'Несчастный случай'],
 # ~ [1984, 1991, 'Карнавал'],
 # ~ [1984, 2020, 'Гражданская оборона'],
 # ~ [1984, 2022, 'Коррозия металла'],
 # ~ [1984, 2022, 'Телевизор'],
 # ~ [1985, 2022, 'Ария'],
 # ~ [1985, 2022, 'Бригада С'],
 # ~ [1985, 2022, 'Ноль'],
 # ~ [1985, 2022, 'Чайф'],
 # ~ [1986, 2022, 'Вопли Видоплясова'],
 # ~ [1986, 2022, 'Калинов мост'],
 # ~ [1987, 2000, 'Сектор Газа'],
 # ~ [1987, 2010, 'Агата Кристи'],
 # ~ [1988, 2022, 'Би-2'],
 # ~ [1988, 2022, 'Ва-Банкъ'],
 # ~ [1988, 2022, 'Иван Кайф'],
 # ~ [1988, 2022, 'Ногу свело!'],
 # ~ [1993, 2022, 'Чиж и Ко'],
 # ~ [1995, 2022, 'Умка и Броневик'],
 # ~ [1998, 2022, 'Земфира'],
 # ~ [1999, 2022, 'Мельница']]


def count_duration():
    """посчитать длительность активности"""
    for group in rock:
        group.append(group[1] - group[0])

count_duration()

pp(sorted(rock, key=lambda x: x[3], reverse=True))

# ~ [[1961, 2022, 'Удачное приобретение', 61],
 # ~ [1969, 2022, 'Машина времени', 53],
 # ~ [1969, 2022, 'Санкт-Петербург', 53],
 # ~ [1972, 2022, 'Аквариум', 50],
 # ~ [1978, 2022, 'АукцЫон', 44],
 # ~ [1978, 2022, 'Земляне', 44],
 # ~ [1978, 2022, 'Пикник', 44],
 # ~ [1979, 2022, 'Воскресение', 43],
 # ~ [1979, 2022, 'Чёрный Кофе', 43],
 # ~ [1980, 2022, 'ДДТ', 42],
 # ~ [1980, 2022, 'Круиз', 42],
 # ~ [1980, 2022, 'Центр', 42],
 # ~ [1983, 2022, 'Алиса', 39],
 # ~ [1983, 2022, 'Браво', 39],
 # ~ [1983, 2022, 'Крематорий', 39],
 # ~ [1983, 2022, 'Несчастный случай', 39],
 # ~ [1983, 2021, 'Звуки Му', 38],
 # ~ [1984, 2022, 'Коррозия металла', 38],
 # ~ [1984, 2022, 'Телевизор', 38],
 # ~ [1985, 2022, 'Ария', 37],
 # ~ [1985, 2022, 'Бригада С', 37],
 # ~ [1985, 2022, 'Ноль', 37],
 # ~ [1985, 2022, 'Чайф', 37],
 # ~ [1984, 2020, 'Гражданская оборона', 36],
 # ~ [1986, 2022, 'Вопли Видоплясова', 36],
 # ~ [1986, 2022, 'Калинов мост', 36],
 # ~ [1988, 2022, 'Би-2', 34],
 # ~ [1988, 2022, 'Ва-Банкъ', 34],
 # ~ [1988, 2022, 'Иван Кайф', 34],
 # ~ [1988, 2022, 'Ногу свело!', 34],
 # ~ [1993, 2022, 'Чиж и Ко', 29],
 # ~ [1995, 2022, 'Умка и Броневик', 27],
 # ~ [1998, 2022, 'Земфира', 24],
 # ~ [1969, 1992, 'Диалог', 23],
 # ~ [1987, 2010, 'Агата Кристи', 23],
 # ~ [1999, 2022, 'Мельница', 23],
 # ~ [1969, 1990, 'Мозаика', 21],
 # ~ [1966, 1984, 'Мифы', 18],
 # ~ [1982, 1997, 'Наутилус Помпилиус', 15],
 # ~ [1977, 1991, 'Магнетик бэнд', 14],
 # ~ [1966, 1979, 'Скоморохи', 13],
 # ~ [1983, 1996, 'Секрет', 13],
 # ~ [1987, 2000, 'Сектор Газа', 13],
 # ~ [1979, 1990, 'Автограф', 11],
 # ~ [1980, 1991, 'Урфин Джюс', 11],
 # ~ [1981, 1991, 'Зоопарк', 10],
 # ~ [1981, 1991, 'Кино', 10],
 # ~ [1962, 1969, 'Интеграл', 7],
 # ~ [1984, 1991, 'Карнавал', 7],
 # ~ [1964, 1969, 'Сокол', 5],
 # ~ [1964, 1966, 'Славяне', 2]]


# показать список по алфавиту

pp(sorted(rock, key=lambda x: x[2]))

# ~ [[1979, 1990, 'Автограф', 11],
 # ~ [1987, 2010, 'Агата Кристи', 23],
 # ~ [1972, 2022, 'Аквариум', 50],
 # ~ [1983, 2022, 'Алиса', 39],
 # ~ [1985, 2022, 'Ария', 37],
 # ~ [1978, 2022, 'АукцЫон', 44],
 # ~ [1988, 2022, 'Би-2', 34],
 # ~ [1983, 2022, 'Браво', 39],
 # ~ [1985, 2022, 'Бригада С', 37],
 # ~ [1988, 2022, 'Ва-Банкъ', 34],
 # ~ [1986, 2022, 'Вопли Видоплясова', 36],
 # ~ [1979, 2022, 'Воскресение', 43],
 # ~ [1984, 2020, 'Гражданская оборона', 36],
 # ~ [1980, 2022, 'ДДТ', 42],
 # ~ [1969, 1992, 'Диалог', 23],
 # ~ [1983, 2021, 'Звуки Му', 38],
 # ~ [1978, 2022, 'Земляне', 44],
 # ~ [1998, 2022, 'Земфира', 24],
 # ~ [1981, 1991, 'Зоопарк', 10],
 # ~ [1988, 2022, 'Иван Кайф', 34],
 # ~ [1962, 1969, 'Интеграл', 7],
 # ~ [1986, 2022, 'Калинов мост', 36],
 # ~ [1984, 1991, 'Карнавал', 7],
 # ~ [1981, 1991, 'Кино', 10],
 # ~ [1984, 2022, 'Коррозия металла', 38],
 # ~ [1983, 2022, 'Крематорий', 39],
 # ~ [1980, 2022, 'Круиз', 42],
 # ~ [1977, 1991, 'Магнетик бэнд', 14],
 # ~ [1969, 2022, 'Машина времени', 53],
 # ~ [1999, 2022, 'Мельница', 23],
 # ~ [1966, 1984, 'Мифы', 18],
 # ~ [1969, 1990, 'Мозаика', 21],
 # ~ [1982, 1997, 'Наутилус Помпилиус', 15],
 # ~ [1983, 2022, 'Несчастный случай', 39],
 # ~ [1988, 2022, 'Ногу свело!', 34],
 # ~ [1985, 2022, 'Ноль', 37],
 # ~ [1978, 2022, 'Пикник', 44],
 # ~ [1969, 2022, 'Санкт-Петербург', 53],
 # ~ [1983, 1996, 'Секрет', 13],
 # ~ [1987, 2000, 'Сектор Газа', 13],
 # ~ [1966, 1979, 'Скоморохи', 13],
 # ~ [1964, 1966, 'Славяне', 2],
 # ~ [1964, 1969, 'Сокол', 5],
 # ~ [1984, 2022, 'Телевизор', 38],
 # ~ [1961, 2022, 'Удачное приобретение', 61],
 # ~ [1995, 2022, 'Умка и Броневик', 27],
 # ~ [1980, 1991, 'Урфин Джюс', 11],
 # ~ [1980, 2022, 'Центр', 42],
 # ~ [1985, 2022, 'Чайф', 37],
 # ~ [1993, 2022, 'Чиж и Ко', 29],
 # ~ [1979, 2022, 'Чёрный Кофе', 43]]
