#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / main - testing classes
# 2026-03-09 2026-03-09 1.0

from datetime import date


class Person:
    def __init__(self, name = "Noname", bd = date.today(), sex = True):
        self.name = name
        self.bd = bd
        self.sex = sex

    @property
    def age(self):
        return date.today().year - self.bd.year

    def __str__(self):
        return f"Person(name='{self.name}', bd='{self.bd}', sex='{self.sex}')"


class Student(Person):
    def __init__(self, name = "Noname", bd = date.today(), sex = True, group = None, grade = 1):
        super().__init__(name, bd, sex)
        self.group = group
        self.grade = grade

    def __str__(self):
        return f"Student(name='{self.name}', bd='{self.bd}', sex='{self.sex}', group={self.group}, grade={self.grade})"


class Teacher(Person):

    MIN_SALARY = 100
    MAX_SALARY = 1000
    
    def __init__(self, name = "Noname", bd = date.today(), sex = True, groups = None, salary = 0):
        super().__init__(name, bd, sex)
        if groups is None:
            self.groups = []
        else:
            self.groups = groups
        self.salary = salary

    def add_group(self, gruppa):
        if gruppa not in self.groups:
            self.groups.append(gruppa)

    def del_group(self, gruppa):
        if gruppa in self.groups:
            self.groups.remove(gruppa)

    def set_salary(self, value):
        if Teacher.MIN_SALARY <= value <= Teacher.MAX_SALARY:
            self.salary = value
        else:
            raise ValueError

    def __str__(self):
        return f"Teacher(name='{self.name}', bd='{self.bd}', sex='{self.sex}', groups={self.groups}, salary={self.salary})"
            

def main():
    print("Hello from classes!")

    boy = Person(bd=date(2000, 3, 4))
    print(boy)
    boy.name = 'Юра'
    print(boy)
    print("age of boy:", boy.age)

    girl = Person(name='Алиса', sex=False)
    print(girl)

    stud1 = Student(name="Вася", group=4505)
    print(stud1)

    stud2 = Student(name="Катя", group=4705, grade=3)
    print(stud2)

    prep1 = Teacher(name='Иван Петрович', bd=date(1970, 1, 1))
    print(prep1)

    prep1.add_group(123)
    print(prep1)

    prep1.add_group(123)
    print(prep1)

    prep1.add_group(230)
    print(prep1)

    prep1.set_salary(100)
    print(prep1)

    try:
        prep1.set_salary(10000)
        print(prep1)
    except:
        print("Была ошибка с зарплатой в 10000 монет, но мы справились!")

    prep1.del_group(123)
    print(prep1)

    prep1.del_group(123)
    print(prep1)
    

if __name__ == "__main__":
    main()
