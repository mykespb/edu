#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / simple-6.py - testing classes
# 2026-03-09 2026-03-25 2.4

from datetime import date, datetime
from random import choice, random, randint, shuffle
from pprint import pprint


class Person:

    quantity = 0

    def __init__(self, name="Noname", bd=date.today(), sex=True):
        self.name = name
        self.bd = bd
        self.sex = sex

        Person.quantity += 1
        self.number = Person.quantity

    @staticmethod
    def howmany():
        return Person.quantity

    @property
    def age(self):
        return date.today().year - self.bd.year

    def __str__(self):
        return f"Person(name='{self.name}', bd='{self.bd}', sex={self.sex}, number={self.number})"

    def __repr__(self):
        return f"Person(name='{self.name}', bd='{self.bd}', sex={self.sex}, number={self.number})"


def main():
    print("Hello from classes!")

    names = "Alfa Bravo Charlie Delta Echo Foxtrot Golf Hotel India Juliett Kilo Lima Mike November Oscar Papa Quebec Romeo Sierra Tango Uniform Victor Whiskey X-ray Yankee Zulu".split()
    shuffle(names)

    myClass = []
    for istud in range(10):
        stud = Person(
            name=names[istud],
            bd=date(randint(1990, 2020), randint(1, 12), randint(1,28)),
            sex=choice([True, False])
            )
        myClass.append(stud)

    print("\nMy class is:", *myClass, sep="\n")

    oldest = sorted(myClass, key = lambda x: x.age)[-1]
    print("\nThe oldest is:", oldest, "\n")

    print("How many persons are there:", Person.howmany(), "\n")

   

if __name__ == "__main__":
    main()
