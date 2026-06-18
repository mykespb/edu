#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2026-06-18 2026-06-18 1.0
# bridge-europe.py

# ~ Дана карта некоторых стран Европы в виде списка смежности.
# ~ Определить, можно ли проехать по этим странам так, чтобы побывать в каждой стране
# ~ и пересечь каждую границу по 1 разу.
# ~ Если да, то какие страны будут в начале и в конце поездки?
# ~ Или можно проехать по-разному?
# ~ Если совесм нет, то м.б. можно выкинуть из набора стран 1 страну так, чтобы всё же проехать?

from pprint import pprint
from collections import Counter

mapa = """
Spain - Portugal
Spain - France
France - Belgium
France - Luxemburg
France - Germany
France - Switzerland
France - Italy
Finland - Sweden
Sweden - Norway
Estonia - Latvia
Latvia - Lithuania
Lithuania - Poland
Poland - Germany
Poland - Czechia
Czechia - Slovakia
Slovakia - Hungary
Hungary - Romania
Romania - Bulgaria
Bulgaria - Macedonia
Serbia - Macedonia
Greece - Macedonia
Albania - Macedonia
Bulgaria - Greece
Greece - Albania
Albania - Montenegro
Montenegro - Serbia
Hungary - Serbia
Hungary - Austria
Belgium - Netherlands
Belgium - Luxemburg
Belgium - Germany
Austria - Switzerland
Italy - Switzerland
Austria - Czech
Germany - Czech
Germany - Denmark
Hungary - Croatia
Serbia - Croatia
Bosnia - Croatia
Slovenia - Croatia
Italy - Croatia
Belarus - Latvia
Belarus - Lithuania
Belarus - Poland
Belarus - Ukraine
Poland - Ukraine
Moldova - Ukraine
Moldova - Romania
Slovakia - Ukraine
Romania - Ukraine
"""

pairs = []

for line in mapa.strip().split('\n'):
    c1, _, c2 = line.strip().split()
    pairs.append((c1, c2))
    pairs.append((c2, c1))

pprint(pairs)

cnt = Counter( [ c[0] for c in pairs ])

pprint(cnt)

odds = sum( [ (1 if x%2 == 1 else 0) for x in cnt.values() ] )

print(f"нечётных стран: {odds}")

if odds == 0:
    print("проехать можно, по-разному")
elif odds == 2:
    print("проехать можно, крайние страны: ", [x for x in cnt.keys() if cnt[x] %2 == 1] )
elif odds == 1:
    print("проехать нельзя, но если выкинуть из маршрута страну: ", [x for x in cnt.keys() if cnt[x] % 2 == 1], ", то можно")
else:
    print("проехать никак нельзя")
