#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-06-19 2026-06-23 1.1
# europe-over.py

# ~ дай список западноевропейских стран как list[dict], включающий поля:
# ~ name: название,
# ~ capital: столица,
# ~ area: территория страны (тыс. кв. км),
# ~ population: население страны (тыс. чел.)

# ~ задача. найди наименьший набор стран, в сумме дающий величину большую, чем все остальные в сумме,
# ~ а. по площади,
# ~ б. по населению.

europe: list[dict] = [
    {
        "name": "Австрия",
        "capital": "Вена",
        "area": 83.88,
        "population": 9100.0
    },
    {
        "name": "Албания",
        "capital": "Тирана",
        "area": 28.75,
        "population": 2760.0
    },
    {
        "name": "Андорра",
        "capital": "Андорра-ла-Велья",
        "area": 0.47,
        "population": 85.0
    },
    {
        "name": "Белоруссия",
        "capital": "Минск",
        "area": 207.60,
        "population": 9200.0
    },
    {
        "name": "Бельгия",
        "capital": "Брюссель",
        "area": 30.69,
        "population": 11800.0
    },
    {
        "name": "Болгария",
        "capital": "София",
        "area": 110.99,
        "population": 6400.0
    },
    {
        "name": "Босния и Герцеговина",
        "capital": "Сараево",
        "area": 51.21,
        "population": 3200.0
    },
    {
        "name": "Ватикан",
        "capital": "Ватикан",
        "area": 0.00049,
        "population": 0.8
    },
    {
        "name": "Великобритания",
        "capital": "Лондон",
        "area": 242.50,
        "population": 68000.0
    },
    {
        "name": "Венгрия",
        "capital": "Будапешт",
        "area": 93.03,
        "population": 9600.0
    },
    {
        "name": "Германия",
        "capital": "Берлин",
        "area": 357.59,
        "population": 84500.0
    },
    {
        "name": "Греция",
        "capital": "Афины",
        "area": 131.96,
        "population": 10400.0
    },
    {
        "name": "Дания",
        "capital": "Копенгаген",
        "area": 42.93,
        "population": 5900.0
    },
    {
        "name": "Ирландия",
        "capital": "Дублин",
        "area": 70.27,
        "population": 5300.0
    },
    {
        "name": "Исландия",
        "capital": "Рейкьявик",
        "area": 103.00,
        "population": 390.0
    },
    {
        "name": "Испания",
        "capital": "Мадрид",
        "area": 505.99,
        "population": 48500.0
    },
    {
        "name": "Италия",
        "capital": "Рим",
        "area": 302.07,
        "population": 58900.0
    },
    {
        "name": "Латвия",
        "capital": "Рига",
        "area": 64.59,
        "population": 1870.0
    },
    {
        "name": "Литва",
        "capital": "Вильнюс",
        "area": 65.30,
        "population": 2880.0
    },
    {
        "name": "Лихтенштейн",
        "capital": "Вадуц",
        "area": 0.16,
        "population": 40.0
    },
    {
        "name": "Люксембург",
        "capital": "Люксембург",
        "area": 2.59,
        "population": 660.0
    },
    {
        "name": "Мальта",
        "capital": "Валлетта",
        "area": 0.32,
        "population": 535.0
    },
    {
        "name": "Молдавия",
        "capital": "Кишинёв",
        "area": 33.85,
        "population": 2500.0
    },
    {
        "name": "Монако",
        "capital": "Монако",
        "area": 0.002,
        "population": 39.0
    },
    {
        "name": "Нидерланды",
        "capital": "Амстердам",
        "area": 41.54,
        "population": 17900.0
    },
    {
        "name": "Норвегия",
        "capital": "Осло",
        "area": 385.20,
        "population": 5500.0
    },
    {
        "name": "Польша",
        "capital": "Варшава",
        "area": 312.68,
        "population": 36700.0
    },
    {
        "name": "Португалия",
        "capital": "Лиссабон",
        "area": 92.21,
        "population": 10500.0
    },
    # ~ {
        # ~ "name": "Россия",
        # ~ "capital": "Москва",
        # ~ "area": 17125.19,
        # ~ "population": 146000.0
    # ~ },
    {
        "name": "Румыния",
        "capital": "Бухарест",
        "area": 238.40,
        "population": 19000.0
    },
    {
        "name": "Сан-Марино",
        "capital": "Сан-Марино",
        "area": 0.061,
        "population": 34.0
    },
    {
        "name": "Северная Македония",
        "capital": "Скопье",
        "area": 25.71,
        "population": 1800.0
    },
    {
        "name": "Сербия",
        "capital": "Белград",
        "area": 88.49,
        "population": 6600.0
    },
    {
        "name": "Словакия",
        "capital": "Братислава",
        "area": 49.03,
        "population": 5400.0
    },
    {
        "name": "Словения",
        "capital": "Любляна",
        "area": 20.27,
        "population": 2100.0
    },
    {
        "name": "Украина",
        "capital": "Киев",
        "area": 603.62,
        "population": 38000.0
    },
    {
        "name": "Финляндия",
        "capital": "Хельсинки",
        "area": 338.45,
        "population": 5600.0
    },
    {
        "name": "Франция",
        "capital": "Париж",
        "area": 543.94,
        "population": 68200.0
    },
    {
        "name": "Хорватия",
        "capital": "Загреб",
        "area": 56.59,
        "population": 3850.0
    },
    {
        "name": "Черногория",
        "capital": "Подгорица",
        "area": 13.81,
        "population": 620.0
    },
    {
        "name": "Чехия",
        "capital": "Прага",
        "area": 78.87,
        "population": 10900.0
    },
    {
        "name": "Швейцария",
        "capital": "Берн",
        "area": 41.28,
        "population": 8900.0
    },
    {
        "name": "Швеция",
        "capital": "Стокгольм",
        "area": 450.30,
        "population": 10500.0
    },
    {
        "name": "Эстония",
        "capital": "Таллин",
        "area": 45.34,
        "population": 1360.0
    }
]


total = len(europe)
print(f"Всего есть стран в Западной Европе: {total}")

# ~ а. по площади,

key = 'area'

europe.sort(key = lambda x: x[key], reverse=True)

total_value = sum( x[key] for x in europe )
print(f"\nСуммарная площадь всех стран Западной Европы равна {total_value:.2f} тыс.кв.км.")

best_value = 0
for num in range(total):
    best_value += europe[num][key]
    rest_value = total_value - best_value
    if best_value >= rest_value:
        print(f"""
Площадь {num} крупнейших стран Западной Европы равна {best_value:.2f} тыс.кв.км
и превосходит площадь всех остальных стран, равную {rest_value:.2f} тыс.кв.км.
Это страны: """, end="")
        print( *(land['name'] for land in europe[:num]), sep=", ", end=".")
        break

# ~ б. по населению.

key = 'population'

europe.sort(key = lambda x: x[key], reverse=True)

total_value = sum( x[key] for x in europe )
print(f"\n\nСуммарное население всех стран Западной Европы равно {total_value:.2f} тыс.человек.")

best_value = 0
for num in range(total):
    best_value += europe[num][key]
    rest_value = total_value - best_value
    if best_value >= rest_value:
        print(f"""
Население {num} крупнейших стран Западной Европы равно {best_value:.2f} тыс.человек
и превосходит население всех остальных стран, равное {rest_value:.2f} тыс.человек.
Это страны: """, end="")
        print( *(land['name'] for land in europe[:num]), sep=", ", end=".")
        break

# -------------------- end ----------------
print()

# ------------------------------------

# Всего есть стран в Западной Европе: 43

# ~ Суммарная площадь всех стран Западной Европы равна 5955.53 тыс.кв.км.

# ~ Площадь 6 крупнейших стран Западной Европы равна 3185.09 тыс.кв.км
# ~ и превосходит площадь всех остальных стран, равную 2770.44 тыс.кв.км.
# ~ Это страны: Украина, Франция, Испания, Швеция, Норвегия, Германия.

# ~ Суммарное население всех стран Западной Европы равно 596023.80 тыс.человек.

# ~ Население 4 крупнейших стран Западной Европы равно 328100.00 тыс.человек
# ~ и превосходит население всех остальных стран, равное 267923.80 тыс.человек.
# ~ Это страны: Германия, Франция, Великобритания, Италия.

# ------------------------------------
