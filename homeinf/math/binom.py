#!/usr/bin/env python
# Miklhail (myke) Kolodin
# math / binom.py
# 2026-07-29 2026-07-29 1.0
# Треугольник Паскаля
# Построить ТП из n строк.

def tp(n):
    row = [1]
    width = 8

    for rn in range(1, n+1):
        
        print(' ' * ((n-rn) * width // 2), end='')
        for p in row:
            if p:
                print(f"{p:{width}}", end='')
            # ~ else:
                # ~ break
        print()

        row = [0] + row + [0]

        for i in range(len(row)-1):
            row[i] += row[i+1]

tp(10)
   

                                           # ~ 1
                                       # ~ 1       1
                                   # ~ 1       2       1
                               # ~ 1       3       3       1
                           # ~ 1       4       6       4       1
                       # ~ 1       5      10      10       5       1
                   # ~ 1       6      15      20      15       6       1
               # ~ 1       7      21      35      35      21       7       1
           # ~ 1       8      28      56      70      56      28       8       1
       # ~ 1       9      36      84     126     126      84      36       9       1


# ~ https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B5%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA_%D0%9F%D0%B0%D1%81%D0%BA%D0%B0%D0%BB%D1%8F

# ~ https://ru.wikipedia.org/wiki/%D0%91%D0%B8%D0%BD%D0%BE%D0%BC%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%BA%D0%BE%D1%8D%D1%84%D1%84%D0%B8%D1%86%D0%B8%D0%B5%D0%BD%D1%82

# ~ https://ru.wikipedia.org/wiki/%D0%91%D0%B8%D0%BD%D0%BE%D0%BC_%D0%9D%D1%8C%D1%8E%D1%82%D0%BE%D0%BD%D0%B0

# ~ https://ru.wikipedia.org/wiki/%D0%A4%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D1%8B_%D1%81%D0%BE%D0%BA%D1%80%D0%B0%D1%89%D1%91%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE_%D1%83%D0%BC%D0%BD%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F_%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%D1%87%D0%BB%D0%B5%D0%BD%D0%BE%D0%B2

# ~ https://ru.wikipedia.org/wiki/%D0%91%D0%B8%D0%BD%D0%BE%D0%BC

