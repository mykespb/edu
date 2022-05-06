#!/usr/bin/env python
# myke 2022-05-06 2022-05-06 1.0
# dict-rock.py

# ~ Есть некоторые сведения о русском роке.
# ~ Найти разную полезную информацию.

from dict_rock_data import *
from pprint import pp

# 1. просто распечатаем всё поальбомно
pp(coj)

# 2. сколько песен написано и издано за первые 3 года
year_start = min(x["year"] for x in coj)
print("начал издавать в", year_start, "году")
songs3 = []
for songs in [x["songs"] for x in coj if x["year"] < year_start+3]:
    songs3 += songs
print("\n\nпесни за 3 года:", songs3)
print("\nза 3 года издано песен", len(songs3))

# 3. а без повторов?
print("\n\nпесни за 3 года:", sorted(songs3))
print("\nза 3 года издано песен", len(set(songs3)))

# 4. полный алфавитный список песен
songs_all = []
for songs in [x["songs"] for x in coj]:
    songs_all += songs
salf = []
for song in songs_all:
    if song not in salf:
        salf.append(song)
salf.sort()
print("\n\nвсего песен:", len(salf))
print("всё по алфавиту:\n", salf)
