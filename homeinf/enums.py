#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2026-04-27 2026-04-27 1.5
# enums.py

# ~ Пробы перечислений.

from dataclasses import dataclass
from enum import Enum

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
# ~ The end.
# ~ -------------------------------------
""")
