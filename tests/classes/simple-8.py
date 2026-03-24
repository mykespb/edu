from datetime import date, datetime
from random import random


class Person:
    def __init__(self, name="Noname", bd=date.today(), sex=True):
        self.name = name
        self.bd = bd
        self.sex = sex

    def age(self):
        return date.today().year - self.bd.year

    def __str__(self):
        return f"Человек {self.name} {self.age()} лет от роду"

    def __repr__(self):
        return f"Person(name='{self.name}', bd='{self.bd}', sex={self.sex})"


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


def main():
    print("Hello from classes!")

    # Dates  -----------------------------------------------

    print()
    today = datetime.today()

    print("simple:", today)
    print("str:", str(today))
    print("repr:", repr(today))

    # Persons -----------------------------------------------

    print()
    boy = Person("Вася", date(2000, 3, 4))
    print(boy)

    boy.name = "Юра"
    print(boy)

    print("str: ", boy.__str__())
    print("repr:", boy.__repr__())

    print("str: ", str(boy))
    print("repr:", repr(boy))

    print("boy's age this year is", boy.age())

    girl = Person(name="Алиса", sex=False, bd=date(2000, 1, 13))
    print(girl)

    # Points -----------------------------------------------

    print()

    p1 = Point()
    print(p1)
    print(p1.x, p1.y)

    p2 = Point(3.14, 5.25)
    print(p2)
    print(p2.x, p2.y)

    p3 = Point(y=2.72, x=9.81)
    print(p3)
    print(p3.x, p3.y)


if __name__ == "__main__":
    main()
