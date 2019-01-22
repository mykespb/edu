#! /usr/bin/env python3
# myke 2019-01-22 1.0

# ~ http://company.yandex.ru/job/vacancies/python_pit.xml
# ~ Продемонстрируйте свои знания
# ~ Вопрос 1
# ~ Есть два списка разной длины. В первом содержатся ключи, а во втором значения. Напишите функцию, которая создаёт из этих ключей и значений словарь. Если ключу не хватило значения, в словаре должно быть значение None. Значения, которым не хватило ключей, нужно игнорировать.

tests = {
1:
    {"first": "one two three four".split(),
    "second": [1, 2, 3, 4]
    },
2:
    {"first": "basic fortran c lisp cobol".split(),
    "second": [1, 2, 3]
    },
3:
    {"first": "see you again".split(),
    "second": [1, 2, 3, 4, 5]
    }
}

def tester():
    """ function takes data and tests all of them"""

    for num, test in tests.items():
        print ("\ntest", num, test["first"], "->", test["second"], "\nmakes", one_test (test))

def one_test (test):
    """ test one pair"""

    d = {}
    k = test["first"][:]
    v = test["second"][:]
    while k:
        d [k.pop(0)] = v.pop(0) if len(v) else None
    return d

tester()

# -------------------------------

# ~ test 1 ['one', 'two', 'three', 'four'] -> [1, 2, 3, 4]
# ~ makes {'one': 1, 'two': 2, 'three': 3, 'four': 4}

# ~ test 2 ['basic', 'fortran', 'c', 'lisp', 'cobol'] -> [1, 2, 3]
# ~ makes {'basic': 1, 'fortran': 2, 'c': 3, 'lisp': None, 'cobol': None}

# ~ test 3 ['see', 'you', 'again'] -> [1, 2, 3, 4, 5]
# ~ makes {'see': 1, 'you': 2, 'again': 3}
