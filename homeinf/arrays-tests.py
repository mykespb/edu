#!/usr/bin/env python
# Mikhail (myke) Kolodin
# 2025-03-07 2025-03-07 1.0
# arrays-tests.py

# ~ Изучение типа данных array, сравнение скорости работы и занимаемой памяти с list.

import array, random, sys, time

# 1. создание

a = array.array('i')
l = []

print(f"arrays: типы элементов: {array.typecodes}")

print(f"создание: {l=}, {a=}")

print(f"размер пустого: {sys.getsizeof(a)}, {sys.getsizeof(l)}")

a.append(1)
l.append(1)

print(f"размер единичного: {sys.getsizeof(a)}, {sys.getsizeof(l)}")

adder = 10_000

t1 = time.time()
for i in range(adder):
    a.append(i)
t2 = time.time()

print(f"добавили {adder} элементов к array. заняло {t2-t1} секунд. размер стал {sys.getsizeof(a):_} байт")

t1 = time.time()
for i in range(adder):
    l.append(i)
t2 = time.time()

print(f"добавили {adder} элементов к list. заняло {t2-t1} секунд. размер стал {sys.getsizeof(l):_} байт")

print("сделаем shuffle")

random.shuffle(a)
random.shuffle(l)

print("теперь отсортируем")

t1 = time.time()
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
t2 = time.time()

print(f"это заняло для array {t2-t1} секунд")

t1 = time.time()
for i in range(len(l)-1):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]
t2 = time.time()

print(f"это заняло для list {t2-t1} секунд")


# ~ arrays: типы элементов: bBuwhHiIlLqQfd
# ~ создание: l=[], a=array('i')
# ~ размер пустого: 80, 56
# ~ размер единичного: 96, 88
# ~ добавили 10000 элементов к array. заняло 0.00096893310546875 секунд. размер стал 40_420 байт
# ~ добавили 10000 элементов к list. заняло 0.0005869865417480469 секунд. размер стал 85_176 байт
# ~ сделаем shuffle
# ~ теперь отсортируем
# ~ это заняло для array 13.65906286239624 секунд
# ~ это заняло для list 7.799661874771118 секунд

# ~ arrays: типы элементов: bBuwhHiIlLqQfd
# ~ создание: l=[], a=array('Q')
# ~ размер пустого: 80, 56
# ~ размер единичного: 112, 88
# ~ добавили 10000 элементов к array. заняло 0.0007696151733398438 секунд. размер стал 80_760 байт
# ~ добавили 10000 элементов к list. заняло 0.0005931854248046875 секунд. размер стал 85_176 байт
# ~ сделаем shuffle
# ~ теперь отсортируем
# ~ это заняло для array 13.766939878463745 секунд
# ~ это заняло для list 7.740118503570557 секунд

# ~ https://pythonworld.ru/moduli/modul-array-massivy-v-python.html

