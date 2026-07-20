#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-04-08 2022-04-08 1.0
# class-pairs.py

# ~ ДЗ5. Классные пары
# ~ В классе есть мальчики и девочки, определяемые как
# ~ NUM = 12; ROST = 160; DIFF = 20; ALLOWED = 10
# ~ boys  = [ROST+random.randint(-DIFF, DIFF) for n in range(NUM)]
# ~ girls = [ROST+random.randint(-DIFF, DIFF) for n in range(NUM)]
# ~ Удастся ли их построить в пары “мальчик+девочка”,
# ~ если требуется, чтобы их росты в каждой паре
# ~ отличались не более чем на ALLOWED см.

import random

NUM = 12; ROST = 160; DIFF = 20; ALLOWED = 10
boys = [ROST+random.randint(-DIFF, DIFF) for n in range(NUM)]
girls = [ROST+random.randint(-DIFF, DIFF) for n in range(NUM)]

boys.sort()
girls.sort()

print("boys: ", boys)
print("girls:", girls)

for p in zip(boys, girls):
    if abs(p[0]-p[1]) > ALLOWED:
        print("увы, не получилось...")
        break
else:
    print("нормально построились!")

    
# ~ boys:  [141, 143, 143, 153, 158, 161, 163, 169, 169, 170, 170, 172]
# ~ girls: [140, 143, 146, 147, 151, 155, 162, 162, 168, 171, 174, 174]
# ~ нормально построились!

# ~ boys:  [142, 145, 146, 147, 152, 152, 160, 167, 174, 174, 176, 178]
# ~ girls: [140, 141, 141, 142, 142, 144, 153, 154, 156, 173, 173, 176]
# ~ увы, не получилось...
