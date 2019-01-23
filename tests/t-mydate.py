#! /usr/bin/env python3
# myke 2019-01-23 1.2

# ------------------------- my date class

import datetime

class Mydate:
    def __init__ (self, d=0, m=0, y=0):
        _today = datetime.date.today()
        self.year = y if y else _today.year
        self.month = m if m else _today.month
        self.day = d if d else _today.day

    def __str__(self):
        return f"{self.year:04}-{self.month:02}-{self.day:02}"

    def __repr__(self):
        return f"<Mydate {self.year:04}-{self.month:02}-{self.day:02}>"

cd1 = Mydate()
print (cd1, cd1.__repr__())

cd2 = Mydate(11)
print (cd2, cd2.__repr__())

cd3 = Mydate(20, 3)
print (cd3, cd3.__repr__())

# ---------------------------------- done.

# ~ 2019-01-22 <Mydate 2019-01-22>
# ~ 2019-01-11 <Mydate 2019-01-11>
# ~ 2019-03-20 <Mydate 2019-03-20>
