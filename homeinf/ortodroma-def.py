#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-04-28 2026-04-28 1.0
# ortodroma-def.py

# ~ Ортодро́мия, ортодро́ма (от др.-греч. «ὀρθός» — «прямой» и «δρόμος» — «бег», «путь»[1]) в геометрии — кратчайшая линия между двумя точками на поверхности вращения, частный случай геодезической линии.

# ~ В картографии и навигации ортодромия — название кратчайшего расстояния между двумя точками на поверхности Земли. В судо- и самолётовождении, где Земля принимается за шар, ортодромия представляет собой дугу большого круга. Через две точки на земной поверхности, расположенные не на противоположных концах одного диаметра Земли, можно провести только одну ортодромию.

# ~ По 2 точкам рассчитать длину ортодромы.

# ~ https://ru.wikipedia.org/wiki/%D0%9E%D1%80%D1%82%D0%BE%D0%B4%D1%80%D0%BE%D0%BC%D0%B8%D1%8F
# ~ https://en.wikipedia.org/wiki/Haversine_formula
# ~ https://planetcalc.ru/722/
# ~ https://www.google.com/search?q=%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D0%B0+%D0%B3%D0%B0%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%BD%D1%83%D1%81%D0%BE%D0%B2&sourceid=chrome&ie=UTF-8
# ~ https://www.distance.to/

from math import asin, cos, pi, sin, sqrt
from pprint import pprint


def sign(a):
    return -1 if a < 0.0 else 1 if a > 0.0 else 0.0


def dms2d(d=0.0, m=0.0, s=0.0):
    return sign(d) * (abs(d) + m / 60 + s / 3600)


def deg2rad(a):
    return a * pi / 180


points = [
    # ~ city, latitude, langitude
    ("spb", deg2rad(dms2d(59, 57)), deg2rad(dms2d(30, 15))),
    ("msk", deg2rad(dms2d(55, 45, 2)), deg2rad(dms2d(37, 37, 3))),
    ("nsk", deg2rad(dms2d(55, 1)), deg2rad(dms2d(82, 55))),
    ("che", deg2rad(dms2d(55, 9)), deg2rad(dms2d(61, 24))),
    ("wash", deg2rad(38.898), deg2rad(-77.037)),
    ("paris", deg2rad(48.858), deg2rad(2.294)),
    ("cc", deg2rad(dms2d(-43, 31, 48)), deg2rad(dms2d(172, 37, 13))),
    ("well", deg2rad(dms2d(-41, 17, 20)), deg2rad(dms2d(174, 46, 38))),
]

# ~ wash = Washington, DC, USA
# ~ cc = Christchurch, NZ
# ~ well = Wellington, NZ

pprint(points)

# -------------------------------


def orto(p1, p2):
    if p1[0] == p2[0]:
        return 0.0

    dlat = p2[1] - p1[1]
    dlon = p2[2] - p1[2]
    R = 6371.0

    a = sin(dlat / 2) ** 2 + cos(p1[1]) * cos(p2[1]) * sin(dlon / 2) ** 2
    d = 2 * R * asin(sqrt(a))

    return d


# -------------------------------

print("\nspb - msk:", orto(points[0], points[1]))

# -------------------------------

print("\nfrom - to   ", end="")
for c1 in points:
    print(f"{c1[0]:>12}", end="")
print()

for c1 in points:
    print(f"{c1[0]:>12}", end="")
    for c2 in points:
        print(f"{orto(c1, c2):12.2f}", end="")
    print()


print("\n")
