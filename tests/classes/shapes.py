#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / shapes.py - testing classes
# 2026-03-09 2026-03-09 1.1

# classes with geo-figures, step 2


from datetime import date
from random import choice, random
from math import sqrt


class Figure:
    
    def __init__(self, name = "Noname", cx = 0.0, cy = 0.0):
        self.cx = cx
        self.cy = cy
        self.name = "Figurka " + name

    @property
    def area(self):
        return 0.0

    @property
    def length(self):
        return 0.0

    # ~ @property
    # ~ def peri(self):
        # ~ return 0.0

    def __str__(self):
        return f"Фигура('{self.name}', {self.cx:.2f}, {self.cy:.2f})"

    def __repr__(self):
        return f"Figure('{self.name}', {self.cx:.2f}, {self.cy:.2f})"


class Point(Figure):
    
    def __init__(self, name = "Noname", cx = 0.0, cy = 0.0):
        super().__init__()
        self.name = "Tochka " + name


class Line(Figure):
    
    def __init__(self, name = "Noname", cx = 0.0, cy = 0.0, ex = 0.0, ey = 0.0):
        super().__init__()
        self.ex = ex
        self.ey = ey
        self.name = "Linia " + name

    @property
    def length(self):
        return sqrt( (self.cx-self.ex)**2 + (self.cy-self.ey)**2 )

    def __str__(self):
        return f"Figure('{self.name}', {self.cx:.2f}, {self.cy:.2f}, {self.ex:.2f}, {self.ey:.2f})"

    def __repr__(self):
        return f"Figure('{self.name}', {self.cx:.2f}, {self.cy:.2f}, {self.ex:.2f}, {self.ey:.2f})"


names = "Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey X-ray Yankee Zulu".split()

vowels = "aeiouy"

types = "Figure Point Line".split()


def main():

    lof = []    
    for i in range(10):

        newtype = choice(types)

        match newtype:
            case 'Point':
                f = Point(name = choice(names),
                    cx = random() * 10., cy = random() * 10.)
            case 'Line':
                f = Line(name = choice(names),
                    cx = random() * 10., cy = random() * 10.,
                    ex = random() * 10., ey = random() * 10.)
            case _:
                f = Figure(name = choice(names),
                    cx = random() * 10., cy = random() * 10.)
            
        print(f)
        lof.append((f, f.length))
        
    print(f"{lof=}")

    best = [fig for fig in lof if fig[0].name.lower().split()[1].startswith(tuple(vowels))]
    print(f"{best=}")

    max_sized = sorted(lof, key = lambda x: x[1], reverse=True)[0]
    print(f"{max_sized=}")
    

if __name__ == "__main__":
    main()

