#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-05-23 2025-05-26 1.4

# ~ Во всех кружках

# ~ Есть данные о школьниках и в каких кружках они участвуют.
# ~ Выписать тех, кто участвует сразу во всех кружках,
# ~ если такие школьники есть.

from pprint import pprint

pups = {
    'Kate': 'swimming dancing drawing drawing drawing drawing drawing drawing drawing' . split(),
    'Jane': 'swimming running' . split(),
    'Nick': 'drawing running' . split(),
    'Pete': 'dancing math chemistry swimming drawing running' . split(),
    'John': 'dancing math chemistry' . split(),
    'Mary': 'dancing math chemistry swimming drawing running' . split(),
    # ~ 'Joker': 'go went gone' . split(),
    }

pprint(pups)

# ~ kru = set()
# ~ for v in pups.values():
    # ~ kru |= set(v)

krulen = len( kru := set() . union (*map(set, pups.values() ) ) )

# ~ kru = set() . union (*map(set, pups.values() ) )
# ~ krulen = len(kru)
# ~ print(krulen, kru)   

print("Most busy pups:", 
    ", " .join ( [k for k in pups if set(pups[k]) == kru] )
    # ~ ", " .join ( [k for k in pups if len(set(pups[k])) == krulen] )
    or "No such pup"
    )
