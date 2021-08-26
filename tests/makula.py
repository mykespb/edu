#!/usr/bin/env python3.9
# makula.py
# (C) Mikhail Kolodin, 2021
# ver. 2021-08-26 2021-08-27 1.4

# ----------------------------------------------

# ~ сбор макулатуры
# ~ дан список имён учеников класса.
# ~ известно, что каждый сдал столько кг макулатуры, сколько букв в его имени.
# ~ подсчитать результат класса.

# ~ дано:
names = "Вася Коля Иванушка Тимур Иннокентий Веста Мальвина".split()

# ~ решение:
kg = sum([len(x) for x in names])
print("\nученики", end=" ")
print(*names, sep=", ", end=" ")
print("всего сдали", kg, "кг")

# ----------------------------------------------

# ~ то же, есть списки, но на этот раз в них указаны и имена, и фамилии
# ~ задание то же

# ~ дано:
names = "Вася Васильков,Коля Колокольчиков,Иванушка Интернешнл,Тимур Батькович,Иннокентий Невинный,Веста Нордова,Мальвина Карлова".split(",")

# ~ решение:
pnames = [x.split()[0] for x in names ]
kg = sum([len(x) for x in pnames])
print("\nученики", end=" ")
print(*names, sep=", ", end=" ")
print("всего сдали", kg, "кг")

# ----------------------------------------------

# ~ классы соревнуются по сбору.
# ~ найти, какие классы собрали больше всего
# ~ (может быть несколько победителей)

# ~ дано:
got = 34, 15, 11, 10, 11, 17, 42, 42, 33, 23, 10
# ~ got = 34, 15, 11, 10, 11, 17, 42, 42, 33, 23, 90
# начиная с 0 элемента = 1 класс

# ~ решение:
print()
for klass, gotmoney in enumerate(got):
    print("класс", klass+1, "сдал", round(gotmoney), "кг")

maks  = max(got)
best = [i+1 for i, j in enumerate(got) if j == maks]
print("победили классы:" if len(best)>1 else "победил класс", end=" ")
print(*best, sep=", ")

# ----------------------------------------------

# ~ награды
# ~ за сбор всем выдали 1000 рублей
# ~ и распределили пропорционально сданным кг
# ~ сколько кому досталось?

# всего денег
money = 1000

# ~ решение
print()

# всего сдали
kgall = sum(got)

prop = [money * x / kgall for x in got]

print("всего денег:", round(sum(prop)))
for klass, gotmoney in enumerate(prop):
    print("класс", klass+1, "получил", round(gotmoney), "руб.")

# ----------------------------------------------
