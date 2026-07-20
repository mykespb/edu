#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# planets.py
# 2026-06-24 2026-06-24 1.1

# ~ Изучаем планеты Солнечной системы. 
# ~ Перечисли их (list[json]), указав поля (все по-английски):
# ~ - name: название,
# ~ - discover: год открытия,
# ~ - distance: расстояние от Солнца,
# ~ - order: порядок от Солнца,
# ~ - mass: масса, 
# ~ - radius: радиус,
# ~ - satellites: спутники (list[json]: поля: название, масса, диаметр, расстояние до планеты),
# ~ - reason: почему так названа

# -------------------------- данные -------------------------

data = [
  {
    "name": "Mercury",
    "discover": "Known since antiquity",
    "distance (AU)": 0.39,
    "order": 1,
    "mass (kg)": 3.3011e23,
    "radius (km)": 2439.7,
    "density (g/cm³)": 5.427,
    "type": "каменная",
    "satellites": [],
    "reason": "Named after the Roman messenger god due to its fast movement across the sky."
  },
  {
    "name": "Venus",
    "discover": "Known since antiquity",
    "distance (AU)": 0.72,
    "order": 2,
    "mass (kg)": 4.8675e24,
    "radius (km)": 6051.8,
    "density (g/cm³)": 5.243,
    "type": "каменная",
    "satellites": [],
    "reason": "Named after the Roman goddess of love and beauty because it is the brightest planet in the night sky."
  },
  {
    "name": "Earth",
    "discover": "Known since antiquity",
    "distance (AU)": 1.0,
    "order": 3,
    "mass (kg)": 5.9722e24,
    "radius (km)": 6371.0,
    "density (g/cm³)": 5.514,
    "type": "каменная",
    "satellites": [
      {
        "name": "The Moon",
        "mass (kg)": 7.342e22,
        "diameter (km)": 3474.8,
        "distance_to_planet (km)": 384400
      }
    ],
    "reason": "Derived from Old English and Germanic words ('eor(t)he' and 'erda') which simply mean 'ground' or 'soil'."
  },
  {
    "name": "Mars",
    "discover": "Known since antiquity",
    "distance (AU)": 1.52,
    "order": 4,
    "mass (kg)": 6.4171e23,
    "radius (km)": 3389.5,
    "density (g/cm³)": 3.933,
    "type": "каменная",
    "satellites": [
      {
        "name": "Phobos",
        "mass (kg)": 1.0659e16,
        "diameter (km)": 22.2,
        "distance_to_planet (km)": 9377
      },
      {
        "name": "Deimos",
        "mass (kg)": 1.4762e15,
        "diameter (km)": 12.6,
        "distance_to_planet (km)": 23460
      }
    ],
    "reason": "Named after the Roman god of war because of its reddish, blood-like color caused by iron oxide on its surface."
  },
  {
    "name": "Jupiter",
    "discover": "Known since antiquity",
    "distance (AU)": 5.2,
    "order": 5,
    "mass (kg)": 1.8982e27,
    "radius (km)": 69911.0,
    "density (g/cm³)": 1.326,
    "type": "газовая",
    "satellites": [
      {
        "name": "Ganymede",
        "mass (kg)": 1.4819e23,
        "diameter (km)": 5268.2,
        "distance_to_planet (km)": 1070400
      },
      {
        "name": "Callisto",
        "mass (kg)": 1.0759e23,
        "diameter (km)": 4820.6,
        "distance_to_planet (km)": 1882700
      },
      {
        "name": "Io",
        "mass (kg)": 8.9319e22,
        "diameter (km)": 3643.2,
        "distance_to_planet (km)": 421700
      },
      {
        "name": "Europa",
        "mass (kg)": 4.7998e22,
        "diameter (km)": 3121.6,
        "distance_to_planet (km)": 670900
      }
    ],
    "reason": "Named after the king of the Roman gods as it is the largest and most massive planet in the Solar System."
  },
  {
    "name": "Saturn",
    "discover": "Known since antiquity",
    "distance (AU)": 9.58,
    "order": 6,
    "mass (kg)": 5.6834e26,
    "radius (km)": 58232.0,
    "density (g/cm³)": 0.687,
    "type": "газовая",
    "satellites": [
      {
        "name": "Titan",
        "mass (kg)": 1.3452e23,
        "diameter (km)": 5149.5,
        "distance_to_planet (km)": 1221870
      },
      {
        "name": "Rhea",
        "mass (kg)": 2.306e21,
        "diameter (km)": 1527.6,
        "distance_to_planet (km)": 527040
      },
      {
        "name": "Iapetus",
        "mass (kg)": 1.805e21,
        "diameter (km)": 1468.6,
        "distance_to_planet (km)": 3561300
      },
      {
        "name": "Dione",
        "mass (kg)": 1.095e21,
        "diameter (km)": 1122.8,
        "distance_to_planet (km)": 377400
      }
    ],
    "reason": "Named after the Roman god of agriculture and time, who was also the father of Jupiter in mythology."
  },
  {
    "name": "Uranus",
    "discover": "1781",
    "distance (AU)": 19.22,
    "order": 7,
    "mass (kg)": 8.681e25,
    "radius (km)": 25362.0,
    "density (g/cm³)": 1.27,
    "type": "прочее",
    "satellites": [
      {
        "name": "Titania",
        "mass (kg)": 3.527e21,
        "diameter (km)": 1577.8,
        "distance_to_planet (km)": 435900
      },
      {
        "name": "Oberon",
        "mass (kg)": 3.014e21,
        "diameter (km)": 1522.8,
        "distance_to_planet (km)": 583500
      },
      {
        "name": "Umbriel",
        "mass (kg)": 1.2e21,
        "diameter (km)": 1169.4,
        "distance_to_planet (km)": 266000
      },
      {
        "name": "Ariel",
        "mass (kg)": 1.35e21,
        "diameter (km)": 1157.8,
        "distance_to_planet (km)": 191000
      }
    ],
    "reason": "Named after the ancient Greek personification of the sky (Ouranos), the grandfather of Zeus/Jupiter."
  },
  {
    "name": "Neptune",
    "discover": "1846",
    "distance (AU)": 30.05,
    "order": 8,
    "mass (kg)": 1.0241e26,
    "radius (km)": 24622.0,
    "density (g/cm³)": 1.638,
    "type": "прочее",
    "satellites": [
      {
        "name": "Triton",
        "mass (kg)": 2.14e22,
        "diameter (km)": 2706.8,
        "distance_to_planet (km)": 354760
      },
      {
        "name": "Proteus",
        "mass (kg)": 4.4e19,
        "diameter (km)": 420.0,
        "distance_to_planet (km)": 117640
      },
      {
        "name": "Nereid",
        "mass (kg)": 3.1e19,
        "diameter (km)": 340.0,
        "distance_to_planet (km)": 5513800
      }
    ],
    "reason": "Named after the Roman god of the sea because of its deep ocean-blue appearance caused by methane in its atmosphere."
  }
]


# -------------------------- подготовка -------------------------

from pprint import pprint
from collections import defaultdict, Counter

# -------------------------- расчёт -------------------------

# ---------- тест 1 ----------

print('\n1. подсчёт планет')

print(f"всего сейчас планет: {len(data)}")

# ---------- тест 2 ----------

print('\n2. подсчёт планет по типам')

typed = Counter( [ p['type'] for p in data] )

print(f"всего сейчас планет по типам:\n{typed}")

# -------------------------- результаты -------------------------

# ~ 1. подсчёт планет
# ~ всего сейчас планет: 8

# ~ 2. подсчёт планет по типам
# ~ всего сейчас планет по типам:
# ~ Counter({'каменная': 4, 'газовая': 2, 'прочее': 2})

# -------------------------- обсуждение -------------------------

# ~ Астрофизические примечания к новым полям

# ~ Классификация Урана и Нептуна (type: "прочее"): В современной астрофизике эти планеты выделяют в отдельный класс «ледяные гиганты» (ice giants). В отличие от Юпитера и Сатурна, состоящих преимущественно из водорода и гелия, недра Урана и Нептуна заполнены высокотемпературной модификацией льда (водного, аммиачного и метанового), скрытой под массивной атмосферой. Из-за этого относить их просто к «газовым» некорректно.

# ~ Аномалия Сатурна (density): Плотность Сатурна составляет всего 0.687 г/см³, что ниже плотности жидкой воды (1 г/см³). Если бы существовал гипотетический океан подходящего размера, Сатурн держался бы на его поверхности.

# -------------------------- конец -------------------------
print()
