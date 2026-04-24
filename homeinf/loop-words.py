#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2026
# 2026-04-24 2026-04-24 1.0
# loop-words.py

# ~ Есть набор слов.
# ~ Нужно расположить их в таком порядке, чтобы первая буква каждого слова
# ~ совпадала с последней буквой предыдущего слова,
# ~ и так по кругу,
# ~ либо сказать, что такое невозможно.
# ~ Все буквы строчные.

words1 = "oscar bravo romb"
words2 = "omar lego roll"
words3 = "papa alert ant tomb tip belt tina"
words4 = "mama papa dotta sonnie"

words = words1, words2, words3, words4

# ~ debug = True
# ~ debug = False


from itertools import permutations


def solve(task):

    for perm in permutations(task, len(task)):
        if check(perm):
            return perm

    return False
    

def check(perm):

    # ~ if debug: print(perm)
    for i in range(len(perm)):
        if perm[i][-1] != perm[ (i+1) % len(perm) ][0]:
            return False
    return True


def main():
    
    for task in words:
        print(f"\n-----------------------------\ntask:\n{task}")
        
        result = solve(task.split())
        
        if result:
            print("result:")
            print(*result, sep=", ")
        else:
            print("no result.")

    print()
    

main()
