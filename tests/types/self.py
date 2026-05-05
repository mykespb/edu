#!/usr/bin/env python

# Mikhail (myke) Kolodin, 2025
# 2026-05-05 2026-05-05 1.0
# self.py

# ~ проверка аннотации Self

class MyStack[T]:
    def __init__(self, values: Sequence[T] = ()) -> Self:
        self.values: list[T] = list(values)

    def push(self, value: T) -> Self:
        self.values.append(value)
        return self

    def pop(self) -> T:
        return self.values.pop()

    def top(self) -> T:
        return self.values[-1]

    def is_empty(self) -> bool:
        return not self.values

    def __bool__(self) -> bool:
        return not self.is_empty()


def main_int():    

    ms = MyStack[int]()
    ms.push(1)
    print(ms)

    while ms:
        print(ms.pop())

    ms.push(2)
    ms.push(3)
    ms.push(4)

    while ms:
        print(ms.pop())

    ms.push(11).push(12).push(13)

    while ms:
        print(ms.pop())


def main_str():

    ms = MyStack[str]()
    ms.push("apple")
    print(ms)

    while ms:
        print(ms.pop())

    ms.push("fruit").push("orange").push("wine")

    while ms:
        print(ms.pop())


if __name__ == "__main__":
    main_int()
    main_str()
    

# ~ https://www.youtube.com/watch?v=q4QVvmJo79E

# ~ <__main__.MyStack object at 0x7d0a0a888c20>
# ~ 1
# ~ 4
# ~ 3
# ~ 2
# ~ 13
# ~ 12
# ~ 11
# ~ <__main__.MyStack object at 0x7d0a0a8787d0>
# ~ apple
# ~ wine
# ~ orange
# ~ fruit
