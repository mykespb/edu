#!/usr/bin/env python
# Miklhail (myke) Kolodin
# classes / mainer-mult.py - testing classes
# 2026-03-09 2026-03-10 1.3

from datetime import date


class Person:
    def __init__(self, name = "Noname", bd = date.today(), sex = True):
        self.name = name
        self.sex = sex
        if bd <= date.today():
            self.bd = bd
        else:
            self.bd = date.today()
            raise ValueError

    @property
    def age(self):
        return date.today().year - self.bd.year

    @property
    def birth(self):
        return self.bd

    @birth.setter
    def birth(self, value):
        if value > date.today():
            raise ValueError
        self.bd = value

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


class Aspirant(Student, Teacher):
    def __init__(self,
        name = "Noname", bd = date.today(), sex = True,
        group = None, grade = 1,
        groups = None, salary = 0):

        self.name = name
        self.sex = sex
        self.bd = bd
        self.group = group
        self.grade = grade
        if groups is None:
            self.groups = []
        else:
            self.groups = groups
        self.salary = salary

    def __str__(self):
        return f"Aspirant(name='{self.name}', bd='{self.bd}', sex='{self.sex}', groups={self.groups}, salary={self.salary}, group={self.group}, grade={self.grade})"
        

def main():
    print("Hello from classes!")

    # Person ------------------------------------------------
    
    boy = Person(bd=date(2000, 3, 4))
    print(boy)
    boy.name = 'Юра'
    print(boy)
    print("age of boy:", boy.age)

    girl = Person(name='Алиса', sex=False)
    print(girl)

    print("boy's birthday:", boy.birth)

    try:
        noman = Person('Некто', date(2030, 1, 1))
        print("noman:", noman)
    except:
        print("Гость из будущего 2030 не принят.")
        noman = Person('Новак', date(1999, 3, 5))

    print("Noman 1:", noman)
    print("Noman's birth:", noman.birth)

    try:
        noman.birth = date(2010, 11, 11)
        print("Reset noman:", noman)
    except:
        print("Гость из будущего 2010 не принят.")

    print("Noman 2:", noman)
    print("Noman's birth:", noman.birth)

    # Student ------------------------------------------------
    
    stud1 = Student(name="Вася", group=4505)
    print(stud1)

    stud2 = Student(name="Катя", group=4705, grade=3)
    print(stud2)

    # Teacher ------------------------------------------------

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

    # Aspirant ------------------------------------------------

    asp1 = Aspirant(name = 'Сверховный', bd = date(1968, 3, 20))
    print("аспирант 1:", asp1)
    print("его возраст", asp1.age)

    asp2 = Aspirant(name = 'Кромешная', bd = date(2001, 6, 10), sex = False,
        group=1103,
        groups=[123, 234, 56], salary=120)
    print("аспирант 2:", asp2)
    print("его возраст", asp2.age)
    

if __name__ == "__main__":
    main()


# ~ Полезно:
# ~ https://habr.com/ru/articles/1000378/
# ~ https://skillbox.ru/media/code/kak-izbezhat-putanitsy-v-kode-ili-kratkiy-kurs-oop-na-python/
