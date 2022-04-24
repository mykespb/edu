#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-08 2022-04-23 2.0
# akapi-short.py

akapi = 5     # len("akapi")
kapi  = 8     # len("kapibara")

days = 365    # year length

akdrank = akapi
kadrank = kapi

day = 1

aknext = 1 + akapi + 1
kanext = 1 + kapi + 1

for day in range(2, days+1):
    if day == aknext and day == kanext:
        aknext += akapi + 1
        kanext += kapi + 1
        continue

    if day == aknext:
        akdrank += akapi
        aknext  += akapi + 1
        continue

    if day == kanext:
        kadrank += kapi
        kanext  += kapi + 1
        continue

print(f"\nвыпили:\nакапи: {akdrank:10}\nкапибара: {kadrank:7}\nвсего: {akdrank+kadrank:10}")
