#! /usr/bin/env python
# myke 2019-01-22 2026-03-25 1.2

from pprint import pprint

# ------------------------ internal class vars

class C:
    a = 3
    _b = 4
    __d = 5

q = C()

pprint ((q.a, q._b, q._C__d, dir(q), C.__dict__))


# ---------------------------------- done.

# 3 4 5
# ['_C__d', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_b', 'a']
# {'__module__': '__main__', 'a': 3, '_b': 4, '_C__d': 5, '__dict__': <attribute '__dict__' of 'C' objects>, '__weakref__': <attribute '__weakref__' of 'C' objects>, '__doc__': None}


# ~ (3,
 # ~ 4,
 # ~ 5,
 # ~ ['_C__d',
  # ~ '__class__',
  # ~ '__delattr__',
  # ~ '__dict__',
  # ~ '__dir__',
  # ~ '__doc__',
  # ~ '__eq__',
  # ~ '__firstlineno__',
  # ~ '__format__',
  # ~ '__ge__',
  # ~ '__getattribute__',
  # ~ '__getstate__',
  # ~ '__gt__',
  # ~ '__hash__',
  # ~ '__init__',
  # ~ '__init_subclass__',
  # ~ '__le__',
  # ~ '__lt__',
  # ~ '__module__',
  # ~ '__ne__',
  # ~ '__new__',
  # ~ '__reduce__',
  # ~ '__reduce_ex__',
  # ~ '__repr__',
  # ~ '__setattr__',
  # ~ '__sizeof__',
  # ~ '__static_attributes__',
  # ~ '__str__',
  # ~ '__subclasshook__',
  # ~ '__weakref__',
  # ~ '_b',
  # ~ 'a'],
 # ~ mappingproxy({'_C__d': 5,
               # ~ '__dict__': <attribute '__dict__' of 'C' objects>,
               # ~ '__doc__': None,
               # ~ '__firstlineno__': 8,
               # ~ '__module__': '__main__',
               # ~ '__static_attributes__': (),
               # ~ '__weakref__': <attribute '__weakref__' of 'C' objects>,
               # ~ '_b': 4,
               # ~ 'a': 3}))
