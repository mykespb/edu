#!/usr/bin/env python
# Mikhail (myke) Kolodin
# institutes.py
# 2025-02-15 2025-03-31 2.1

# ~ Институты
# ~ Названия институтов часто начинаются на первые буквы соответствующих городов.
# ~ Определить, какие институты находятся в каких городах.
# ~ Показать в алфавитном порядке.

cities = "Новосибирск Ленинград Москва"

institutes = "ЛГУ МГУ НГУ ЛИАП ЛЭТИ ЛИТМО МПИ ЛИК ЛМИ1 ЛПИ МПИ МИСиС НЭТИ ЛИСИ ЛИВТ"

citylist = sorted(cities.strip().split())
print(citylist)

instlist = sorted(institutes.strip().split())
print(instlist)

# ~ cabr = {}

# ~ for city in citylist:
    # ~ cabr[city[0]] = city

# ~ for city in citylist:
    # ~ first = city[0]
    # ~ print(cabr[first], end=" : ")
    # ~ for iname in instlist:
        # ~ if iname[0] == first:
            # ~ print(iname, end=", ")
    # ~ print()


for city in citylist:

    print(city, end=": ")
    
    for inst in instlist:
        if inst[0] == city[0]:
            print(inst, end=", ")
    print()
    

# ~ Ленинград : ЛГУ, ЛИАП, ЛИВТ, ЛИК, ЛИСИ, ЛИТМО, ЛМИ1, ЛПИ, ЛЭТИ, 
# ~ Москва : МГУ, МИСиС, МПИ, МПИ, 
# ~ Новосибирск : НГУ, НЭТИ, 
