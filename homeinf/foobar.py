#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  foobar.py 1.2
#  Write a program that prints the numbers from 1 to 100.
#  But for multiples of three print “Foo” instead of the number
#  and for the multiples of five print “Bar”.
#  For numbers which are multiples of both three and five print “FooBar”.

def main():
    for n in range(1, 101):
        print(
            "FooBar" if n % 15 == 0 else
            "Foo" if n % 3 == 0 else
            "Bar" if n % 5 == 0 else n
            , ", ",
            sep="",
            end="\n" if n % 10 == 0 else "")

    return 0


if __name__ == '__main__':
    main()

# ~ 1, 2, Foo, 4, Bar, Foo, 7, 8, Foo, Bar,
# ~ 11, Foo, 13, 14, FooBar, 16, 17, Foo, 19, Bar,
# ~ Foo, 22, 23, Foo, Bar, 26, Foo, 28, 29, FooBar,
# ~ 31, 32, Foo, 34, Bar, Foo, 37, 38, Foo, Bar,
# ~ 41, Foo, 43, 44, FooBar, 46, 47, Foo, 49, Bar,
# ~ Foo, 52, 53, Foo, Bar, 56, Foo, 58, 59, FooBar,
# ~ 61, 62, Foo, 64, Bar, Foo, 67, 68, Foo, Bar,
# ~ 71, Foo, 73, 74, FooBar, 76, 77, Foo, 79, Bar,
# ~ Foo, 82, 83, Foo, Bar, 86, Foo, 88, 89, FooBar,
# ~ 91, 92, Foo, 94, Bar, Foo, 97, 98, Foo, Bar,
