#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# langs-europe.py
# 2026-06-24 2026-06-24 1.0

# ~ перечисли 50 основных европейских разговорных языков в формате list[dict], указав:
# ~ - name; название,
# ~ - people: сколько человек говорит,
# ~ - worsd: сколько слов  в языке,
# ~ - diff: относительную сложность для русскоговорящего.

# --------------- данные --------------------


# --------------- обработка --------------------

from collections import Counter, defaultdict
from pprint import pprint

print("1. сгруппировать языки по сложности, вывести по группам по алфавиту")

gl = defaultdict(list)

for lang in langs:
    gl[lang['diff']] .append( lang['name'] )

for g in gl.values():
    g.sort()

pprint(gl)

# --------------- результат --------------------


# --------------- конец --------------------
