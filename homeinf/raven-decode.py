#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-03-27 2025-03-27 1.0
# raven-decode.py

# file with text of verse
file_raven = "tmp/raven-betaki.txt"

# file to get encoded message from
file_mess_coded = "tmp/text-coded.txt"

# secret message
# ~ message = """
# ~ Вот и первое заданье.
# ~ В три пятнадцать возле бани
# ~ (Может, раньше, а может — позже) остановится такси.
# ~ Надо сесть, связать шофера,
# ~ Разыграть простого вора,
# ~ А потом про этот случай раструбят по BBC.
# ~ И еще. Оденьтесь свеже,
# ~ И на выставке в Манеже
# ~ К вам приблизится мужчина с чемоданом — скажет он:
# ~ "Не хотите ли черешни?"
# ~ Вы ответите: "Конечно!"
# ~ Он вам даст батон с взрывчаткой — принесете мне батон.
# ~ """

# imports and setup

from collections import defaultdict
from random import choice

# program - prepare coder

abc = defaultdict(str)

print("Prepare coder.")

with open(file_raven, 'rt') as fin:
    text = fin.read()

for linum, txt in enumerate(text.lower().strip().split('\n'), 1):
    for pos, ch in enumerate(txt, 1):
        chlow = ch.lower()
        abc[(linum, pos)] = ch

# ~ print(abc)

print("Coder prepared.")

# program - encode message

print("Decoding started.")

got = ""

with open(file_mess_coded, "rt") as fin:
    coded = fin.read()

arr = list(map(int, coded.strip().split()))

for i in range(len(arr) // 2):

    p1, p2 = arr[i*2], arr[i*2+1]

    # ~ print(p1, p2)

    if p1 == p2 == 0:
        got += '\n'
        continue

    if (p1, p2) in abc:
        got += abc[(p1, p2)]
        # ~ print(".", end="")
    else:
        # ~ print("?", end="")
        ...
       

print(got)        

print("Decoding finished.")
