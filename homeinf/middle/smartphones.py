#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# smartphones.py
# 2026-06-24 2026-06-24 1.0

# ~ перечисли 10 основных фирм-производителей смартфонов, в формате list[dict],
# ~ все ключи и значения - по-английски,
# ~ указав:
# ~ - name: название,
# ~ - land: страна,
# ~ - years: годы существования (list),
# ~ - models: основные модели смартфонов (list),
# ~ - creator: основатель,
# ~ - owners: нынешние владельцы (управляющие),
# ~ - capital: нынешняя капитализация,
# ~ - position: примерное место в мире по производству смартфонов,
# ~ - amount: объём выпуска (штук в год)

# --------------- данные --------------------

sfman = [
    {
        "name": "Samsung Electronics",
        "land": "South Korea",
        "years": [1969, 2026],
        "models": ["Galaxy S26", "Galaxy S25 Ultra", "Galaxy A55", "Galaxy Z Fold6"],
        "creator": "Lee Byung-chul",
        "owners": ["Samsung Group", "Public shareholders"],
        "capital": "$1.32 Trillion",
        "position": "1st or 2nd (Varies by quarter with Apple)",
        "amount": "230-240 Million units"
    },
    {
        "name": "Apple Inc.",
        "land": "United States",
        "years": [1976, 2026],
        "models": ["iPhone 17 Pro Max", "iPhone 16", "iPhone 15", "iPhone SE"],
        "creator": "Steve Jobs, Steve Wozniak, Ronald Wayne",
        "owners": ["Institutional investors (Vanguard, BlackRock)", "Public shareholders"],
        "capital": "$4.38 Trillion",
        "position": "1st or 2nd (Varies by quarter with Samsung)",
        "amount": "220-230 Million units"
    },
    {
        "name": "Xiaomi Corporation",
        "land": "China",
        "years": [2010, 2026],
        "models": ["Xiaomi 14 Ultra", "Redmi Note 13 Pro", "POCO F6", "Xiaomi 13"],
        "creator": "Lei Jun",
        "owners": ["Lei Jun", "Public shareholders"],
        "capital": "$45 Billion",
        "position": "3rd",
        "amount": "140-150 Million units"
    },
    {
        "name": "OPPO Co., Ltd.",
        "land": "China",
        "years": [2004, 2026],
        "models": ["Find X7 Ultra", "Reno12 Pro", "A98", "Find N3 Flip"],
        "creator": "Tony Chen",
        "owners": ["BBK Electronics"],
        "capital": "Private (Estimated enterprise value around $20-30 Billion)",
        "position": "4th",
        "amount": "100-110 Million units"
    },
    {
        "name": "Vivo Mobile Communication Co., Ltd.",
        "land": "China",
        "years": [2009, 2026],
        "models": ["X100 Pro", "V30 Pro", "Y200", "iQOO 12"],
        "creator": "Shen Wei",
        "owners": ["BBK Electronics"],
        "capital": "Private (Estimated enterprise value around $15-25 Billion)",
        "position": "5th",
        "amount": "95-105 Million units"
    },
    {
        "name": "Transsion Holdings",
        "land": "China",
        "years": [2006, 2026],
        "models": ["Tecno Camon 30", "Infinix Note 40", "itel P55", "Tecno Phantom V Flip"],
        "creator": "Zhu Zhaojiang",
        "owners": ["Zhu Zhaojiang", "Public shareholders"],
        "capital": "$11.5 Billion",
        "position": "6th (Dominates African and South Asian markets)",
        "amount": "85-95 Million units"
    },
    {
        "name": "Honor Device Co., Ltd.",
        "land": "China",
        "years": [2013, 2026],
        "models": ["Honor Magic6 Pro", "Honor 200 Pro", "Honor X9b", "Honor Magic V2"],
        "creator": "Huawei Technologies (Spin-off in 2020)",
        "owners": ["Shenzhen Smart City Technology Development Group"],
        "capital": "Private (Estimated enterprise value around $12-18 Billion)",
        "position": "7th",
        "amount": "50-60 Million units"
    },
    {
        "name": "Motorola Mobility LLC",
        "land": "United States (Owned by China)",
        "years": [1928, 2026],
        "models": ["Edge 50 Ultra", "Razr 50 Ultra", "Moto G84", "Moto G Power"],
        "creator": "Paul Galvin, Joseph Galvin",
        "owners": ["Lenovo Group"],
        "capital": "Subsidiary (Lenovo Group market cap is around $15 Billion)",
        "position": "8th",
        "amount": "45-55 Million units"
    },
    {
        "name": "Huawei Technologies Co., Ltd.",
        "land": "China",
        "years": [1987, 2026],
        "models": ["Pura 70 Ultra", "Mate 60 Pro", "Nova 12", "Mate X5"],
        "creator": "Ren Zhengfei",
        "owners": ["Employee-owned cooperative (Huawei Investment & Holding)"],
        "capital": "Private (Estimated enterprise value over $100 Billion)",
        "position": "9th",
        "amount": "40-50 Million units"
    },
    {
        "name": "Realme Chongqing Mobile Telecommunications Corp., Ltd.",
        "land": "China",
        "years": [2018, 2026],
        "models": ["Realme GT6", "Realme 12 Pro+", "Realme C67", "Realme Narzo 70"],
        "creator": "Sky Li",
        "owners": ["BBK Electronics (Oppo subsidiary)"],
        "capital": "Private (Financially integrated with Oppo)",
        "position": "10th",
        "amount": "35-45 Million units"
    }
]

# --------------- обработка --------------------

from collections import Counter
from pprint import pprint

print("1. какие страны представлены, сколько раз?")

lands = Counter( [ sf['land']  for sf in sfman ] )

pprint(lands)

# --------------- результат --------------------

# ~ 1. какие страны представлены, сколько раз?
# ~ Counter({'China': 7,
         # ~ 'South Korea': 1,
         # ~ 'United States': 1,
         # ~ 'United States (Owned by China)': 1})

# --------------- конец --------------------
