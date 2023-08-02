#!/usr/bin/env python
# bfs1.py 2023-08-02 2023-08-02 1.0
# (C) Mikhail Kolodin, 2023

# Breath First algo, 
# given a connected graph, show the order the graph is parsed.
# Graph is presented as a list of tuples.

from collections import defaultdict
# from pprint import pp

def bfs(g):
    """find a node"""

    m = make_matrix(G)
    # pp(g)
    # pp(m)

    queue = [0]
    visited = []

    while queue:
        cur = queue.pop(0)
        visited.append(cur)
        for sosed in m[cur]:
            if sosed not in visited:
                queue.append(sosed)

    return visited


def make_matrix(g):
    """ make matrix as dict of lists for all undirected connections"""

    m = defaultdict(list)

    for a, b in g:
        m[a].append(b)
        m[b].append(a)

    return m
    

G = [
    (0, 3), (0, 9), (0, 5),
    (5, 4), (5, 2),
    (2, 10),
    (4, 8), (4, 1),
    (1, 6), (1, 7), 
    (4, 8)
]

print("path:", bfs(G))

# path: [0, 3, 9, 5, 4, 2, 8, 1, 8, 10, 6, 7]
