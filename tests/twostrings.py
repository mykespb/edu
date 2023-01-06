#!/usr/bin/env python3
# twostrings.py 2023-01-06 1.0 2023-01-06

# ~ https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
# ~ Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# ~ A string is represented by an array if the array elements concatenated in order forms the string.

tests = ((('one', 'two', 'three'), ('o', 'netwot', 'hree')),
    (('a', 'book', 'no'), ('thebook', 'yes')))

def equals(group):
    return "".join(group[0]) == "".join(group[1])

def test(group):
    print(group, '->', equals(group))

for group in tests:
    test(group)

# ~ (('one', 'two', 'three'), ('o', 'netwot', 'hree')) -> True
# ~ (('a', 'book', 'no'), ('thebook', 'yes')) -> False
