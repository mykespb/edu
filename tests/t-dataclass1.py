#!/usr/bin/env python3.9
# dataclass test 1
# (C) Mikhail Kolodin, 2021
# ver. 2021-08-24 2021-08-24 1.0

from dataclasses import dataclass, field
import uuid
from pprint import pprint as pp

@dataclass
class Homo:
  name: str
  age:  float
  unic: str = field(init=False)

  def __post_init__(self):
    self.unic = uuid.uuid4().hex


h1 = Homo("Vasya", 25)

print(h1)

