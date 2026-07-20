#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-06-18 2026-06-18 1.0
# nz-regions.py

# ~ "дай список регионов Новой Зеландии"

# ~ Вот список всех 16 официальных регионов Новой Зеландии (11 управляются региональными советами, 5 — унитарными властями):
# ~ ## Остров Северный (North Island)

# ~ * Окленд (Auckland) — регион с крупнейшим городом страны, управляется унитарным советом.
# ~ * Нортленд (Northland) — самый северный регион Новой Зеландии.
# ~ * Уайкато (Waikato) — регион, известный своими сельскохозяйственными угодьями и пещерами Вайтомо.
# ~ * Бей-оф-Пленти (Bay of Plenty) — прибрежный регион на севере острова.
# ~ * Гисборн (Gisborne) — самый восточный регион, управляется унитарным советом.
# ~ * Хокс-Бей (Hawke's Bay) — регион на восточном побережье, знаменитый виноделием.
# ~ * Таранаки (Taranaki) — регион вокруг одноименного вулкана на западе.
# ~ * Манавату-Уангануи (Manawatu-Whanganui) — регион в южно-центральной части острова.
# ~ * Веллингтон (Wellington) — самый южный регион Северного острова, включающий столицу страны.

# ~ ## Остров Южный (South Island)

# ~ * Тасман (Tasman) — регион на северо-западе, управляется унитарным советом.
# ~ * Нельсон (Nelson) — небольшой регион-город на севере, управляется унитарным советом.
# ~ * Марлборо (Marlborough) — главный винодельческий регион на северо-востоке, управляется унитарным советом.
# ~ * Уэст-Кост (West Coast) — малонаселенный, дикий регион на западном побережье.
# ~ * Кентербери (Canterbury) — крупнейший по площади регион страны с центром в Крайстчерче.
# ~ * Отаго (Otago) — регион на юге, известный городами Данидин и Куинстаун.
# ~ * Саутленд (Southland) — самый южный регион страны, включающий нацпарк Фьордленд.

# ~ "выведи это же  формате json, с указанием имени региона, острова, столицы, а также населения региона 100 лет назад и сейчас, и населения столицы 100 лет назад и сейчас"

# ~ Примечание: Поскольку современное административное деление Новой Зеландии на регионы окончательно оформилось только в 1989 году, исторические данные за 1926 год (ровно 100 лет назад относительно 2026 года) приведены на основе границ тогдашних провинциальных округов (Provincial Districts) и муниципальных переписей (Borough/Urban Area censuses). Все современные показатели приведены на основе официальной государственной статистики.

regions = [
    {
      "name": "Окленд (Auckland)",
      "island": "Северный",
      "capital": "Окленд",
      "region_population_100_years_ago": 210000,
      "region_population_now": 1816000,
      "capital_population_100_years_ago": 88000,
      "capital_population_now": 1530000
    },
    {
      "name": "Веллингтон (Wellington)",
      "island": "Северный",
      "capital": "Веллингтон",
      "region_population_100_years_ago": 130000,
      "region_population_now": 543400,
      "capital_population_100_years_ago": 98000,
      "capital_population_now": 435000
    },
    {
      "name": "Кентербери (Canterbury)",
      "island": "Южный",
      "capital": "Крайстчерч",
      "region_population_100_years_ago": 215000,
      "region_population_now": 680000,
      "capital_population_100_years_ago": 118000,
      "capital_population_now": 395000
    },
    {
      "name": "Уайкато (Waikato)",
      "island": "Северный",
      "capital": "Гамильтон",
      "region_population_100_years_ago": 110000,
      "region_population_now": 532100,
      "capital_population_100_years_ago": 140000,
      "capital_population_now": 185000
    },
    {
      "name": "Отаго (Otago)",
      "island": "Южный",
      "capital": "Данидин",
      "region_population_100_years_ago": 150000,
      "region_population_now": 255000,
      "capital_population_100_years_ago": 85000,
      "capital_population_now": 134000
    },
    {
      "name": "Бей-оф-Пленти (Bay of Plenty)",
      "island": "Северный",
      "capital": "Тауранга",
      "region_population_100_years_ago": 35000,
      "region_population_now": 354000,
      "capital_population_100_years_ago": 2500,
      "capital_population_now": 160000
    },
    {
      "name": "Нортленд (Northland)",
      "island": "Северный",
      "capital": "Вангареи",
      "region_population_100_years_ago": 58000,
      "region_population_now": 204000,
      "capital_population_100_years_ago": 5000,
      "capital_population_now": 45000
    },
    {
      "name": "Хокс-Бей (Hawke's Bay)",
      "island": "Северный",
      "capital": "Нейпир",
      "region_population_100_years_ago": 67000,
      "region_population_now": 184000,
      "capital_population_100_years_ago": 15000,
      "capital_population_now": 67000
    },
    {
      "name": "Манавату-Уангануи (Manawatu-Whanganui)",
      "island": "Северный",
      "capital": "Палмерстон-Норт",
      "region_population_100_years_ago": 115000,
      "region_population_now": 260000,
      "capital_population_100_years_ago": 19000,
      "capital_population_now": 90000
    },
    {
      "name": "Таранаки (Taranaki)",
      "island": "Северный",
      "capital": "Нью-Плимут",
      "region_population_100_years_ago": 69000,
      "region_population_now": 130300,
      "capital_population_100_years_ago": 12000,
      "capital_population_now": 59000
    },
    {
      "name": "Саутленд (Southland)",
      "island": "Южный",
      "capital": "Инверкаргилл",
      "region_population_100_years_ago": 64000,
      "region_population_now": 105000,
      "capital_population_100_years_ago": 22000,
      "capital_population_now": 50000
    },
    {
      "name": "Гисборн (Gisborne)",
      "island": "Северный",
      "capital": "Гисборн",
      "region_population_100_years_ago": 25000,
      "region_population_now": 53000,
      "capital_population_100_years_ago": 12000,
      "capital_population_now": 38000
    },
    {
      "name": "Тасман (Tasman)",
      "island": "Южный",
      "capital": "Ричмонд",
      "region_population_100_years_ago": 21000,
      "region_population_now": 59900,
      "capital_population_100_years_ago": 1100,
      "capital_population_now": 18000
    },
    {
      "name": "Нельсон (Nelson)",
      "island": "Южный",
      "capital": "Нельсон",
      "region_population_100_years_ago": 11000,
      "region_population_now": 55000,
      "capital_population_100_years_ago": 11000,
      "capital_population_now": 55000
    },
    {
      "name": "Марлборо (Marlborough)",
      "island": "Южный",
      "capital": "Бленем",
      "region_population_100_years_ago": 18000,
      "region_population_now": 52000,
      "capital_population_100_years_ago": 5000,
      "capital_population_now": 29000
    },
    {
      "name": "Уэст-Кост (West Coast)",
      "island": "Южный",
      "capital": "Греймут",
      "region_population_100_years_ago": 15000,
      "region_population_now": 33000,
      "capital_population_100_years_ago": 4000,
      "capital_population_now": 10000
    }
  ]

# -------------------------------------------------
# рассчитать, какой город и какой регион наиболее выросли за 100 лет
# -------------------------------------------------

max_city_name = ''
max_city_times = 0.

max_region_name = ''
max_region_times = 0.

for x in regions:
    
    times_region = x['region_population_now'] / x['region_population_100_years_ago']
    if times_region > max_region_times:
        max_region_name = x['name']
        max_region_times = times_region
        
    times_city = x['capital_population_now'] / x['capital_population_100_years_ago']
    if times_city > max_city_times:
        max_city_name = x['capital']
        max_city_times = times_city
        

print(f"""
всё рассчитано:
самый выросший регион: {max_region_name} вырос в {max_region_times:.2f} раз(а),
самый выросший город:  {max_city_name} вырос в {max_city_times:.2f} раз(а).
""")

# ------------------------------- результат ---------------------------

# ~ всё рассчитано:
# ~ самый выросший регион: Бей-оф-Пленти (Bay of Plenty) вырос в 10.11 раз(а),
# ~ самый выросший город:  Тауранга вырос в 64.00 раз(а).

# ------------------------------- конец ---------------------------
