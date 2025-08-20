#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2025-08-20 2025-08-20 1.0
# long-go-up.py

# ~ Длинный подъём
# ~ -----------------------------------------

# ~ Найти самую длинную строго возрастающую последовательность натуральных чисел в списке.
# ~ Указать длину и составляющие числа.
# ~ (Если их несколько, то любую).


import random

lst = [ random.randint(1, 1_000_000) for _ in range(10) ]
print("data:", lst)


def main():

    if not lst:
        print("no data, alas. quitting...")
        return

    max_start = this_start = 0
    max_len = this_len = 1

    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            this_len += 1
            if this_len > max_len:
                max_len = this_len
                max_start = this_start
        else:
            this_start = i
            this_len = 1

    print(f"longest upgoing sequence starts at {max_start} and is {max_len} numbers long.")
    print(lst[max_start : max_start+max_len])


main()


# ~ data: [105435, 269314, 435433, 584106, 816159, 359664, 42518, 214695, 342607, 296003]
# ~ longest upgoing sequence starts at 0 and is 5 numbers long.
# ~ [105435, 269314, 435433, 584106, 816159]
