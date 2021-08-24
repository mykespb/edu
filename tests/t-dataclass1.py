#!/usr/bin/env python3.9
# dataclass test 1
# (C) Mikhail Kolodin, 2021
# ver. 2021-08-24 2021-08-24 1.1

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

loh = []

for hi in range(10):
  loh.append(Homo("homo"+str(hi), 10+hi%10))

pp(loh)


# ~ Homo(name='Vasya', age=25, unic='ae34fc1891364b4889572bde82275046')
# ~ [Homo(name='homo0', age=10, unic='a876b1676eac4289b3839fcc7f71a8f7'),
 # ~ Homo(name='homo1', age=11, unic='9ba7a256884a4443b07a5f811b7e8248'),
 # ~ Homo(name='homo2', age=12, unic='4005c9c2c8b74e18aec4703686e7e19f'),
 # ~ Homo(name='homo3', age=13, unic='f720d3ea10d84b5eaa8b8129cb7029d3'),
 # ~ Homo(name='homo4', age=14, unic='ce80f29e1b9e4c289b03976a3b3fc9e8'),
 # ~ Homo(name='homo5', age=15, unic='07e0749584764807a40440ff6d887347'),
 # ~ Homo(name='homo6', age=16, unic='8b3e269bc14541f3855ad5e81e18f16c'),
 # ~ Homo(name='homo7', age=17, unic='d6a8faf1a2ad46bebb9ed7d4fefaeb8b'),
 # ~ Homo(name='homo8', age=18, unic='e9b3c8ac929d4ec89699756eb5bf90c1'),
 # ~ Homo(name='homo9', age=19, unic='d96823e782994b8abd0a0b3010c0c80b')]
