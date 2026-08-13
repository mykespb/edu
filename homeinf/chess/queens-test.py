#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# queens-test.py
# 2025-02-14 2025-03-11 1.4

# ~ Дан список расположения ферзей на доске, повертикально, с 0 по 7 - их горизонтали (тоже 0..7).
# ~ Проверить, хорошее ли их расположение (т.е. верно ли, что ни один не бьёт другого).
# ~ Не расстановка! Только проверка!
# ~ https://en.wikipedia.org/wiki/Eight_queens_puzzle

from random import shuffle, random


def generate() -> list[int]:
    """сделать случайное расположение"""

    if random() < .5:
        # заведомо хорошая - для проверки
        boa = [4, 2, 0, 6, 1, 7, 5, 3]
    else:
        # возможно, и плохая - надо проверить
        boa = [0, 1, 2, 3, 4, 5, 6, 7]
        shuffle(boa)
    # ~ print("gen:", boa)
    return boa


def test(boa: list[int]) -> bool:
    """проверить позицию"""

    for right in range(1, 8):
        br = boa[right]
        for left in range(right):
            bl = boa[left]
            if bl == br or abs(br - bl) == (right - left):
                return False

    return True


def print_board(boa: list[int]) -> None:
    """печать доски"""

    for hor in range(7, -1, -1):
        print(hor+1, end=" : ")
        for ver in range(8):
            if boa[ver] == hor:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print()
    print("    ", end="")
    for i in range(8):
        print("ABCDEFGH"[i], end=' ')
    print()


def main(rept: int = 1) -> None:
    """запустить тесты rept раз"""

    for i in range(1, rept+1):
        print(f"----------------------------------\nтест номер {i}\n")
        boa = generate()
        print_board(boa)
        good = test(boa)
        print("\nрасстановка", ["плохая", "хорошая"][good], "\n")

main()


# ~ ----------------------------------
# ~ тест номер 1

# ~ 8 :       *         
# ~ 7 :             *   
# ~ 6 :               * 
# ~ 5 : *               
# ~ 4 :           *     
# ~ 3 :         *       
# ~ 2 :   *             
# ~ 1 :     *           
    # ~ A B C D E F G H 

# ~ расстановка плохая 

# ~ ----------------------------------
# ~ тест номер 1

# ~ 8 :           *     
# ~ 7 :       *         
# ~ 6 :             *   
# ~ 5 : *               
# ~ 4 :               * 
# ~ 3 :   *             
# ~ 2 :         *       
# ~ 1 :     *           
    # ~ A B C D E F G H 

# ~ расстановка хорошая 

