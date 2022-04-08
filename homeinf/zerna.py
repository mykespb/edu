#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-08 2022-04-08 1.0
# zerna.py

import random

temp = [random.randint(-10, 10) for _ in range(100)]
print(temp)

cold = 0
for day in range(len(temp)):
    if temp[day] < 0:
        cold += 1
        if cold > 6:
            print("Замёрзли на", day, "день.")
            break
    else:
        cold = 0
else:
    print("Выжили и проросли!")
    
