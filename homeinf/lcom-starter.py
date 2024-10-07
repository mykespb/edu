#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2021
# 2024-10-07 2024-10-07 1.0
# lcom-starter.py

# Играем со списковыми включениями

import random

# Получить знакопеременный список натуральных чисел до 10.
# Типа [1, -2, 3, -4, …]

a = [ (-1)**(i+1) * i for i in range(1, 11)]

print(f"{a=}")
