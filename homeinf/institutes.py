#!/usr/bin/env python
# Mikhail (myke) Kolodin
# institutes.py
# 2025-02-15 2025-02-15 1.1

# ~ Институты
# ~ Известно, что названия институтов часто начинаются на первые буквы соответствующих городов.
# ~ Определить, какие институты находятся в каких городах.
# ~ Показать в алфавитном порядке.

cities = "Ленинград Москва Новосибирск"

institutes = "ЛГУ МГУ НГУ ЛИАП ЛЭТИ ЛИТМО МПИ ЛИК ЛМИ1 ЛПИ МПИ МИСиС НЭТИ ЛИСИ ЛИВТ"

cabr = {}

for city in (cl := cities.strip().split()):
    cabr[city[0]] = city

insts = sorted(institutes.strip().split())

for city in sorted(cl):
    first = city[0]
    print(cabr[first], end=" : ")
    for iname in insts:
        if iname[0] == first:
            print(iname, end=", ")
    print()


# ~ Ленинград : ЛГУ, ЛИАП, ЛИВТ, ЛИК, ЛИСИ, ЛИТМО, ЛМИ1, ЛПИ, ЛЭТИ, 
# ~ Москва : МГУ, МИСиС, МПИ, МПИ, 
# ~ Новосибирск : НГУ, НЭТИ, 
