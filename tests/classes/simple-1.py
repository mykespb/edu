#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / simple-1.py - testing classes
# 2026-03-09 2026-03-30 2.3

class Person:
    
    def __init__(self, name, bd, sex):
        self.name = name
        self.bd = bd
        self.sex = sex


def main():
    print("Hello from classes!")

    boy = Person("Вася", '2000-03-04', True)
    print(boy)

    print(boy.name)
    print(boy.bd)
    print(boy.sex)
    
    boy.name = "Юра"
    print(boy)

    print(boy.name)
    print(boy.bd)
    print(boy.sex)
    
    girl = Person(name="Алиса", sex=False, bd='2000-01-13')
    print(girl)

    print(girl.name)
    print(girl.bd)
    print(girl.sex)
    

if __name__ == "__main__":
    main()


# ~ from datetime import date, datetime
# ~ d = datetime.strptime('2026-03-30' , '%Y-%m-%d')
# ~ print(d.date())
