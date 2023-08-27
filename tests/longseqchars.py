#!/usr/bin/env python
# longseqchars.py 2023-08-27 2023-08-27 1.0
# (C) Mikhail Kolodin, 2023

# String is given.
# Find longest substring without repeating characters.

stroka = "aaaabbbbbvvvvvxxxzzzrgdsbbbbbbddddvccc"

def findsub(s: str) -> str:
    """find best substring"""

    if not s:
        return ""
    
    cur = ""
    best = ""
    lenbest = 0

    for c in s:
        if c in cur:
            if len(cur) > lenbest:
                lenbest = len(cur)
                best = cur
                cur = c
        else:
            cur += c

    if len(cur) > lenbest:
        lenbest = len(cur)
        best = cur

    return best


print(stroka, findsub(stroka))
