#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# stars.py
# 2026-06-24 2026-06-24 1.1

# ~ дай список 50 крупнейших звёзд как list[json], 
# ~ указав (всё по-английски): 
# ~ - название,
# ~ - звёздная величина,
# ~ - масса,
# ~ - радиус

# -------------------------- данные -------------------------

data = [
  {
    "name": "Stephenson 2-18",
    "magnitude (V)": 15.2,
    "mass (Solar Masses)": 40.0,
    "radius (Solar Radii)": 2150.0,
    "distance (ly)": 18900.0,
    "constellation": "Scutum"
  },
  {
    "name": "UY Scuti",
    "magnitude (V)": 8.9,
    "mass (Solar Masses)": 10.0,
    "radius (Solar Radii)": 1708.0,
    "distance (ly)": 5100.0,
    "constellation": "Scutum"
  },
  {
    "name": "WOH G64",
    "magnitude (V)": 18.4,
    "mass (Solar Masses)": 25.0,
    "radius (Solar Radii)": 1540.0,
    "distance (ly)": 160000.0,
    "constellation": "Dorado"
  },
  {
    "name": "RW Cephei",
    "magnitude (V)": 6.5,
    "mass (Solar Masses)": 13.9,
    "radius (Solar Radii)": 1535.0,
    "distance (ly)": 11500.0,
    "constellation": "Cepheus"
  },
  {
    "name": "Westerlund 1-26",
    "magnitude (V)": 16.8,
    "mass (Solar Masses)": 35.0,
    "radius (Solar Radii)": 1530.0,
    "distance (ly)": 11500.0,
    "constellation": "Ara"
  },
  {
    "name": "V354 Cephei",
    "magnitude (V)": 10.9,
    "mass (Solar Masses)": 20.0,
    "radius (Solar Radii)": 1520.0,
    "distance (ly)": 9000.0,
    "constellation": "Cepheus"
  },
  {
    "name": "VX Sagittarii",
    "magnitude (V)": 8.8,
    "mass (Solar Masses)": 12.0,
    "radius (Solar Radii)": 1520.0,
    "distance (ly)": 5100.0,
    "constellation": "Sagittarius"
  },
  {
    "name": "KY Cygni",
    "magnitude (V)": 10.8,
    "mass (Solar Masses)": 25.0,
    "radius (Solar Radii)": 1420.0,
    "distance (ly)": 5000.0,
    "constellation": "Cygnus"
  },
  {
    "name": "VY Canis Majoris",
    "magnitude (V)": 7.9,
    "mass (Solar Masses)": 17.0,
    "radius (Solar Radii)": 1420.0,
    "distance (ly)": 3900.0,
    "constellation": "Canis Major"
  },
  {
    "name": "HR 5171 A",
    "magnitude (V)": 6.3,
    "mass (Solar Masses)": 39.0,
    "radius (Solar Radii)": 1315.0,
    "distance (ly)": 12000.0,
    "constellation": "Centaurus"
  },
  {
    "name": "AH Scorpii",
    "magnitude (V)": 8.1,
    "mass (Solar Masses)": 15.0,
    "radius (Solar Radii)": 1287.0,
    "distance (ly)": 7400.0,
    "constellation": "Scorpius"
  },
  {
    "name": "VV Cephei A",
    "magnitude (V)": 4.9,
    "mass (Solar Masses)": 19.0,
    "radius (Solar Radii)": 1050.0,
    "distance (ly)": 4900.0,
    "constellation": "Cepheus"
  },
  {
    "name": "NML Cygni",
    "magnitude (V)": 16.6,
    "mass (Solar Masses)": 25.0,
    "radius (Solar Radii)": 1183.0,
    "distance (ly)": 5300.0,
    "constellation": "Cygnus"
  },
  {
    "name": "BI Cygni",
    "magnitude (V)": 9.3,
    "mass (Solar Masses)": 20.0,
    "radius (Solar Radii)": 1160.0,
    "distance (ly)": 5200.0,
    "constellation": "Cygnus"
  },
  {
    "name": "BC Cygni",
    "magnitude (V)": 9.9,
    "mass (Solar Masses)": 19.0,
    "radius (Solar Radii)": 1140.0,
    "distance (ly)": 5300.0,
    "constellation": "Cygnus"
  },
  {
    "name": "RT Carinae",
    "magnitude (V)": 8.5,
    "mass (Solar Masses)": 15.0,
    "radius (Solar Radii)": 1090.0,
    "distance (ly)": 8200.0,
    "constellation": "Carina"
  },
  {
    "name": "CK Carinae",
    "magnitude (V)": 7.5,
    "mass (Solar Masses)": 15.0,
    "radius (Solar Radii)": 1060.0,
    "distance (ly)": 7200.0,
    "constellation": "Carina"
  },
  {
    "name": "KW Sagittarii",
    "magnitude (V)": 8.9,
    "mass (Solar Masses)": 15.0,
    "radius (Solar Radii)": 1005.0,
    "distance (ly)": 7800.0,
    "constellation": "Sagittarius"
  },
  {
    "name": "PZ Cassiopeiae",
    "magnitude (V)": 8.6,
    "mass (Solar Masses)": 25.0,
    "radius (Solar Radii)": 1004.0,
    "distance (ly)": 7800.0,
    "constellation": "Cassiopeia"
  },
  {
    "name": "Betelgeuse",
    "magnitude (V)": 0.5,
    "mass (Solar Masses)": 16.5,
    "radius (Solar Radii)": 950.0,
    "distance (ly)": 640.0,
    "constellation": "Orion"
  },
  {
    "name": "Antares",
    "magnitude (V)": 1.0,
    "mass (Solar Masses)": 12.0,
    "radius (Solar Radii)": 700.0,
    "distance (ly)": 550.0,
    "constellation": "Scorpius"
  },
  {
    "name": "V382 Carinae",
    "magnitude (V)": 3.9,
    "mass (Solar Masses)": 20.0,
    "radius (Solar Radii)": 700.0,
    "distance (ly)": 5900.0,
    "constellation": "Carina"
  },
  {
    "name": "S Persei",
    "magnitude (V)": 9.1,
    "mass (Solar Masses)": 20.0,
    "radius (Solar Radii)": 940.0,
    "distance (ly)": 7900.0,
    "constellation": "Perseus"
  },
  {
    "name": "TV Geminorum",
    "magnitude (V)": 6.6,
    "mass (Solar Masses)": 15.0,
    "radius (Solar Radii)": 710.0,
    "distance (ly)": 3900.0,
    "constellation": "Gemini"
  },
  {
    "name": "V509 Cassiopeiae",
    "magnitude (V)": 5.1,
    "mass (Solar Masses)": 25.0,
    "radius (Solar Radii)": 650.0,
    "distance (ly)": 4500.0,
    "constellation": "Cassiopeia"
  },
  {
    "name": "Mu Cephei",
    "magnitude (V)": 4.1,
    "mass (Solar Masses)": 19.2,
    "radius (Solar Radii)": 972.0,
    "distance (ly)": 2840.0,
    "constellation": "Cepheus"
  },
  {
    "name": "V838 Monocerotis",
    "magnitude (V)": 15.7,
    "mass (Solar Masses)": 15.0,
    "radius (Solar Radii)": 380.0,
    "distance (ly)": 20000.0,
    "constellation": "Monoceros"
  },
  {
    "name": "IRC+10420",
    "magnitude (V)": 11.1,
    "mass (Solar Masses)": 50.0,
    "radius (Solar Radii)": 1340.0,
    "distance (ly)": 13000.0,
    "constellation": "Aquila"
  },
  {
    "name": "V602 Carinae",
    "magnitude (V)": 8.7,
    "mass (Solar Masses)": 15.0,
    "radius (Solar Radii)": 1050.0,
    "distance (ly)": 6500.0,
    "constellation": "Carina"
  },
  {
    "name": "V355 Cephei",
    "magnitude (V)": 11.2,
    "mass (Solar Masses)": 15.0,
    "radius (Solar Radii)": 300.0,
    "distance (ly)": 9500.0,
    "constellation": "Cepheus"
  },
  {
    "name": "BO Carinae",
    "magnitude (V)": 7.2,
    "mass (Solar Masses)": 15.0,
    "radius (Solar Radii)": 400.0,
    "distance (ly)": 8200.0,
    "constellation": "Carina"
  },
  {
    "name": "V396 Centauri",
    "magnitude (V)": 8.7,
    "mass (Solar Masses)": 14.0,
    "radius (Solar Radii)": 600.0,
    "distance (ly)": 7100.0,
    "constellation": "Centaurus"
  },
  {
    "name": "V915 Scorpii",
    "magnitude (V)": 4.8,
    "mass (Solar Masses)": 16.0,
    "radius (Solar Radii)": 500.0,
    "distance (ly)": 7300.0,
    "constellation": "Scorpius"
  },
  {
    "name": "GCIRS 7",
    "magnitude (V)": 15.9,
    "mass (Solar Masses)": 20.0,
    "radius (Solar Radii)": 960.0,
    "distance (ly)": 26000.0,
    "constellation": "Sagittarius"
  },
  {
    "name": "S Cassiopeiae",
    "magnitude (V)": 8.9,
    "mass (Solar Masses)": 10.0,
    "radius (Solar Radii)": 930.0,
    "distance (ly)": 2300.0,
    "constellation": "Cassiopeia"
  },
  {
    "name": "R Doradus",
    "magnitude (V)": 5.4,
    "mass (Solar Masses)": 1.0,
    "radius (Solar Radii)": 370.0,
    "distance (ly)": 178.0,
    "constellation": "Dorado"
  },
  {
    "name": "S Doradus",
    "magnitude (V)": 9.4,
    "mass (Solar Masses)": 24.0,
    "radius (Solar Radii)": 380.0,
    "distance (ly)": 160000.0,
    "constellation": "Dorado"
  },
  {
    "name": "La Superba",
    "magnitude (V)": 5.4,
    "mass (Solar Masses)": 3.0,
    "radius (Solar Radii)": 443.0,
    "distance (ly)": 711.0,
    "constellation": "Canes Venatici"
  },
  {
    "name": "Rho Cassiopeiae",
    "magnitude (V)": 4.5,
    "mass (Solar Masses)": 22.0,
    "radius (Solar Radii)": 450.0,
    "distance (ly)": 3400.0,
    "constellation": "Cassiopeia"
  },
  {
    "name": "CE Tauri",
    "magnitude (V)": 4.3,
    "mass (Solar Masses)": 14.3,
    "radius (Solar Radii)": 608.0,
    "distance (ly)": 1800.0,
    "constellation": "Taurus"
  },
  {
    "name": "Alpha Herculis",
    "magnitude (V)": 3.3,
    "mass (Solar Masses)": 2.8,
    "radius (Solar Radii)": 400.0,
    "distance (ly)": 360.0,
    "constellation": "Hercules"
  },
  {
    "name": "Mira A",
    "magnitude (V)": 6.5,
    "mass (Solar Masses)": 1.2,
    "radius (Solar Radii)": 400.0,
    "distance (ly)": 300.0,
    "constellation": "Cetus"
  },
  {
    "name": "Rigel",
    "magnitude (V)": 0.1,
    "mass (Solar Masses)": 21.0,
    "radius (Solar Radii)": 78.9,
    "distance (ly)": 860.0,
    "constellation": "Orion"
  },
  {
    "name": "Pistol Star",
    "magnitude (V)": 28.0,
    "mass (Solar Masses)": 27.5,
    "radius (Solar Radii)": 306.0,
    "distance (ly)": 25000.0,
    "constellation": "Sagittarius"
  },
  {
    "name": "Eta Carinae A",
    "magnitude (V)": 4.5,
    "mass (Solar Masses)": 100.0,
    "radius (Solar Radii)": 240.0,
    "distance (ly)": 7500.0,
    "constellation": "Carina"
  },
  {
    "name": "Deneb",
    "magnitude (V)": 1.25,
    "mass (Solar Masses)": 19.0,
    "radius (Solar Radii)": 203.0,
    "distance (ly)": 2600.0,
    "constellation": "Cygnus"
  },
  {
    "name": "Canopus",
    "magnitude (V)": -0.74,
    "mass (Solar Masses)": 8.0,
    "radius (Solar Radii)": 71.0,
    "distance (ly)": 310.0,
    "constellation": "Carina"
  },
  {
    "name": "LBV 1806-20",
    "magnitude (V)": 8.6,
    "mass (Solar Masses)": 36.0,
    "radius (Solar Radii)": 150.0,
    "distance (ly)": 28000.0,
    "constellation": "Sagittarius"
  },
  {
    "name": "Peony Nebula Star",
    "magnitude (V)": 15.1,
    "mass (Solar Masses)": 100.0,
    "radius (Solar Radii)": 100.0,
    "distance (ly)": 26000.0,
    "constellation": "Sagittarius"
  },
  {
    "name": "Cyg OB2-12",
    "magnitude (V)": 11.4,
    "mass (Solar Masses)": 110.0,
    "radius (Solar Radii)": 228.0,
    "distance (ly)": 5200.0,
    "constellation": "Cygnus"
  }
]


# -------------------------- подготовка -------------------------

from pprint import pprint
from collections import defaultdict

# -------------------------- расчёт -------------------------

# ---------- тест 1 ----------

print('\n1. найти самую тяжёлую и самую далёкую звезды')

print(f"""
самая тяжёлая (в массах Солнца):  { max( [ (star['mass (Solar Masses)'], star['name']) for star in data] ) }
самая далёкая (в световых годах): { max( [ (star['distance (ly)'], star['name']) for star in data] ) }
""")

# ---------- тест 2 ----------

print('\n2. разбери всё по созвездиям')

cons = defaultdict(list)

for star in data:
    cons[ star['constellation'] ] . append( star['name'] )

pprint(cons)

# -------------------------- результаты -------------------------

# ~ 1. найти самую тяжёлую и самую далёкую звезды

# ~ самая тяжёлая (в массах Солнца):  (110.0, 'Cyg OB2-12')
# ~ самая далёкая (в световых годах): (160000.0, 'WOH G64')

# ~ 2. разбери всё по созвездиям

# ~ defaultdict(<class 'list'>,
            # ~ {'Aquila': ['IRC+10420'],
             # ~ 'Ara': ['Westerlund 1-26'],
             # ~ 'Canes Venatici': ['La Superba'],
             # ~ 'Canis Major': ['VY Canis Majoris'],
             # ~ 'Carina': ['RT Carinae',
                        # ~ 'CK Carinae',
                        # ~ 'V382 Carinae',
                        # ~ 'V602 Carinae',
                        # ~ 'BO Carinae',
                        # ~ 'Eta Carinae A',
                        # ~ 'Canopus'],
             # ~ 'Cassiopeia': ['PZ Cassiopeiae',
                            # ~ 'V509 Cassiopeiae',
                            # ~ 'S Cassiopeiae',
                            # ~ 'Rho Cassiopeiae'],
             # ~ 'Centaurus': ['HR 5171 A', 'V396 Centauri'],
             # ~ 'Cepheus': ['RW Cephei',
                         # ~ 'V354 Cephei',
                         # ~ 'VV Cephei A',
                         # ~ 'Mu Cephei',
                         # ~ 'V355 Cephei'],
             # ~ 'Cetus': ['Mira A'],
             # ~ 'Cygnus': ['KY Cygni',
                        # ~ 'NML Cygni',
                        # ~ 'BI Cygni',
                        # ~ 'BC Cygni',
                        # ~ 'Deneb',
                        # ~ 'Cyg OB2-12'],
             # ~ 'Dorado': ['WOH G64', 'R Doradus', 'S Doradus'],
             # ~ 'Gemini': ['TV Geminorum'],
             # ~ 'Hercules': ['Alpha Herculis'],
             # ~ 'Monoceros': ['V838 Monocerotis'],
             # ~ 'Orion': ['Betelgeuse', 'Rigel'],
             # ~ 'Perseus': ['S Persei'],
             # ~ 'Sagittarius': ['VX Sagittarii',
                             # ~ 'KW Sagittarii',
                             # ~ 'GCIRS 7',
                             # ~ 'Pistol Star',
                             # ~ 'LBV 1806-20',
                             # ~ 'Peony Nebula Star'],
             # ~ 'Scorpius': ['AH Scorpii', 'Antares', 'V915 Scorpii'],
             # ~ 'Scutum': ['Stephenson 2-18', 'UY Scuti'],
             # ~ 'Taurus': ['CE Tauri']})

# -------------------------- обсуждение -------------------------

# ~ Астрофизические примечания к данным

# ~ Единицы измерения: Масса (mass (M☉)) и радиус (radius (R☉)) приведены в долях от массы и радиуса нашего Солнца, чтобы избежать неудобных степенных чисел в байтах.В

# ~ идимая величина (magnitude (V)): Указан блеск звезд в оптическом (видимом) диапазоне. Обратите внимание, что некоторые гиганты (например, Stephenson 2-18 или WOH G64) имеют большое значение звездной величины (15–18) из-за огромного удаления или плотных облаков космической пыли, блокирующих их свет на пути к Земле.

# ~ Соотношение радиуса и массы: Крупнейшие по объему звезды (красные сверхгиганты) не обязательно являются самыми массивными. Их колоссальный объем объясняется раздувшейся неплотной оболочкой, в то время как их масса часто не превышает 15–40 масс Солнца.

# ~ Астрономический факт на заметкуОбратите внимание на звезду WOH G64 и S Doradus: расстояние до них указано как 160 000 световых лет. Это связано с тем, что они физически расположены за пределами нашей Галактики (Млечный Путь) и находятся в её спутнике — Большом Магеллановом Облаке.

# -------------------------- конец -------------------------
