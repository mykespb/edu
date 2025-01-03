#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2022
# 2022-05-03 2024-11-04 1.3
# maxpair.py

# ~ пользователь вводит строку натуральных чисел.
# ~ программа находит пару, дающую макс. произведение.
# ~ так повторяется, пока пользователь не введёт пустую строку или 0.

def test():
    while (s := input("Введите строку натуральных чисел через пробелы или 0 для окончания: ")):

        nums = s.strip().split()
        nums = [int(x) for x in nums]

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

# ~ Введите строку натуральных чисел через пробелы или 0 для окончания: 3 4 5
# ~ числа: [3, 4, 5] , наибольшее произведение равно 20 для пары 4 5
# ~ Введите строку натуральных чисел через пробелы или 0 для окончания: 4 5 1 1 1 1
# ~ числа: [4, 5, 1, 1, 1, 1] , наибольшее произведение равно 20 для пары 4 5
# ~ Введите строку натуральных чисел через пробелы или 0 для окончания: 
# ~ Конец работы.
