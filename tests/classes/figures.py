#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / figures.py - testing classes
# 2026-03-09 2026-03-09 1.1

# classes with geo-figures, step 1

from datetime import date
from random import choice, random


class Figure:
    def __init__(self, name = "Noname", cx = 0.0, cy = 0.0):
        self.cx = cx
        self.cy = cy
        self.name = name

    @property
    def area(self):
        return 0.0

    # ~ @property
    # ~ def peri(self):
        # ~ return 0.0

    def __str__(self):
        return f"Figure({self.name}, {self.cx:.2f}, {self.cy:.2f})"

    def __repr__(self):
        return f"Figure({self.name}, {self.cx:.2f}, {self.cy:.2f})"


names = "Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey X-ray Yankee Zulu".split()

vowels = "aeiouy"


def main():

    lof = []    
    for i in range(10):
        f = Figure(name = choice(names), cx = random() * 10., cy = random() * 10.)
        print(f)
        lof.append(f)
    print(f"{lof=}")

    best = [fig for fig in lof if fig.name.lower().startswith(tuple(vowels))]
    print(f"{best=}")
    

if __name__ == "__main__":
    main()

