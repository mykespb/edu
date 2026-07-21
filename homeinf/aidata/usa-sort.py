#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# usa-sort.py
# 2026-07-19 2026-07-20 2.2

# ~ "сделай сортируемую таблицу из них, указав параметры (столбцы): процент консервативного населения, безопасность, уровень экономического развития, уровень культурного развития, климат (не слишком контрастный или жаркий или влажный или опасные явления)"
# ~ "замени слова типа "высокое" на числа от 0 до 10, сделай таблицу, пригодную к экспорту в google table"
# ~ Безопасность / Экономика / Культура: 9-10 — Очень высокая/очень развитая, 7-8 — Высокая/выше среднего, 5-6 — Средняя, 3-4 — Ниже среднего/низкая, 0-2 — Критически низкая.Комфорт климата: 7-8 — Мягкий климат без экстрима и катаклизмов, 5-6 — Умеренно контрастный, без сильных угроз, 3-4 — Высокие контрасты или сильные ветры, 1-2 — Экстремальная жара, влажность, ураганы или торнадо.
# ~ State — Название штата (отсортировано по английскому алфавиту).Cons (%) — Percentage of conservative population (Процент консервативного населения).Safety — Crime and public safety score (Уровень безопасности, 0-10).Economy — Economic development and GDP score (Экономическое развитие, 0-10).Culture — Cultural infrastructure and activities score (Культурное развитие, 0-10).Climate — Climate comfort score; higher means fewer extremes/disasters (Комфорт климата, 0-10).
# ~ "добавь столбец "Dems (%)"  с долей демократического населения"
# ~ сделай из этих данных list[list]]

from enum import IntEnum

class Params(IntEnum):
    NAME    = 0
    CONS    = 1
    DEMS    = 2
    SAFETY  = 3
    ECONOMY = 4
    CULTURE = 5
    CLIMATE = 6
    RATIO   = 7
    PARTY   = 8
    

states = [
    ["State", "Cons (%)", "Dems (%)", "Safety", "Economy", "Culture", "Climate"],
    ["Alabama", 52, 15, 3, 4, 5, 2],
    ["Alaska", 39, 22, 3, 8, 5, 1],
    ["Arizona", 36, 31, 5, 8, 7, 4],
    ["Arkansas", 50, 17, 3, 3, 5, 2],
    ["California", 21, 47, 4, 10, 10, 8],
    ["Colorado", 26, 39, 5, 9, 8, 6],
    ["Connecticut", 21, 43, 9, 8, 8, 6],
    ["Delaware", 25, 38, 6, 7, 6, 7],
    ["District of Columbia", 6, 75, 1, 9, 10, 6],
    ["Florida", 37, 24, 5, 8, 8, 1],
    ["Georgia", 32, 30, 5, 8, 8, 4],
    ["Hawaii", 18, 45, 7, 6, 7, 7],
    ["Idaho", 52, 14, 8, 7, 5, 7],
    ["Illinois", 26, 42, 4, 8, 9, 5],
    ["Indiana", 43, 21, 5, 5, 5, 5],
    ["Iowa", 44, 22, 8, 5, 5, 5],
    ["Kansas", 45, 23, 5, 5, 5, 2],
    ["Kentucky", 49, 20, 5, 4, 5, 6],
    ["Louisiana", 45, 21, 3, 4, 8, 1],
    ["Maine", 24, 38, 10, 6, 6, 6],
    ["Maryland", 22, 46, 4, 9, 8, 7],
    ["Massachusetts", 15, 52, 9, 9, 10, 6],
    ["Michigan", 31, 33, 5, 6, 7, 5],
    ["Minnesota", 28, 37, 7, 8, 7, 4],
    ["Mississippi", 47, 20, 3, 2, 5, 2],
    ["Missouri", 44, 23, 4, 5, 5, 2],
    ["Montana", 43, 21, 8, 5, 5, 5],
    ["Nebraska", 45, 21, 8, 7, 5, 2],
    ["Nevada", 30, 33, 4, 7, 7, 5],
    ["New Hampshire", 24, 35, 10, 8, 6, 6],
    ["New Jersey", 21, 43, 8, 9, 8, 7],
    ["New Mexico", 28, 36, 2, 4, 7, 6],
    ["New York", 19, 48, 6, 10, 10, 6],
    ["North Carolina", 33, 29, 5, 8, 7, 5],
    ["North Dakota", 49, 15, 7, 7, 4, 3],
    ["Ohio", 41, 26, 5, 5, 8, 7],
    ["Oklahoma", 52, 16, 4, 5, 5, 2],
    ["Oregon", 24, 41, 5, 7, 8, 8],
    ["Pennsylvania", 32, 34, 6, 7, 8, 6],
    ["Rhode Island", 14, 46, 9, 7, 7, 6],
    ["South Carolina", 44, 21, 4, 5, 5, 2],
    ["South Dakota", 48, 16, 8, 5, 5, 2],
    ["Tennessee", 48, 18, 4, 7, 8, 5],
    ["Texas", 39, 27, 5, 9, 8, 2],
    ["Utah", 42, 16, 9, 8, 7, 6],
    ["Vermont", 19, 53, 9, 6, 7, 6],
    ["Virginia", 29, 37, 7, 8, 8, 7],
    ["Washington", 25, 45, 6, 9, 9, 8],
    ["West Virginia", 51, 15, 5, 3, 5, 7],
    ["Wisconsin", 34, 31, 6, 6, 6, 5],
    ["Wyoming", 55, 11, 9, 7, 5, 4]
]

# -----------------------------------------------------------

from pprint import pprint, pp

def ppp(data):
    for q,p in data:
        print(f"{q:12.6f} : {p}")

head   = states[0]
states = states[1:]

print("\nотсортируй штаты по отношению cons/dems\n")

data = []
for d in states:
    cd = d[Params.CONS] / d[Params.DEMS]
    data.append( d + [cd, "cons" if cd>=1. else "dems"])
    
data.sort(key = lambda s: s[Params.RATIO], reverse = True)

print(head)
pp(data)
print(head)

# -----------------------------------------------------------

print('-------------------------------------')
print("\nотсортируй штаты по моим простым предпочтениям\n")
print('-------------------------------------')

def priosimple(data, prefs):
    
    pref_len = len(prefs)

    repref = [
        [
            sum( [state[pref] * (pref_len - pn) 
                for pn, pref in enumerate(prefs)]
                ),
            state[Params.NAME]
        ]
        for sn, state in enumerate(data)
        ]
        
    repref.sort(reverse=True)

    ppp(repref)


prefs = [
    Params.SAFETY,   # 5
    Params.CLIMATE,  # 4
    Params.CULTURE,  # 3
    Params.ECONOMY,  # 2
    Params.RATIO     # 1
    ]
print(prefs)

priosimple(data, prefs)

print('-------------------------------------')

prefs = [
    Params.ECONOMY,  # 2
    Params.CULTURE,  # 1
    ]
print(prefs)

priosimple(data, prefs)

print('-------------------------------------')

prefs = [
    Params.RATIO	# 1
    ]
print(prefs)

priosimple(data, prefs)

# -----------------------------------------------------------

print('-------------------------------------')
print("\nотсортируй штаты по моим сложным предпочтениям\n")
print('-------------------------------------')

def priocomlex(data, prefs):
    
    pref_len = len(prefs)

    repref = [
        [
            sum( [state[pref[0]] * pref[1]
                for pn, pref in enumerate(prefs)]
                ),
            state[Params.NAME]
        ]
        for sn, state in enumerate(data)
        ]
        
    repref.sort(reverse=True)

    ppp(repref)


prefs = [
    [Params.SAFETY,  50],
    [Params.CLIMATE, 42],
    [Params.CULTURE, 64],
    [Params.ECONOMY, 22],
    [Params.RATIO,   88]
    ]

print(prefs)

priocomlex(data, prefs)

print('-------------------------------------')

prefs = [
    [Params.ECONOMY,  99],
    [Params.CULTURE,  11],
    ]
print(prefs)

priocomlex(data, prefs)

print('-------------------------------------')

prefs = [
    [Params.RATIO, 100]
    ]
print(prefs)

priocomlex(data, prefs)

print('-------------------------------------')

# -----------------------------------------------------------
print()
