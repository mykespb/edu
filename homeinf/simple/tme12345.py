#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-03-28 2022-03-28 1.0
# tme12345.py
# https://www.youtube.com/watch?v=n9BhA-9ia2U
# Как решать числовой ребус. Найдите неизвестные цифры в примере
# 1275 просмотров28 мар. 2022 г.

sol = 0

for a in range(1, 10):
    for b in range(10):
        for c in range(10):
            if (
                (a*100 + b*10 +5) * c // 100 == 3 and
                (a*100 + b*10 +5) * 4 // 100 % 10 == 2 and
                (a*100 + b*10 +5) * (40+c) // 10000 == 1
                ):
                    sol += 1
                    print(f"\nsolution#{sol}:\n  {a}{b}5\n   4{c}\n-----\n  {(a*100+b*10+5)*c}\n{(a*100+b*10+5)*4}\n-----\n{(a*100+b*10+5)*(40+c)}")

print(f"\ntotal solutions: {sol}")



    # ~ solution#1:
      # ~ 305
       # ~ 41
    # ~ -----
      # ~ 305
    # ~ 1220
    # ~ -----
    # ~ 12505

    # ~ solution#2:
      # ~ 315
       # ~ 41
    # ~ -----
      # ~ 315
    # ~ 1260
    # ~ -----
    # ~ 12915

    # ~ total solutions: 2
