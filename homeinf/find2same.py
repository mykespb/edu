# myke find2same.py
# 2022-08-26 2022-08-29 2.0

# задача про носки.
# есть ящик с чёрными носками разного размера (от 20 до 40),
# найти пару одного размера (всего там 10 штук).

# а. создать список с 2 одинаковыми натур. числами
# б. найти эти 2 числа

from random import randint, shuffle

def make(size = 10, nmin = 20, nmax = 40):
    """сделать список размера size из случайных чисел от nmin до nmax"""

    if size < 2 or nmin < 1 or nmax < nmin:
        return []

    a = [randint(nmin, nmax) for i in range(size)]
    a[0] = a[1]
    shuffle(a)
    return a


def find1(arr):
    """найти одну пару одинаковых чисел в данном списке"""

    size = len(arr)
    for i in range(size-1):
        for j in range(i+1, size):
            if arr[i] == arr[j]:
                return arr[i]
    return None

def find2(arr):
    """найти одну пару одинаковых чисел в данном списке"""

    size = len(arr)
    for i in range(size-1):
        if arr[i] in arr[i+1:]:
            return arr[i]
    return None


find = find2
print(a := make(), "-->", find(a))


# пример вывода:
# [98, 2, 15, 11, 55, 29, 15, 33, 45, 71] --> 15

# если данные для создания списка некорректные, возвращается пустой список.
# если пар нет, возвращается None.
# если пар несколько, возвращается одна любая.
