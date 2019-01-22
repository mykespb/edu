#! /usr/bin/env python3
# myke 2019-01-22 1.3

# ASLists = autosorted lists

from collections.abc import Iterable

class ASList:

    def __init__(self, e=None):
        self.l = []
        if e is not None:
            self.add (e)

    def add (self, e):
        if isinstance (e, Iterable):
            self.l.extend (e)
        else:
            self.l += [e]
        self.l.sort()

    def __str__ (self):
        res = "["
        for e in self.l:
            res += str(e) + ", "
        res += "]"
        return res
        # "," output can be improved

    @property
    def len (self):
        return len (self.l)

# tests

s = ASList((66, -99, 34))
print (s)

s.add (11)
print (s)

s.add (0)
print (s)

s.add (33)
print (s)

s.add (-64)
print (s)

s.add ([21, 3, 5])
print (s)

print ("len=", s.len)

# ----------------- // done.

# ~ [-99, 34, 66, ]
# ~ [-99, 11, 34, 66, ]
# ~ [-99, 0, 11, 34, 66, ]
# ~ [-99, 0, 11, 33, 34, 66, ]
# ~ [-99, -64, 0, 11, 33, 34, 66, ]
# ~ [-99, -64, 0, 3, 5, 11, 21, 33, 34, 66, ]
# ~ len= 10
