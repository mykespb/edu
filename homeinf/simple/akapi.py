#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-08 2022-04-08 1.0
# akapi.py

# Выходят как-то из бара акапи и капибара.

akapi = 5
kapi  = 8

# ~ debug = 0
debug = 1

days = 365

akdrank = akapi
kadrank = kapi

day = 1
if debug:
    print(day, "акапи пьёт")
if debug:
    print(day, "капибара пьёт")

aknext = 1 + akapi + 1
kanext = 1 + kapi + 1

for day in range(2, days+1):
    if day == aknext and day == kanext:
        aknext += akapi + 1
        kanext += kapi + 1
        if debug:
            print(day, "разбежались")
        continue

    if day == aknext:
        akdrank += akapi
        aknext  += akapi + 1
        if debug:
            print(day, "акапи пьёт")
        continue

    if day == kanext:
        kadrank += kapi
        kanext  += kapi + 1
        if debug:
            print(day, "капибара пьёт")
        continue

print(f"\nвыпили:\nакапи: {akdrank:10}\nкапибара: {kadrank:7}\nвсего: {akdrank+kadrank:10}")
