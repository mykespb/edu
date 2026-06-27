#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# planes.py
# 2026-06-27 2026-06-27 1.0

# ~ Самолёты частной гражданской авиации в мире. Перечисли 30 наиболее известных самолётов, включить в список украинский ANG-01, SF-50, DA-50, DA-62, PLiatus PC-24, Epic-1000, Stratos-716, Cirrus sr22t-g7, аналогичные. По ним укажи (list[dict], всё по-англ.):
# ~ - name; название,
# ~ - company: компания-разработчик (производитель),
# ~ - country: страна,
# ~ - year: год начала выпуска,
# ~ - amount: сколько выпущено бортов,
# ~ - type: тип (винтовой, реактивный, пр.),
# ~ - engines: количество двигателей,
# ~ - speed_best: скорость крейсерская,
# ~ - speed_max: скорость максимальная,
# ~ - people: сколько человек (crew: экипаж, pass: пассажиры),
# ~ - mtom: макс. взлётная масса,
# ~ - weight: макс. груз,
# ~ - dist: макс. дальность,
# ~ - licence: тип лицензии пилота,
# ~ - usd: цена в тыс. USD,
# ~ - up: длина взлётной полосы,
# ~ - down: длина посадочной полосы.

# -------------------------- данные -------------------------

data = [
  {
    "name": "ANG-01 Patriot",
    "company": "ANG Patriot UA / Veloce Planes",
    "country": "Ukraine",
    "year": 2019,
    "amount": 12,
    "type": "propeller",
    "engines": 1,
    "speed_best": 310,
    "speed_max": 360,
    "people": {
      "crew": 1,
      "pass": 4
    },
    "mtom": 950,
    "weight": 570,
    "dist": 2500,
    "licence": "PPL",
    "usd": 297,
    "up": 250,
    "down": 300
  },
  {
    "name": "Vision SF50 Generation 2+",
    "company": "Cirrus Aircraft",
    "country": "USA",
    "year": 2016,
    "amount": 650,
    "type": "jet",
    "engines": 1,
    "speed_best": 560,
    "speed_max": 576,
    "people": {
      "crew": 1,
      "pass": 6
    },
    "mtom": 2727,
    "weight": 600,
    "dist": 2360,
    "licence": "PPL / Type Rating",
    "usd": 3250,
    "up": 619,
    "down": 495
  },
  {
    "name": "Diamond DA50 RG",
    "company": "Diamond Aircraft Industries",
    "country": "Austria",
    "year": 2020,
    "amount": 180,
    "type": "propeller",
    "engines": 1,
    "speed_best": 298,
    "speed_max": 335,
    "people": {
      "crew": 1,
      "pass": 4
    },
    "mtom": 1999,
    "weight": 559,
    "dist": 1390,
    "licence": "PPL",
    "usd": 1150,
    "up": 440,
    "down": 350
  },
  {
    "name": "Diamond DA62",
    "company": "Diamond Aircraft Industries",
    "country": "Austria",
    "year": 2015,
    "amount": 500,
    "type": "propeller",
    "engines": 2,
    "speed_best": 325,
    "speed_max": 356,
    "people": {
      "crew": 1,
      "pass": 6
    },
    "mtom": 2300,
    "weight": 710,
    "dist": 2380,
    "licence": "PPL / ME",
    "usd": 1500,
    "up": 480,
    "down": 390
  },
  {
    "name": "Pilatus PC-24",
    "company": "Pilatus Aircraft",
    "country": "Switzerland",
    "year": 2018,
    "amount": 260,
    "type": "jet",
    "engines": 2,
    "speed_best": 815,
    "speed_max": 815,
    "people": {
      "crew": 1,
      "pass": 10
    },
    "mtom": 8500,
    "weight": 1134,
    "dist": 3700,
    "licence": "PPL / Type Rating",
    "usd": 13000,
    "up": 900,
    "down": 724
  },
  {
    "name": "Epic E1000 GX",
    "company": "Epic Aircraft",
    "country": "USA",
    "year": 2015,
    "amount": 95,
    "type": "turboprop",
    "engines": 1,
    "speed_best": 617,
    "speed_max": 617,
    "people": {
      "crew": 1,
      "pass": 5
    },
    "mtom": 3629,
    "weight": 500,
    "dist": 2900,
    "licence": "PPL / SET",
    "usd": 4450,
    "up": 488,
    "down": 554
  },
  {
    "name": "Stratos 716",
    "company": "Stratos Aircraft",
    "country": "USA",
    "year": 2020,
    "amount": 5,
    "type": "jet",
    "engines": 1,
    "speed_best": 744,
    "speed_max": 760,
    "people": {
      "crew": 1,
      "pass": 6
    },
    "mtom": 3810,
    "weight": 680,
    "dist": 2778,
    "licence": "PPL / Type Rating",
    "usd": 3500,
    "up": 750,
    "down": 650
  },
  {
    "name": "Cirrus SR22T G7",
    "company": "Cirrus Aircraft",
    "country": "USA",
    "year": 2001,
    "amount": 10200,
    "type": "propeller",
    "engines": 1,
    "speed_best": 339,
    "speed_max": 395,
    "people": {
      "crew": 1,
      "pass": 4
    },
    "mtom": 1633,
    "weight": 602,
    "dist": 1900,
    "licence": "PPL",
    "usd": 1050,
    "up": 330,
    "down": 360
  },
  {
    "name": "Cessna 172 Skyhawk",
    "company": "Textron Aviation",
    "country": "USA",
    "year": 1956,
    "amount": 46000,
    "type": "propeller",
    "engines": 1,
    "speed_best": 230,
    "speed_max": 246,
    "people": {
      "crew": 1,
      "pass": 3
    },
    "mtom": 1157,
    "weight": 400,
    "dist": 1185,
    "licence": "PPL",
    "usd": 490,
    "up": 293,
    "down": 407
  },
  {
    "name": "Cessna 182 Skylane",
    "company": "Textron Aviation",
    "country": "USA",
    "year": 1956,
    "amount": 24500,
    "type": "propeller",
    "engines": 1,
    "speed_best": 269,
    "speed_max": 280,
    "people": {
      "crew": 1,
      "pass": 3
    },
    "mtom": 1406,
    "weight": 517,
    "dist": 1720,
    "licence": "PPL",
    "usd": 680,
    "up": 241,
    "down": 411
  },
  {
    "name": "Beechcraft Bonanza G36",
    "company": "Textron Aviation",
    "country": "USA",
    "year": 1947,
    "amount": 18500,
    "type": "propeller",
    "engines": 1,
    "speed_best": 326,
    "speed_max": 345,
    "people": {
      "crew": 1,
      "pass": 5
    },
    "mtom": 1656,
    "weight": 483,
    "dist": 1700,
    "licence": "PPL",
    "usd": 1100,
    "up": 583,
    "down": 442
  },
  {
    "name": "Piper PA-28 Cherokee",
    "company": "Piper Aircraft",
    "country": "USA",
    "year": 1961,
    "amount": 33500,
    "type": "propeller",
    "engines": 1,
    "speed_best": 230,
    "speed_max": 260,
    "people": {
      "crew": 1,
      "pass": 3
    },
    "mtom": 975,
    "weight": 430,
    "dist": 1100,
    "licence": "PPL",
    "usd": 420,
    "up": 490,
    "down": 450
  },
  {
    "name": "Piper PA-46 Malibu Mirage",
    "company": "Piper Aircraft",
    "country": "USA",
    "year": 1983,
    "amount": 13200,
    "type": "propeller",
    "engines": 1,
    "speed_best": 395,
    "speed_max": 460,
    "people": {
      "crew": 1,
      "pass": 5
    },
    "mtom": 1968,
    "weight": 650,
    "dist": 2490,
    "licence": "PPL",
    "usd": 1450,
    "up": 637,
    "down": 510
  },
  {
    "name": "Mooney M20 Ovation Ultra",
    "company": "Mooney Airplane Company",
    "country": "USA",
    "year": 1955,
    "amount": 11200,
    "type": "propeller",
    "engines": 1,
    "speed_best": 365,
    "speed_max": 374,
    "people": {
      "crew": 1,
      "pass": 3
    },
    "mtom": 1528,
    "weight": 460,
    "dist": 2685,
    "licence": "PPL",
    "usd": 890,
    "up": 610,
    "down": 580
  },
  {
    "name": "Pilatus PC-12 NGX",
    "company": "Pilatus Aircraft",
    "country": "Switzerland",
    "year": 1994,
    "amount": 2100,
    "type": "turboprop",
    "engines": 1,
    "speed_best": 537,
    "speed_max": 540,
    "people": {
      "crew": 1,
      "pass": 9
    },
    "mtom": 4740,
    "weight": 1018,
    "dist": 3417,
    "licence": "PPL / CPL / SET",
    "usd": 6200,
    "up": 756,
    "down": 661
  },
  {
    "name": "Socata TBM 960",
    "company": "Daher",
    "country": "France",
    "year": 1990,
    "amount": 1200,
    "type": "turboprop",
    "engines": 1,
    "speed_best": 611,
    "speed_max": 611,
    "people": {
      "crew": 1,
      "pass": 5
    },
    "mtom": 3396,
    "weight": 650,
    "dist": 3200,
    "licence": "PPL / SET",
    "usd": 4800,
    "up": 732,
    "down": 741
  },
  {
    "name": "HondaJet Elite II",
    "company": "Honda Aircraft Company",
    "country": "USA / Japan",
    "year": 2015,
    "amount": 260,
    "type": "jet",
    "engines": 2,
    "speed_best": 782,
    "speed_max": 782,
    "people": {
      "crew": 1,
      "pass": 6
    },
    "mtom": 4853,
    "weight": 680,
    "dist": 2865,
    "licence": "PPL / Type Rating",
    "usd": 7200,
    "up": 1128,
    "down": 829
  },
  {
    "name": "Cessna Citation M2 Gen2",
    "company": "Textron Aviation",
    "country": "USA",
    "year": 2013,
    "amount": 380,
    "type": "jet",
    "engines": 2,
    "speed_best": 748,
    "speed_max": 748,
    "people": {
      "crew": 1,
      "pass": 6
    },
    "mtom": 4853,
    "weight": 700,
    "dist": 2870,
    "licence": "PPL / Type Rating",
    "usd": 6150,
    "up": 978,
    "down": 789
  },
  {
    "name": "Embraer Phenom 100EV",
    "company": "Embraer",
    "country": "Brazil",
    "year": 2008,
    "amount": 420,
    "type": "jet",
    "engines": 2,
    "speed_best": 750,
    "speed_max": 750,
    "people": {
      "crew": 1,
      "pass": 6
    },
    "mtom": 4800,
    "weight": 755,
    "dist": 2180,
    "licence": "PPL / Type Rating",
    "usd": 5100,
    "up": 975,
    "down": 741
  },
  {
    "name": "Tecnam P2010",
    "company": "Tecnam",
    "country": "Italy",
    "year": 2014,
    "amount": 320,
    "type": "propeller",
    "engines": 1,
    "speed_best": 250,
    "speed_max": 260,
    "people": {
      "crew": 1,
      "pass": 3
    },
    "mtom": 1160,
    "weight": 410,
    "dist": 1780,
    "licence": "PPL",
    "usd": 480,
    "up": 380,
    "down": 320
  }
]


# -------------------------- подготовка -------------------------

from collections import Counter
from pprint import pprint

       
# -------------------------- расчёт -------------------------

print('1. сколько какого типа?')

proptype = Counter( [ p['type'] for p in data] )

pprint(proptype)

# ~ 1. сколько какого типа?
# ~ Counter({'propeller': 11, 'jet': 6, 'turboprop': 3})


# -------------------------- конец -------------------------
