#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / simple-4.py - testing classes
# 2026-03-09 2026-03-24 2.2

from datetime import date
from random import random

class Person:
    def __init__(self, name="Noname", bd=date.today(), sex=True):
        self.name = name
        self.bd = bd
        self.sex = sex
        self.random = random()

    @property
    def age(self):
        return date.today().year - self.bd.year

    def __str__(self):
        return f"Person(name='{self.name}', bd='{self.bd}', sex={self.sex}, random={self.random:.3f})"


def main():
    print("Hello from classes!")

    boy = Person("Вася", date(2000, 3, 4))
    print(boy)
    
    boy.name = "Юра"
    print(boy)
    
    print("bot's age this year is", boy.age)

    girl = Person(name="Алиса", sex=False, bd=date(2000, 1, 13))
    print(girl)


if __name__ == "__main__":
    main()
