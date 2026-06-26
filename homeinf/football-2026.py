#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# football-2026.py
# 2026-06-27 2026-06-27 0.1

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
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Австрия",
    "debut": 1934,
    "times": 8,
    "best": "3-е место",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 1
    }
  },
  {
    "country": "Алжир",
    "debut": 1982,
    "times": 5,
    "best": "1/8 финала",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Аргентина",
    "debut": 1930,
    "times": 19,
    "best": "Чемпион",
    "medals": {
      "gold": 3,
      "silver": 3,
      "bronze": 0
    }
  },
  {
    "country": "Бельгия",
    "debut": 1930,
    "times": 15,
    "best": "3-е место",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 1
    }
  },
  {
    "country": "Босния и Герцеговина",
    "debut": 2014,
    "times": 2,
    "best": "Групповой этап",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Бразилия",
    "debut": 1930,
    "times": 23,
    "best": "Чемпион",
    "medals": {
      "gold": 5,
      "silver": 2,
      "bronze": 2
    }
  },
  {
    "country": "Гана",
    "debut": 2006,
    "times": 5,
    "best": "1/4 финала",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Германия",
    "debut": 1934,
    "times": 21,
    "best": "Чемпион",
    "medals": {
      "gold": 4,
      "silver": 4,
      "bronze": 4
    }
  },
  {
    "country": "ДР Конго",
    "debut": 1974,
    "times": 2,
    "best": "Групповой этап",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Египет",
    "debut": 1934,
    "times": 4,
    "best": "Групповой этап",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Ирак",
    "debut": 1986,
    "times": 2,
    "best": "Групповой этап",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Иран",
    "debut": 1978,
    "times": 7,
    "best": "Групповой этап",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Испания",
    "debut": 1934,
    "times": 17,
    "best": "Чемпион",
    "medals": {
      "gold": 1,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Италия",
    "debut": 1934,
    "times": 18,
    "best": "Чемпион",
    "medals": {
      "gold": 4,
      "silver": 2,
      "bronze": 1
    }
  },
  {
    "country": "Иордания",
    "debut": 2026,
    "times": 1,
    "best": "Дебют",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Кабо-Верде",
    "debut": 2026,
    "times": 1,
    "best": "Дебют",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Канада",
    "debut": 1986,
    "times": 3,
    "best": "Групповой этап",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Катар",
    "debut": 2022,
    "times": 2,
    "best": "Групповой этап",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Колумбия",
    "debut": 1962,
    "times": 7,
    "best": "1/4 финала",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Кот-д'Ивуар",
    "debut": 2006,
    "times": 4,
    "best": "Групповой этап",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Корея",
    "debut": 1954,
    "times": 12,
    "best": "4-е место",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Коста-Рика",
    "debut": 1990,
    "times": 6,
    "best": "1/4 финала",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Кот-д'Ивуар",
    "debut": 2006,
    "times": 4,
    "best": "Групповой этап",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Кюрасао",
    "debut": 2026,
    "times": 1,
    "best": "Дебют",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Марокко",
    "debut": 1970,
    "times": 7,
    "best": "4-е место",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Мексика",
    "debut": 1930,
    "times": 18,
    "best": "1/4 финала",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Нидерланды",
    "debut": 1934,
    "times": 12,
    "best": "2-е место",
    "medals": {
      "gold": 0,
      "silver": 3,
      "bronze": 1
    }
  },
  {
    "country": "Новая Зеландия",
    "debut": 1982,
    "times": 3,
    "best": "Групповой этап",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Норвегия",
    "debut": 1938,
    "times": 4,
    "best": "1/8 финала",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Панама",
    "debut": 2018,
    "times": 2,
    "best": "Групповой этап",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Парагвай",
    "debut": 1930,
    "times": 9,
    "best": "1/4 финала",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Перу",
    "debut": 1930,
    "times": 5,
    "best": "1/4 финала",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Португалия",
    "debut": 1966,
    "times": 9,
    "best": "3-е место",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 1
    }
  },
  {
    "country": "Саудовская Аравия",
    "debut": 1994,
    "times": 7,
    "best": "1/8 финала",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Сенегал",
    "debut": 2002,
    "times": 4,
    "best": "1/4 финала",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "США",
    "debut": 1930,
    "times": 12,
    "best": "3-е место",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 1
    }
  },
  {
    "country": "Тунис",
    "debut": 1978,
    "times": 7,
    "best": "Групповой этап",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Турция",
    "debut": 1954,
    "times": 3,
    "best": "3-е место",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 1
    }
  },
  {
    "country": "Узбекистан",
    "debut": 2026,
    "times": 1,
    "best": "Дебют",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Уругвай",
    "debut": 1930,
    "times": 15,
    "best": "Чемпион",
    "medals": {
      "gold": 2,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Франция",
    "debut": 1930,
    "times": 17,
    "best": "Чемпион",
    "medals": {
      "gold": 2,
      "silver": 2,
      "bronze": 2
    }
  },
  {
    "country": "Хорватия",
    "debut": 1998,
    "times": 7,
    "best": "2-е место",
    "medals": {
      "gold": 0,
      "silver": 1,
      "bronze": 2
    }
  },
  {
    "country": "Чехия",
    "debut": 1934,
    "times": 10,
    "best": "2-е место",
    "medals": {
      "gold": 0,
      "silver": 2,
      "bronze": 0
    }
  },
  {
    "country": "Швейцария",
    "debut": 1934,
    "times": 13,
    "best": "1/4 финала",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Швеция",
    "debut": 1934,
    "times": 13,
    "best": "2-е место",
    "medals": {
      "gold": 0,
      "silver": 1,
      "bronze": 2
    }
  },
  {
    "country": "Шотландия",
    "debut": 1954,
    "times": 9,
    "best": "Групповой этап",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Эквадор",
    "debut": 2002,
    "times": 5,
    "best": "1/8 финала",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "ЮАР",
    "debut": 1998,
    "times": 4,
    "best": "Групповой этап",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  },
  {
    "country": "Япония",
    "debut": 1998,
    "times": 8,
    "best": "1/8 финала",
    "medals": {
      "gold": 0,
      "silver": 0,
      "bronze": 0
    }
  }
]

# -------------------------- подготовка -------------------------

from pprint import pprint

# -------------------------- расчёт -------------------------

print("\n1. сколько всего команд?")

print("их всего:", len(data))

# ~ 1. сколько всего команд?
# ~ их всего: 50

# -------------------------- примечания -------------------------

# ~ Примечание: Статистика количества участий (times) приведена с учётом турнира 2026 года. Для Чехии (ранее Чехословакии) и Германии (включая ФРГ) достижения и медали посчитаны по правилам исторического правопреемства сборных в реестрах FIFA.
# -------------------------- конец -------------------------
print()
