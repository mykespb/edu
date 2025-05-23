#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2025-05-23 2025-05-23 1.0

# ~ Во всех кружках

# ~ Есть данные о школьникоах и в каких кружках они участвуют.
# ~ Выписать тех, кто участвует сразу о всех кружках,
# ~ если такие школьники есть.

from pprint import pprint

pups = {
    'Cate': 'swimming dancing drawing' . split(),
    'Jane': 'swimming running' . split(),
    'Nick': 'drawing running' . split(),
    'Pete': 'dancing math chemistry swimming drawing running' . split(),
    'John': 'dancing math chemistry' . split(),
    }

# ~ pprint(pups)

kru = set()
for v in pups.values():
    kru |= set(v)

krulen = len(kru)
# ~ print(krulen, kru)   

print("most busy pups:", 
    *[k for k in pups if len(pups[k]) == krulen]
    or "No such pup"
    )
