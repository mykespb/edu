#!/usr/bin/env python
# Mikhhail (myke) Kolodin, 2023
# 2023-02-01 2023-02-01 1.0
# problem from LeetCode (see below)

test_data = [
    ["ABCABC", "ABC"],
    ["ABABAB", "ABAB"],
    ["ABCD", "E"],
    ["", "EFGH"]
]


def one_test(test: list[str]) -> str:
    """run one test"""

    s1, s2 = test

    l1, l2 = len(s1), len(s2)

    if l1 == 0 or l2 == 0:
        return ""

    for curlen in range(min(l1, l2), 0, -1):
        if good(s1, s2, curlen):
            return s1[:curlen]

    return ""


def good(s1: str, s2: str, curlen: int) -> bool:
    """check one length, starting from min of given strings"""

    l1, l2 = len(s1), len(s2)
    if l1 % curlen or l2 % curlen:
        return False

    times1, times2 = l1 // curlen, l2 // curlen

    common = s1[:curlen]

    result = s1 == common * times1 and s2 == common * times2

    return result


def run_tests():
    """run all tests"""
    
    print("Start tests")
    
    for test in test_data:
        print(f"{test=} => {one_test(test) or '(none)'}")

    print("Finish tests")

run_tests()


# Наибольший общий делитель строки 

# (https://leetcode.com/problems/greatest-common-divisor-of-strings/)Сложность: Лёгкая 

# Условие задачи: для двух строк s и t мы говорим "t делит s" тогда и только тогда, когда s = t + ... + t (т.е. t объединяется с самим собой один или несколько раз).

# Дается две строки str1 и str2, верните самую большую строку x, такую, что x делит как str1, так и str2.

# Пример:

# Ввод: str1 = "ABCABC", str2 = "ABC"
# Вывод: "ABC"

# Ввод: str1 = "ABABAB", str2 = "ABAB"
# Вывод: "AB"

# Start tests
# test=['ABCABC', 'ABC'] => ABC
# test=['ABABAB', 'ABAB'] => AB
# test=['ABCD', 'E'] => (none)
# test=['', 'EFGH'] => (none)
# Finish tests
