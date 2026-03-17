#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / figures.py - testing classes
# 2026-03-09 2026-03-17 1.3

# classes with geo-figures, step 1: called Point

from datetime import date
from random import choice, random
from pprint import pprint

class Point:
    def __init__(self, name = "Noname", cx = 0.0, cy = 0.0):
        self.cx = cx
        self.cy = cy
        self.name = name
        self.random = random()

    # ~ def __str__(self):
        # ~ return f"ThePoint({self.name}, {self.cx:.2f}, {self.cy:.2f}, {self.random:.2f})"

    # ~ def __repr__(self):
        # ~ return f"Point({self.name}, {self.cx:.2f}, {self.cy:.2f}, {self.random:.2f})"


names = "Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey X-ray Yankee Zulu".split()

vowels = "aeiouy"


def main():

    lof = []    
    for i in range(10):
        f = Point(name = choice(names), cx = random() * 10., cy = random() * 10.)
        print(f)
        lof.append(f)
    print(f"{lof=}")
    pprint(lof)

    best = [fig for fig in lof if fig.name.lower().startswith(tuple(vowels))]
    print(f"{best=}")
    pprint(best)
    

if __name__ == "__main__":
    main()

