#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2026-04-27 2026-04-27 1.7
# enums.py

# ~ Пробы перечислений.

from dataclasses import dataclass
from enum import Enum, unique, auto

print("""
# ~ -------------------------------------
# ~ test -1
# ~ -------------------------------------
""")

# ~ Constants:

# ~ ver. 1

total = 50
good  = 25

gp = 25 / 50

print(f"{good=} of {total=} is {gp=}")

# ~ ver. 2

total = 100
good  = 25

gp = 25 * 100 / 100

print(f"{good=} of {total=} is {gp=}%")

# м.б. убрать это:   * 100 / 100  ???

gp = 25

# всегда???

# ~ ver. 3

total = 120
good  = 25

gp = 25 * 100 / 120

print(f"{good=} of {total=} is {gp=:.2f}")

# ~ ver. 4

total = 120
good  = 25

PERCENT = 100

gp = 25 * PERCENT / 120

print(f"{good=} of {total=} is {gp=:.2f}")


print("""
# ~ -------------------------------------
# ~ test 0
# ~ -------------------------------------
""")

# ~ Constants:

ONE = 1
TWO = 2
THREE = 3

print(ONE, TWO, THREE)

# ~ => 1 2 3

print(f"{ONE=}, {TWO=}, {THREE=}")

# ~ => ONE=1, TWO=2, THREE=3

print(ONE + TWO == THREE)

# ~ => True


print("""
# ~ -------------------------------------
# ~ test 1
# ~ -------------------------------------
""")


class Role(Enum):
    BOSS = "The main boss"
    MANAGER = "Middle manager"
    PROGER = "Software engineer"


person1 = Role.BOSS
print(person1)

person2 = Role.MANAGER
print(person2)

person3 = Role.PROGER
print(person3)
person4 = Role.PROGER
print(person4)

staff = person1, person2, person3, person4

print("The staff", end=": ")

for person in staff:
    print(person, end=", ")

# ~ Role.BOSS
# ~ Role.MANAGER
# ~ Role.PROGER
# ~ Role.PROGER
# ~ The staff: Role.BOSS, Role.MANAGER, Role.PROGER, Role.PROGER,
print()

print("""
# ~ -------------------------------------
# ~ test 2
# ~ -------------------------------------
""")


@dataclass
class Employer:
    name: str
    role: Role


emp1 = Employer("Jim", Role.BOSS)
emp2 = Employer("Jame", Role.MANAGER)
emp3 = Employer("Judith", Role.PROGER)
emp4 = Employer("Jack", Role.PROGER)

company = emp1, emp2, emp3, emp4

print("The company", end=": ")

for emp in company:
    print(emp)

for emp in company:
    print(f"{emp.name} is {emp.role}")


# ~ The company: Employer(name='Jim', role=<Role.BOSS: 'The main boss'>)
# ~ Employer(name='Jame', role=<Role.MANAGER: 'Middle manager'>)
# ~ Employer(name='Judith', role=<Role.PROGER: 'Software engineer'>)
# ~ Employer(name='Jack', role=<Role.PROGER: 'Software engineer'>)
# ~ Jim is Role.BOSS
# ~ Jame is Role.MANAGER
# ~ Judith is Role.PROGER
# ~ Jack is Role.PROGER

print("""
# ~ -------------------------------------
# ~ test 3
# ~ -------------------------------------
""")

from math import pi

class Planet(Enum):
    MERCURY = (90.39, 3.3e23)
    VENUS   = (0.72,  4.87e24)
    EARH    = (1.,    5.97e24)

    def __init__(self, distance_from_sun, mass):
        self.distance_from_sun = distance_from_sun
        self.mass = mass

    @property
    def density(self):
        return self.mass / ( 4/3. * pi * (self.distance_from_sun ** 3))

print(Planet.EARH.density)
print(f"{Planet.EARH.density=}")


# ~ 1.425232515387923e+24
# ~ Planet.EARH.density=1.425232515387923e+24

print("""
# ~ -------------------------------------
# ~ test 4
# ~ -------------------------------------
""")

@unique
class UniqueColor(Enum):
    RED    = 1
    BLUE   = 2
    # ~ GREEN  = 3
    BLACK  = 3

uc = UniqueColor.BLACK

print(f"{UniqueColor.BLACK=}")
# ~ ValueError: duplicate values found in <enum 'UniqueColor'>: BLACK -> GREEN
# ~ UniqueColor.BLACK=<UniqueColor.BLACK: 3>


print("""
# ~ -------------------------------------
# ~ test 5
# ~ -------------------------------------
""")

@unique
class UniqueColor(Enum):
    RED    = auto()
    BLUE   = auto()
    BLACK  = auto()

uc = UniqueColor.BLACK

print(f"{UniqueColor.BLACK=}")
# ~ UniqueColor.BLACK=<UniqueColor.BLACK: 3>


print("""
# ~ -------------------------------------
# ~ test 6
# ~ -------------------------------------
""")

# ~ https://docs.python.org/3/library/enum.html
# ~ https://docs.python.org/3/howto/enum.html

Color = Enum('Color', [('RED', 1), ('GREEN', 2), ('BLUE', 3)])

some_color = Color.RED

print(some_color)
print(some_color in Color)

# ~ Color.RED
# ~ True

print(dir(Color))
# ~ ['BLUE', 'GREEN', 'RED', '__class__', '__contains__', '__doc__', '__getitem__', '__init_subclass__', '__iter__', '__len__', '__members__', '__module__', '__name__', '__qualname__']

print(len(Color))
# ~ 3

print(Color.__members__)
# ~ {'RED': <Color.RED: 1>, 'GREEN': <Color.GREEN: 2>, 'BLUE': <Color.BLUE: 3>}

print(list(reversed(Color)))
# ~ [<Color.BLUE: 3>, <Color.GREEN: 2>, <Color.RED: 1>]

print(some_color.name, "=>", some_color.value)
# ~ RED => 1


print("""
# ~ -------------------------------------
# ~ The end.
# ~ -------------------------------------
""")
