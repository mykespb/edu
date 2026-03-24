#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / simple-5.py - testing classes
# 2026-03-09 2026-03-25 2.5

from datetime import date
from random import choice, random, randint, shuffle
from pprint import pprint

LIMIT = 10    # repetitions, or length of names' list

names = "Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey X-ray Yankee Zulu".split()

class Person:
    def __init__(self, name="Noname", bd=date.today(), sex=True):
        self.name = name
        self.bd = bd
        self.sex = sex

    @property
    def age(self):
        return date.today().year - self.bd.year

    def __str__(self):
        return f"Человек: имя='{self.name}', ДР='{self.bd}', пол={"М" if self.sex else "Ж"}; "

    def __repr__(self):
        return f"Person(name='{self.name}', bd=date({self.bd}), sex={self.sex})"


def main():
    print("Привет от классной программы!")

    assert LIMIT <= len(names)

    shuffle(names)

    myClass = []
    
    for istud in range(LIMIT):
        stud = Person(
            name=names[istud],
            bd=date(randint(1990, 2020), randint(1, 12), randint(1,28)),
            sex=choice([True, False])
            )
        myClass.append(stud)

    print("\nВот мой класс:", *myClass, sep="\n")

    oldest = sorted(myClass, key = lambda x: x.age)[-1]
    print(f"\nСтарейший: {oldest}\nпредставление: {repr(oldest)}\n")


if __name__ == "__main__":
    main()
