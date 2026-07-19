#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# football-2026.py
# 2026-06-27 2026-07-20 1.1

# ~ ЧМФ-2026. по каждой стране, участвующей в чемпионате мира по футболу в 2026, укажи (list[json], все ключи по-англ., все значения по-русски):
# ~ - country: страна,
# ~ - debut: в каком году впервые участвовала,
# ~ - times: сколько раз участвовала,
# ~ - best: какое наивысшее место заняла,
# ~ - medals: медали: сколько золотых (gold), серебряных (silver), бронзовых (bronze) в сумме за все годы участия
# ~ счёт стран странный

# -------------------------- данные -------------------------

data = [
  {
    "country": "Австралия",
    "debut": 1974,
    "times": 7,
    "best": "1/8 финала",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Австрия",
    "debut": 1934,
    "times": 8,
    "best": "3-е место",
    "medals": { "gold": 0, "silver": 0, "bronze": 1 }
  },
  {
    "country": "Алжир",
    "debut": 1982,
    "times": 5,
    "best": "1/8 финала",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Англия",
    "debut": 1950,
    "times": 17,
    "best": "Чемпион",
    "medals": { "gold": 1, "silver": 0, "bronze": 1 }
  },
  {
    "country": "Аргентина",
    "debut": 1930,
    "times": 19,
    "best": "Чемпион",
    "medals": { "gold": 3, "silver": 4, "bronze": 0 }
  },
  {
    "country": "Бельгия",
    "debut": 1930,
    "times": 15,
    "best": "3-е место",
    "medals": { "gold": 0, "silver": 0, "bronze": 1 }
  },
  {
    "country": "Боливия",
    "debut": 1930,
    "times": 4,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Босния и Герцеговина",
    "debut": 2014,
    "times": 2,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Бразилия",
    "debut": 1930,
    "times": 23,
    "best": "Чемпион",
    "medals": { "gold": 5, "silver": 2, "bronze": 2 }
  },
  {
    "country": "Гана",
    "debut": 2006,
    "times": 5,
    "best": "1/4 финала",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Германия",
    "debut": 1934,
    "times": 21,
    "best": "Чемпион",
    "medals": { "gold": 4, "silver": 4, "bronze": 4 }
  },
  {
    "country": "ДР Конго",
    "debut": 1974,
    "times": 2,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Египет",
    "debut": 1934,
    "times": 4,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Иордания",
    "debut": 2026,
    "times": 1,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Ирак",
    "debut": 1986,
    "times": 2,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Иран",
    "debut": 1978,
    "times": 7,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Испания",
    "debut": 1934,
    "times": 17,
    "best": "Чемпион",
    "medals": { "gold": 2, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Кабо-Верде",
    "debut": 2026,
    "times": 1,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Канада",
    "debut": 1986,
    "times": 3,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Катар",
    "debut": 2022,
    "times": 2,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Колумбия",
    "debut": 1962,
    "times": 7,
    "best": "1/4 финала",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Кот-д’Ивуар",
    "debut": 2006,
    "times": 4,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Кюрасао",
    "debut": 2026,
    "times": 1,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Марокко",
    "debut": 1970,
    "times": 7,
    "best": "4-е место",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Мексика",
    "debut": 1930,
    "times": 18,
    "best": "1/4 финала",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Нидерланды",
    "debut": 1934,
    "times": 12,
    "best": "2-е место",
    "medals": { "gold": 0, "silver": 3, "bronze": 1 }
  },
  {
    "country": "Новая Зеландия",
    "debut": 1982,
    "times": 3,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Норвегия",
    "debut": 1938,
    "times": 4,
    "best": "1/8 финала",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Панама",
    "debut": 2018,
    "times": 2,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Парагвай",
    "debut": 1930,
    "times": 9,
    "best": "1/4 финала",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Португалия",
    "debut": 1966,
    "times": 9,
    "best": "3-е место",
    "medals": { "gold": 0, "silver": 0, "bronze": 1 }
  },
  {
    "country": "Саудовская Аравия",
    "debut": 1994,
    "times": 7,
    "best": "1/8 финала",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Сенегал",
    "debut": 2002,
    "times": 4,
    "best": "1/4 финала",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "США",
    "debut": 1930,
    "times": 12,
    "best": "3-е место",
    "medals": { "gold": 0, "silver": 0, "bronze": 1 }
  },
  {
    "country": "Тунис",
    "debut": 1978,
    "times": 7,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Турция",
    "debut": 1954,
    "times": 3,
    "best": "3-е место",
    "medals": { "gold": 0, "silver": 0, "bronze": 1 }
  },
  {
    "country": "Узбекистан",
    "debut": 2026,
    "times": 1,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Уругвай",
    "debut": 1930,
    "times": 15,
    "best": "Чемпион",
    "medals": { "gold": 2, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Франция",
    "debut": 1930,
    "times": 17,
    "best": "Чемпион",
    "medals": { "gold": 2, "silver": 2, "bronze": 2 }
  },
  {
    "country": "Хорватия",
    "debut": 1998,
    "times": 7,
    "best": "2-е место",
    "medals": { "gold": 0, "silver": 1, "bronze": 2 }
  },
  {
    "country": "Чехия",
    "debut": 1934,
    "times": 10,
    "best": "2-е место",
    "medals": { "gold": 0, "silver": 2, "bronze": 0 }
  },
  {
    "country": "Швейцария",
    "debut": 1934,
    "times": 13,
    "best": "1/4 финала",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Швеция",
    "debut": 1934,
    "times": 13,
    "best": "2-е место",
    "medals": { "gold": 0, "silver": 1, "bronze": 2 }
  },
  {
    "country": "Шотландия",
    "debut": 1954,
    "times": 9,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Эквадор",
    "debut": 2002,
    "times": 5,
    "best": "1/8 финала",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "ЮАР",
    "debut": 1998,
    "times": 4,
    "best": "Групповой этап",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Южная Корея",
    "debut": 1954,
    "times": 12,
    "best": "4-е место",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  },
  {
    "country": "Япония",
    "debut": 1998,
    "times": 8,
    "best": "1/8 финала",
    "medals": { "gold": 0, "silver": 0, "bronze": 0 }
  }
]

# -------------------------- подготовка -------------------------

from pprint import pprint

# -------------------------- расчёт -------------------------

# -----------------------------------------------------------
print("\n1. сколько всего команд?")

print("их всего:", len(data))

# ~ 1. сколько всего команд?
# ~ их всего: 48

# -----------------------------------------------------------
print("\n2. сколько новичков?")

print("их всего:", len([x for x in data if x['times'] == 1]))

# ~ 2. сколько новичков?
# ~ их всего: 4

# -----------------------------------------------------------
print("\n3. сколько раньше побеждали?")

print("их всего:", len([x for x in data if x['medals']['gold']]))

# ~ 3. сколько раньше побеждали?
# ~ их всего: 7

# -----------------------------------------------------------
print("\n4. сколько раньше были на пьедестале?")

print("их всего:", len([x for x in data if sum(x['medals'].values()) ]))

# ~ 4. сколько раньше были на пьедестале?
# ~ их всего: 16

# -----------------------------------------------------------
print("\n5. покажи всех победителей по заслугам")

sel = [ (tuple(c['medals'].values()), c['country']) for c in data if sum(c['medals'].values())]
# ~ sel.sort(key = lambda x: x[0])
sel.sort(reverse=True)

print(f"{'страна':15} : медали (З,С,Б)")
print("--------------------------------")
for c in sel:
    print(f"{c[1]:15} : {c[0]}")

# ~ 5. покажи всех победителей по заслугам
# ~ страна          : медали (З,С,Б)
# ~ --------------------------------
# ~ Бразилия        : (5, 2, 2)
# ~ Германия        : (4, 4, 4)
# ~ Аргентина       : (3, 3, 0)
# ~ Франция         : (2, 2, 2)
# ~ Уругвай         : (2, 0, 0)
# ~ Англия          : (1, 0, 1)
# ~ Испания         : (1, 0, 0)
# ~ Нидерланды      : (0, 3, 1)
# ~ Чехия           : (0, 2, 0)
# ~ Швеция          : (0, 1, 2)
# ~ Хорватия        : (0, 1, 2)
# ~ Турция          : (0, 0, 1)
# ~ США             : (0, 0, 1)
# ~ Португалия      : (0, 0, 1)
# ~ Бельгия         : (0, 0, 1)
# ~ Австрия         : (0, 0, 1)

# -------------------------- примечания -------------------------

# ~ Примечание: Статистика количества участий (times) приведена с учётом турнира 2026 года. Для Чехии (ранее Чехословакии) и Германии (включая ФРГ) достижения и медали посчитаны по правилам исторического правопреемства сборных в реестрах FIFA.
# -------------------------- конец -------------------------
print()
