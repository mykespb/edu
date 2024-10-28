#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-05-03 2024-10-28 1.1
# maxpair.py

# ~ пользователь вводит строку натуральных чисел.
# ~ программа находит пару, дающую макс. произведение.
# ~ так повторяется, пока пользователь не введёт пустую строку или 0.

def test():
    while (s := input("Введите строку натуральных чисел через пробелы или 0 для окончания: ")):
        if not s: break

        nums = s.strip().split()
        nums = [int(x) for x in nums]
        # ~ nums = list(map(int, nums))

        if not nums or 0 in nums: break
        
        maxprod = maxi = maxj = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j: continue
                if (prod := nums[i] * nums[j]) > maxprod:
                    maxprod, maxi, maxj = prod, i, j

        print("числа:", nums,
            ", наибольшее произведение равно", maxprod,
            "для пары", nums[maxi], nums[maxj])

    print("Конец работы.")

test()

