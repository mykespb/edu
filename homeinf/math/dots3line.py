#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# dots3line.py
# 2026-07-15 2026-07-17 1.1


tests = [
    [[0., 0.], [1., 1.], [2., 2.]],  # T
    [[1., 1.], [2., 2.], [3., 3.]],  # T
    [[0., 0.], [2., 2.], [1., 1.]],  # T
    [[5., 5.], [1., 1.], [2., 2.]],  # T
    [[5., 6.], [1., 1.], [2., 2.]],  # F
    [[6., 2.], [1., 1.], [2., 2.]],  # F
]


EPS = 1e-6

def near(f1, f2=0.):
    """floats near"""

    return abs(f1 - f2) <= EPS
    

def inline(test):
    """run 1 test"""

    test.sort()

    if near(test[0][0], test[1][0]) and near(test[1][0], test[2][0]):
        return True
    if near(test[0][1], test[1][1]) and near(test[1][1], test[2][1]):
        return True

    if near(test[1][0] - test[0][0], 0.) and not near(test[1][1] - test[0][1], 0):
        return False
    if near(test[2][0] - test[1][0], 0.) and not near(test[2][1] - test[1][1], 0):
        return False

    k01 = (test[1][1] - test[0][1]) / (test[1][0] - test[0][0])
    k12 = (test[2][1] - test[1][1]) / (test[2][0] - test[1][0])

    return near(k01, k12)


def main():
    """run all tests"""

    for num, test in enumerate(tests, start=1):
        print(f"test #{num:2}: {test} -> {inline(test)}")


main()


# ~ test # 1: [[0.0, 0.0], [1.0, 1.0], [2.0, 2.0]] -> True
# ~ test # 2: [[1.0, 1.0], [2.0, 2.0], [3.0, 3.0]] -> True
# ~ test # 3: [[0.0, 0.0], [2.0, 2.0], [1.0, 1.0]] -> True
# ~ test # 4: [[5.0, 5.0], [1.0, 1.0], [2.0, 2.0]] -> True
# ~ test # 5: [[5.0, 6.0], [1.0, 1.0], [2.0, 2.0]] -> False
# ~ test # 6: [[6.0, 2.0], [1.0, 1.0], [2.0, 2.0]] -> False
