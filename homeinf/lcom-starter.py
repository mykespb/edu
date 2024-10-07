#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2024-10-07 2024-10-07 2.0
# lcom-starter.py

# import random
from pprint import pp, pprint
    
# Играем со списковыми включениями

def signrow():
    """Получить знакопеременный список натуральных чисел до 10"""
    # Типа [1, -2, 3, -4, …]
    a = [ (-1)**(i+1) * i for i in range(1, 11)]
    print(a)

# signrow()

def lorem():
    """lorem ipsum"""

    import string
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    chars = string.ascii_lowercase
    lst = sorted([w.lower() for w in lorem.replace(',', '').replace('.', '').split()])
    print(f"{lst}")

# lorem()

# ---

def triarray(size=3):
    """make triangle array"""
    
    return [ [ i for i in range(1, line+1) ] for line in range(1, size+1)]

print("--- as print ---")
print(triarray())
print(triarray(4))
print(triarray(10))

print("--- as pretty print ---")
pprint(triarray())
pprint(triarray(4))
pprint(triarray(10))

# exit(1)

# ---
