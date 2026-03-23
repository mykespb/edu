#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / simple-1.py - testing classes
# 2026-03-09 2026-03-23 2.1

class Person:
    def __init__(self, name, bd, sex):
        self.name = name
        self.bd = bd
        self.sex = sex


def main():
    print("Hello from classes!")

    boy = Person("Вася", '2000-03-04', True)
    print(boy)
    
    boy.name = "Юра"
    print(boy)

    girl = Person(name="Алиса", sex=False, bd='2000-01-13')
    print(girl)


if __name__ == "__main__":
    main()
