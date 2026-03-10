#!/usr/bin/env python

# 
# Простые примеры декораторов для школьников.
# Измеряем время работы функции.

from time import sleep, time

def decorate(fun):
    def wrapper(value):
        print("wrapper start")
        start = time()        
        fun(value)
        end = time()
        spent = end - start
        print(f"wrapper end with {spent} secs spent")
    return wrapper

@decorate
def test(value):
    print(f"test start: {value=}")
    sleep(value)
    print("test end")

def main():
    print("Hello from decors!")
    test(1)

if __name__ == "__main__":
    main()
