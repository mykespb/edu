#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# football-2026.py
# 2026-06-27 2026-07-19 2.1

# ~ ЧМФ-2026. по каждой стране, участвующей в чемпионате мира по футболу в 2026, укажи (list[json], все ключи по-англ., все значения по-русски):
# ~ - country: страна,
# ~ - debut: в каком году впервые участвовала,
# ~ - times: сколько раз участвовала,
# ~ - best: какое наивысшее место заняла,
# ~ - medals: медали: сколько золотых (gold), серебряных (silver), бронзовых (bronze) в сумме за все годы участия

# -------------------------- данные -------------------------

data = [
  {
    "country": "Австралия",
    "debut": 1974,
    "times": 6,
    "best": "1/8 финала",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Австрия",
    "debut": 1934,
    "times": 8,
    "best": "3-е место",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": [1954]
    }
  },
  {
    "country": "Алжир",
    "debut": 1982,
    "times": 5,
    "best": "1/8 финала",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Англия",
    "debut": 1950,
    "times": 17,
    "best": "Чемпион",
    "medals": {
      "gold": [1966],
      "silver": [],
      "bronze": [2026]
    }
  },
  {
    "country": "Аргентина",
    "debut": 1930,
    "times": 19,
    "best": "Чемпион",
    "medals": {
      "gold": [1978, 1986, 2022],
      "silver": [1930, 1990, 2014],
      "bronze": []
    }
  },
  {
    "country": "Бельгия",
    "debut": 1930,
    "times": 15,
    "best": "3-е место",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": [2018]
    }
  },
  {
    "country": "Боливия",
    "debut": 1930,
    "times": 4,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Босния и Герцеговина",
    "debut": 2014,
    "times": 2,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Бразилия",
    "debut": 1930,
    "times": 23,
    "best": "Чемпион",
    "medals": {
      "gold": [1958, 1962, 1970, 1994, 2002],
      "silver": [1950, 1998],
      "bronze": [1938, 1978]
    }
  },
  {
    "country": "Гана",
    "debut": 2006,
    "times": 5,
    "best": "1/4 финала",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Германия",
    "debut": 1934,
    "times": 21,
    "best": "Чемпион",
    "medals": {
      "gold": [1954, 1974, 1990, 2014],
      "silver": [1966, 1982, 1986, 2002],
      "bronze": [1934, 1970, 2006, 2010]
    }
  },
  {
    "country": "ДР Конго",
    "debut": 1974,
    "times": 2,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Египет",
    "debut": 1934,
    "times": 4,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Иордания",
    "debut": 2026,
    "times": 1,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Ирак",
    "debut": 1986,
    "times": 2,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Иран",
    "debut": 1978,
    "times": 7,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Испания",
    "debut": 1934,
    "times": 17,
    "best": "Чемпион",
    "medals": {
      "gold": [2010],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Кабо-Верде",
    "debut": 2026,
    "times": 1,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Канада",
    "debut": 1986,
    "times": 3,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Катар",
    "debut": 2022,
    "times": 2,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Колумбия",
    "debut": 1962,
    "times": 7,
    "best": "1/4 финала",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Кот-д’Ивуар",
    "debut": 2006,
    "times": 4,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Кюрасао",
    "debut": 2026,
    "times": 1,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Марокко",
    "debut": 1970,
    "times": 7,
    "best": "4-е место",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Мексика",
    "debut": 1930,
    "times": 18,
    "best": "1/4 финала",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Нидерланды",
    "debut": 1934,
    "times": 12,
    "best": "2-е место",
    "medals": {
      "gold": [],
      "silver": [1974, 1978, 2010],
      "bronze": [2014]
    }
  },
  {
    "country": "Новая Зеландия",
    "debut": 1982,
    "times": 3,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Норвегия",
    "debut": 1938,
    "times": 4,
    "best": "1/8 финала",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Панама",
    "debut": 2018,
    "times": 2,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Парагвай",
    "debut": 1930,
    "times": 9,
    "best": "1/4 финала",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Португалия",
    "debut": 1966,
    "times": 9,
    "best": "3-е место",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": [1966]
    }
  },
  {
    "country": "Саудовская Аравия",
    "debut": 1994,
    "times": 7,
    "best": "1/8 финала",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Сенегал",
    "debut": 2002,
    "times": 4,
    "best": "1/4 финала",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "США",
    "debut": 1930,
    "times": 12,
    "best": "3-е место",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": [1930]
    }
  },
  {
    "country": "Тунис",
    "debut": 1978,
    "times": 7,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Турция",
    "debut": 1954,
    "times": 3,
    "best": "3-е место",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": [2002]
    }
  },
  {
    "country": "Узбекистан",
    "debut": 2026,
    "times": 1,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Уругвай",
    "debut": 1930,
    "times": 15,
    "best": "Чемпион",
    "medals": {
      "gold": [1930, 1950],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Франция",
    "debut": 1930,
    "times": 17,
    "best": "Чемпион",
    "medals": {
      "gold": [1998, 2018],
      "silver": [2006, 2022],
      "bronze": [1958, 1986]
    }
  },
  {
    "country": "Хорватия",
    "debut": 1998,
    "times": 7,
    "best": "2-е место",
    "medals": {
      "gold": [],
      "silver": [2018],
      "bronze": [1998, 2022]
    }
  },
  {
    "country": "Чехия",
    "debut": 1934,
    "times": 10,
    "best": "2-е место",
    "medals": {
      "gold": [],
      "silver": [1934, 1962],
      "bronze": []
    }
  },
  {
    "country": "Швейцария",
    "debut": 1934,
    "times": 13,
    "best": "1/4 финала",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Швеция",
    "debut": 1934,
    "times": 13,
    "best": "2-е место",
    "medals": {
      "gold": [],
      "silver": [1958],
      "bronze": [1950, 1994]
    }
  },
  {
    "country": "Шотландия",
    "debut": 1954,
    "times": 9,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Эквадор",
    "debut": 2002,
    "times": 5,
    "best": "1/8 финала",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "ЮАР",
    "debut": 1998,
    "times": 4,
    "best": "Групповой этап",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Южная Корея",
    "debut": 1954,
    "times": 12,
    "best": "4-е место",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
  },
  {
    "country": "Япония",
    "debut": 1998,
    "times": 8,
    "best": "1/8 финала",
    "medals": {
      "gold": [],
      "silver": [],
      "bronze": []
    }
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

print("их всего:",
    len([    # = sum :)
        1
        for k in data
    if
        len(k['medals']['gold'] + 
            k['medals']['silver'] + 
            k['medals']['bronze'])
    ]
    ))

# ~ 4. сколько раньше были на пьедестале?
# ~ их всего: 16

# -----------------------------------------------------------
print("\n5. покажи всех победителей по заслугам")

sel = [
    (
        (len(k['medals']['gold']),
            len(k['medals']['silver']),
            len(k['medals']['bronze'])),
        k['country']
    )
    for k in data
    if
        len(k['medals']['gold'] + 
            k['medals']['silver'] + 
            k['medals']['bronze'])
    ]

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
