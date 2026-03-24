#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / simple-2.py - testing classes
# 2026-03-09 2026-03-24 2.3

from datetime import date


class Person:
    def __init__(self, name="Noname", bd=date.today(), sex=True):
        self.name = name
        self.bd = bd
        self.sex = sex

    def __str__(self):
        return f"Person(name='{self.name}', bd='{self.bd}', sex={self.sex})"


def main():
    print("Hello from classes!")

    boy = Person("Вася", '2000-03-04')
    print(boy)
    
    boy.name = "Юра"
    print(boy)

    girl = Person(name="Алиса", sex=False, bd='2000-01-13')
    print(girl)

    someBody = Person()
    print(someBody)


if __name__ == "__main__":
    main()
