#!/usr/bin/env python
# Mikhail Kolodin, 2023
# 2023-02-08 2023-02-08 1.3
# ya-join-arrays.py

# ~ Задача из яндекса
# ~ Задача F. Слияние $k$ сортированных списков

from random import randint
from collections import Counter

K = 3

# ~ 1. Делаем случайный набор массивов (всего их K)

def make(num = K):
    """сделать набор массивов"""
    ars = []
    for i in range(K):
        ar = [randint(0, 100) for _ in range(randint(1, 10))]
        ar.sort()
        ars += [ar]

    print("Исходные массивы", *ars, sep='\n')
    return ars


# ~ 2. Решаем задачу

def proc1(ars):
    """1 способ, тупой"""
    print("Результат:")
    best = []
    for ar in ars:
        best.extend(ar)
    # ~ print(best)
    best.sort()
    # ~ print(best)


def proc2(ars):
    """2 способ, умный... слишком..."""
    print("Результат:")
    best = []
    loarr = len(ars)                           # всего массивов
    ptrs = {i: 0 for i in range(loarr)}      # указатели на текущие элементы массивов
    print(f"{ptrs=}")

    while ptrs:

        els = [ [k, ars[k][v]] for k, v in ptrs.items()]
        print(f"{els=}")
        els.sort(key = lambda e: e[1])
        print(f"{els=}")

        lop = els[0]  # обрабатываем этот список
        best.append(lop[1]) # добавили элемент к результату
        print(f"{best=}")
        # продвигаем указатель
        # его новое значение для списка № lop[0]
        prol = lop[0]
        newp = ptrs[prol] + 1
        if newp >= len(ars[prol]):
            del ptrs[prol]
        else:
            ptrs[prol] = newp
        print(f"{ptrs=}")

    return best


def proc3(ars):
    """3 способ, хитрый"""

    cnt = Counter(ars[0])
    
    for arr in ars[1:]:
        cnt.update(arr)
    print(cnt)

    car = sorted(cnt.elements())

    # ~ print(car)
    return car


def proc4(ars):
    """4 способ, хитрый"""

    cnt = [0 for i in range(0, 101)]
    
    for arr in ars:
        for e in arr:
            cnt[e] += 1
    # ~ print(cnt)

    car = []
    for i in range(0, 101):
        for c in range(cnt[i]):
            car.append(i)

    # ~ print(car)
    return car

# ~ 3. Тестируем решалку

ars = make()
best = proc4(ars)

print(f"""
-----------------------------------------------------------------------
Решение:
{best}
-----------------------------------------------------------------------
""")


# ~ Даны $k$ отсортированных в порядке неубывания массивов неотрицательных целых чисел, каждое из которых не превосходит 100. Требуется построить результат их слияния: отсортированный в порядке неубывания массив, содержащий все элементы исходных $k$ массивов. Длина каждого массива не превосходит $10\cdot k$.
# ~ Для каждого массива создадим по указателю; изначально каждый указатель расположен в начале соответствующего массива. Элементы, соответствующие позициям указателей, поместим в любую структуру данных, которая поддерживает извлечение минимума — это может быть мультимножество или, например, куча. Далее будем извлекать из этой структуры минимальный элемент, помещать его в ответ, сдвигать позицию указателя в соответствующем массиве и помещать в структуру данных очередной элемент из этого массива.

# ~ Исходные массивы
# ~ [40, 42, 66, 96]
# ~ [67]
# ~ Результат:
# ~ ptrs={0: 0, 1: 0}
# ~ els=[[0, 40], [1, 67]]
# ~ els=[[0, 40], [1, 67]]
# ~ best=[40]
# ~ ptrs={0: 1, 1: 0}
# ~ els=[[0, 42], [1, 67]]
# ~ els=[[0, 42], [1, 67]]
# ~ best=[40, 42]
# ~ ptrs={0: 2, 1: 0}
# ~ els=[[0, 66], [1, 67]]
# ~ els=[[0, 66], [1, 67]]
# ~ best=[40, 42, 66]
# ~ ptrs={0: 3, 1: 0}
# ~ els=[[0, 96], [1, 67]]
# ~ els=[[1, 67], [0, 96]]
# ~ best=[40, 42, 66, 67]
# ~ ptrs={0: 3}
# ~ els=[[0, 96]]
# ~ els=[[0, 96]]
# ~ best=[40, 42, 66, 67, 96]
# ~ ptrs={}

# ~ -----------------------------------------------------------------------
# ~ Решение:
# ~ [40, 42, 66, 67, 96]
# ~ -----------------------------------------------------------------------

# ~ Исходные массивы
# ~ [10, 16, 50, 53, 58, 88]
# ~ [0, 10, 28, 30, 42, 58, 59, 77]
# ~ [1, 15, 18, 22, 33, 44, 46, 50, 62, 67]
# ~ Результат:
# ~ ptrs={0: 0, 1: 0, 2: 0}
# ~ els=[[0, 10], [1, 0], [2, 1]]
# ~ els=[[1, 0], [2, 1], [0, 10]]
# ~ best=[0]
# ~ ptrs={0: 0, 1: 1, 2: 0}
# ~ els=[[0, 10], [1, 10], [2, 1]]
# ~ els=[[2, 1], [0, 10], [1, 10]]
# ~ best=[0, 1]
# ~ ptrs={0: 0, 1: 1, 2: 1}
# ~ els=[[0, 10], [1, 10], [2, 15]]
# ~ els=[[0, 10], [1, 10], [2, 15]]
# ~ best=[0, 1, 10]
# ~ ptrs={0: 1, 1: 1, 2: 1}
# ~ els=[[0, 16], [1, 10], [2, 15]]
# ~ els=[[1, 10], [2, 15], [0, 16]]
# ~ best=[0, 1, 10, 10]
# ~ ptrs={0: 1, 1: 2, 2: 1}
# ~ els=[[0, 16], [1, 28], [2, 15]]
# ~ els=[[2, 15], [0, 16], [1, 28]]
# ~ best=[0, 1, 10, 10, 15]
# ~ ptrs={0: 1, 1: 2, 2: 2}
# ~ els=[[0, 16], [1, 28], [2, 18]]
# ~ els=[[0, 16], [2, 18], [1, 28]]
# ~ best=[0, 1, 10, 10, 15, 16]
# ~ ptrs={0: 2, 1: 2, 2: 2}
# ~ els=[[0, 50], [1, 28], [2, 18]]
# ~ els=[[2, 18], [1, 28], [0, 50]]
# ~ best=[0, 1, 10, 10, 15, 16, 18]
# ~ ptrs={0: 2, 1: 2, 2: 3}
# ~ els=[[0, 50], [1, 28], [2, 22]]
# ~ els=[[2, 22], [1, 28], [0, 50]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22]
# ~ ptrs={0: 2, 1: 2, 2: 4}
# ~ els=[[0, 50], [1, 28], [2, 33]]
# ~ els=[[1, 28], [2, 33], [0, 50]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28]
# ~ ptrs={0: 2, 1: 3, 2: 4}
# ~ els=[[0, 50], [1, 30], [2, 33]]
# ~ els=[[1, 30], [2, 33], [0, 50]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28, 30]
# ~ ptrs={0: 2, 1: 4, 2: 4}
# ~ els=[[0, 50], [1, 42], [2, 33]]
# ~ els=[[2, 33], [1, 42], [0, 50]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28, 30, 33]
# ~ ptrs={0: 2, 1: 4, 2: 5}
# ~ els=[[0, 50], [1, 42], [2, 44]]
# ~ els=[[1, 42], [2, 44], [0, 50]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28, 30, 33, 42]
# ~ ptrs={0: 2, 1: 5, 2: 5}
# ~ els=[[0, 50], [1, 58], [2, 44]]
# ~ els=[[2, 44], [0, 50], [1, 58]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28, 30, 33, 42, 44]
# ~ ptrs={0: 2, 1: 5, 2: 6}
# ~ els=[[0, 50], [1, 58], [2, 46]]
# ~ els=[[2, 46], [0, 50], [1, 58]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28, 30, 33, 42, 44, 46]
# ~ ptrs={0: 2, 1: 5, 2: 7}
# ~ els=[[0, 50], [1, 58], [2, 50]]
# ~ els=[[0, 50], [2, 50], [1, 58]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28, 30, 33, 42, 44, 46, 50]
# ~ ptrs={0: 3, 1: 5, 2: 7}
# ~ els=[[0, 53], [1, 58], [2, 50]]
# ~ els=[[2, 50], [0, 53], [1, 58]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28, 30, 33, 42, 44, 46, 50, 50]
# ~ ptrs={0: 3, 1: 5, 2: 8}
# ~ els=[[0, 53], [1, 58], [2, 62]]
# ~ els=[[0, 53], [1, 58], [2, 62]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28, 30, 33, 42, 44, 46, 50, 50, 53]
# ~ ptrs={0: 4, 1: 5, 2: 8}
# ~ els=[[0, 58], [1, 58], [2, 62]]
# ~ els=[[0, 58], [1, 58], [2, 62]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28, 30, 33, 42, 44, 46, 50, 50, 53, 58]
# ~ ptrs={0: 5, 1: 5, 2: 8}
# ~ els=[[0, 88], [1, 58], [2, 62]]
# ~ els=[[1, 58], [2, 62], [0, 88]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28, 30, 33, 42, 44, 46, 50, 50, 53, 58, 58]
# ~ ptrs={0: 5, 1: 6, 2: 8}
# ~ els=[[0, 88], [1, 59], [2, 62]]
# ~ els=[[1, 59], [2, 62], [0, 88]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28, 30, 33, 42, 44, 46, 50, 50, 53, 58, 58, 59]
# ~ ptrs={0: 5, 1: 7, 2: 8}
# ~ els=[[0, 88], [1, 77], [2, 62]]
# ~ els=[[2, 62], [1, 77], [0, 88]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28, 30, 33, 42, 44, 46, 50, 50, 53, 58, 58, 59, 62]
# ~ ptrs={0: 5, 1: 7, 2: 9}
# ~ els=[[0, 88], [1, 77], [2, 67]]
# ~ els=[[2, 67], [1, 77], [0, 88]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28, 30, 33, 42, 44, 46, 50, 50, 53, 58, 58, 59, 62, 67]
# ~ ptrs={0: 5, 1: 7}
# ~ els=[[0, 88], [1, 77]]
# ~ els=[[1, 77], [0, 88]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28, 30, 33, 42, 44, 46, 50, 50, 53, 58, 58, 59, 62, 67, 77]
# ~ ptrs={0: 5}
# ~ els=[[0, 88]]
# ~ els=[[0, 88]]
# ~ best=[0, 1, 10, 10, 15, 16, 18, 22, 28, 30, 33, 42, 44, 46, 50, 50, 53, 58, 58, 59, 62, 67, 77, 88]
# ~ ptrs={}

# ~ -----------------------------------------------------------------------
# ~ Решение:
# ~ [0, 1, 10, 10, 15, 16, 18, 22, 28, 30, 33, 42, 44, 46, 50, 50, 53, 58, 58, 59, 62, 67, 77, 88]
# ~ -----------------------------------------------------------------------
