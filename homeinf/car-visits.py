#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-05-05 2026-05-05 1.0
# car-visits.py

# ~ Машина, которая всё проехала

# ~ Есть список городов и номеров машин, которые в них были замечены.
# ~ Показать машины, которые были во всех городах 
# ~ (по номерам в алфавитном порядке),
# ~ или сказать, что таких машин не было.

from pprint import pprint
from random import choice, shuffle, randint

letter = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЭЮЯ"
digit  = "0123456789"

cities = """Москва Ярославль Орёл"""

# ~ cities = """Москва Ярославль Орёл
# ~ Самара Уфа Ижевск Киров Смоленск Тула Белгород Волгоград
# ~ Саратов Череповец Вологда Петрозаводск Мурманск Липецк Курск Брянск Пенза Омск Новосибирск Тюмень Курган Магнотогорск Ижевск Казань Томск Ишим Кемерово Братск Иркустк Красноярск Чита"""


def make() -> str:
    """сделать случайный номер"""

    return (
        choice(letter) +
        choice(digit) +
        choice(digit) +
        choice(digit) +
        choice(letter) +
        # ~ choice(letter) +
        choice(letter)
        )

def populate() -> None:
    """заполнить данными"""

    global cities, cars, nabor

    cities = cities.strip().split()
    shuffle(cities)
    print("cities:", cities)

    cars = [ make() for _ in range(len(cities) * 2)]
    # ~ print("cars:", *cars, sep=", ")

    nabor = []
    cxie = choice(cars)
    print("cxie:", cxie)

    for city in cities:
        nabor.append(( city, set([ choice(cars) for _ in range(len(cars) // 2) ] + [cxie] )))

    print("nabor:")
    pprint(nabor, width=80)


def solve() -> None:
    """найти общие машины"""

    global cities, cars, nabor

    best = set(cars)
    print("init:", best)

    for city in nabor:
        best &= city[1]
        # ~ print("best after", city, "=", best)

    print("best:", best)
    

def main():
    """запуск"""

    populate()
    solve()
    
        
main()


# ~ cities: ['Орёл', 'Москва', 'Ярославль']
# ~ cxie: В031ШУ
# ~ nabor:
# ~ [('Орёл', {'Т387ПФ', 'В031ШУ', 'Т735ЦА', 'Г176ЙХ'}),
 # ~ ('Москва', {'Т387ПФ', 'В031ШУ', 'Г176ЙХ'}),
 # ~ ('Ярославль', {'Т387ПФ', 'В031ШУ'})]
# ~ init: {'Н188ЛЭ', 'Т387ПФ', 'В031ШУ', 'С410ГЖ', 'Т735ЦА', 'Г176ЙХ'}
# ~ best: {'Т387ПФ', 'В031ШУ'}
