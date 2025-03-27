#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-03-27 2025-03-27 1.0
# raven-encode.py

# file with text of verse
file_raven = "tmp/raven-betaki.txt"

# file to code message to
file_mess_coded = "tmp/text-coded.txt"

# secret message
message = """
Вот и первое заданье.
В три пятнадцать возле бани
(Может, раньше, а может — позже) остановится такси.
Надо сесть, связать шофера,
Разыграть простого вора,
А потом про этот случай раструбят по BBC.
И еще. Оденьтесь свеже,
И на выставке в Манеже
К вам приблизится мужчина с чемоданом — скажет он:
"Не хотите ли черешни?"
Вы ответите: "Конечно!"
Он вам даст батон с взрывчаткой — принесете мне батон.
"""

# imports and setup

from collections import defaultdict
from random import choice

# program - prepare coder

abc = defaultdict(list)

print("Prepare coder.")

with open(file_raven, 'rt') as fin:
    text = fin.read()

for linum, txt in enumerate(text.lower().strip().split('\n'), 1):
    for pos, ch in enumerate(txt, 1):
        chlow = ch.lower()
        abc[chlow].append((linum, pos))

print("Coder prepared.")

# program - encode message

print("Encoding started.")

with open(file_mess_coded, "wt") as fout:

    for ch in message.strip():

        if ch == '\n' or ch == '\r':
            outta = f"0 0 "
            fout.write(outta)
            continue
        
        chlow = ch.lower()
        if chlow not in abc:
            chlow = '?'

        loca = choice(abc[chlow])
        outta = f"{loca[0]} {loca[1]} "

        fout.write(outta)

print("Encoding finished.")
