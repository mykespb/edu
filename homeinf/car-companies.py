#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-06-18 2026-06-18 1.0
# car-companies.py

# ~ "дай список из не более чем 30 крупнейших фирм, производящих автомобили, укажи их название (name), тип (type) автомобилей, которые они производят (из набора: легковые, грузовые, спецтехника, военные), примерный оборот в USD (usd), основную страну регистрации (country); формат - json"

from pprint import pprint

companies = [
    {
      "name": "Volkswagen Group",
      "type": ["легковые", "грузовые", "спецтехника"],
      "usd": 318000000000,
      "country": "Германия"
    },
    {
      "name": "Toyota Motor Corporation",
      "type": ["легковые", "грузовые", "спецтехника", "военные"],
      "usd": 286000000000,
      "country": "Япония"
    },
    {
      "name": "Stellantis",
      "type": ["легковые", "грузовые", "спецтехника", "военные"],
      "usd": 200000000000,
      "country": "Нидерланды"
    },
    {
      "name": "General Motors",
      "type": ["легковые", "грузовые", "спецтехника", "военные"],
      "usd": 188000000000,
      "country": "США"
    },
    {
      "name": "Ford Motor Company",
      "type": ["легковые", "грузовые", "спецтехника", "военные"],
      "usd": 182000000000,
      "country": "США"
    },
    {
      "name": "Mercedes-Benz Group",
      "type": ["легковые", "грузовые", "спецтехника", "военные"],
      "usd": 161000000000,
      "country": "Германия"
    },
    {
      "name": "BMW Group",
      "type": ["легковые"],
      "usd": 158000000000,
      "country": "Германия"
    },
    {
      "name": "Honda Motor Co.",
      "type": ["легковые", "спецтехника"],
      "usd": 129000000000,
      "country": "Япония"
    },
    {
      "name": "Hyundai Motor Company",
      "type": ["легковые", "грузовые", "спецтехника", "военные"],
      "usd": 121000000000,
      "country": "Южная Корея"
    },
    {
      "name": "SAIC Motor",
      "type": ["легковые", "грузовые", "спецтехника"],
      "usd": 109000000000,
      "country": "Китай"
    },
    {
      "name": "BYD Auto",
      "type": ["легковые", "грузовые", "спецтехника"],
      "usd": 105000000000,
      "country": "Китай"
    },
    {
      "name": "Tesla, Inc.",
      "type": ["легковые", "грузовые"],
      "usd": 96000000000,
      "country": "США"
    },
    {
      "name": "Nissan Motor Co.",
      "type": ["легковые", "грузовые", "спецтехника"],
      "usd": 78000000000,
      "country": "Япония"
    },
    {
      "name": "Kia Corporation",
      "type": ["легковые", "грузовые", "военные"],
      "usd": 75000000000,
      "country": "Южная Корея"
    },
    {
      "name": "Geely Auto Holding",
      "type": ["легковые", "грузовые"],
      "usd": 70000000000,
      "country": "Китай"
    },
    {
      "name": "Renault Group",
      "type": ["легковые", "грузовые"],
      "usd": 57000000000,
      "country": "Франция"
    },
    {
      "name": "Tata Motors",
      "type": ["легковые", "грузовые", "спецтехника", "военные"],
      "usd": 53000000000,
      "country": "Индия"
    },
    {
      "name": "Maruti Suzuki",
      "type": ["легковые"],
      "usd": 17000000000,
      "country": "Индия"
    },
    {
      "name": "Mahindra & Mahindra",
      "type": ["легковые", "спецтехника", "военные"],
      "usd": 16000000000,
      "country": "Индия"
    },
    {
      "name": "Mazda Motor Corporation",
      "type": ["легковые"],
      "usd": 32000000000,
      "country": "Япония"
    },
    {
      "name": "Suzuki Motor Corporation",
      "type": ["легковые"],
      "usd": 35000000000,
      "country": "Япония"
    },
    {
      "name": "Subaru Corporation",
      "type": ["легковые", "военные"],
      "usd": 29000000000,
      "country": "Япония"
    },
    {
      "name": "Volvo Group (AB Volvo)",
      "type": ["грузовые", "спецтехника", "военные"],
      "usd": 52000000000,
      "country": "Швеция"
    },
    {
      "name": "Paccar (Kenworth, Peterbilt, DAF)",
      "type": ["грузовые", "спецтехника"],
      "usd": 35000000000,
      "country": "США"
    },
    {
      "name": "Traton Group (Scania, MAN)",
      "type": ["грузовые", "спецтехника", "военные"],
      "usd": 50000000000,
      "country": "Германия"
    },
    {
      "name": "Dongfeng Motor",
      "type": ["легковые", "грузовые", "спецтехника", "военные"],
      "usd": 15000000000,
      "country": "Китай"
    },
    {
      "name": "Isuzu Motors",
      "type": ["грузовые", "спецтехника"],
      "usd": 23000000000,
      "country": "Япония"
    },
    {
      "name": "Changan Automobile",
      "type": ["легковые", "грузовые"],
      "usd": 21000000000,
      "country": "Китай"
    },
    {
      "name": "GAC Group",
      "type": ["легковые"],
      "usd": 18000000000,
      "country": "Китай"
    },
    {
      "name": "Ferrari N.V.",
      "type": ["легковые"],
      "usd": 68000000000,
      "country": "Италия"
    }
  ]

# ------------------------ prepare -------------------------

def part(name):
    print(f"""
----------------------------------------------------------
{name}
----------------------------------------------------------
""")

def cprint(kv):
    for k, v in kv:
        print(f"{k:30} ({v})")

# ------------------------ мирные -------------------------

part("1. только мирные компании")

peaceful = [ (x['name'], x['country'])
    for x in companies
    if ('военные' not in x['type']) ]

cprint(peaceful)

# ------------------------ все типы -------------------------

part("2. кто выпускает все типы машин")

all_types = [ (x['name'], x['country'])
    for x in companies
    if len(x['type']) == 4 ]

cprint(all_types)

# ------------------------ азиатские -------------------------

part("3. все азиатские компании")

asian = [ (x['name'], x['country'])
    for x in companies
    if (x['country'] in "Китай,Япония,Индия,Южная Корея".strip(',') ) ]

cprint(asian)

# ------------------------ богатые -------------------------

part("4. богатые компании")

max_rich = max( [ x['usd'] for x in companies] )
simply_rich = max_rich * 0.8

richest = [ (x['name'], x['country'])
    for x in companies
    if (x['usd'] >= simply_rich) ]

cprint(richest)

# ------------------------ страны -------------------------

part("5. все представленные страны")

states = {
    x['country'] for x in companies
}
states = sorted(states)

print(*states, sep=", ")

# ------------------------ конец -------------------------

part("конец")

# --------------------------------------------------------
