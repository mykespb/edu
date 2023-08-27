#!/usr/bin/env python
# logstatistics.py 2023-08-27 2023-08-27 1.0
# (C) Mikhail Kolodin, 2023

# with given log, count stat for each address

log = """
192.168.1.1 - 10:20:30 - 300 - http://www.gogoe.com
193.168.1.1 - 10:20:30 - 200 - http://www.gogoe.com
194.168.1.1 - 10:20:30 - 100 - http://www.gogoe.com
192.167.1.1 - 10:20:30 - 240 - http://www.gogoe.com
192.167.2.1 - 10:20:30 - 300 - http://www.gogoe.com
192.168.1.1 - 10:20:30 - 345 - http://www.gogoe.com
192.168.1.1 - 10:20:30 - 311 - http://www.gogoe.com
192.167.2.1 - 10:20:30 - 312 - http://www.gogoe.com
"""

from collections import defaultdict


def stat(log: list[str]):
    """calculate all and return dict"""

    st = defaultdict(int)

    for line in log.split("\n"):

        line = line.strip()
        if len(line) == 0:
            continue
        
        addr, _, _, _, val, _, _ = line.strip().split()
        st[addr] += int(val)

    return dict(st)


print(stat(log))
        
# {'192.168.1.1': 956, '193.168.1.1': 200, '194.168.1.1': 100, '192.167.1.1': 240, '192.167.2.1': 612}
