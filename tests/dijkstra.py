#!/usr/bin/env python
# dijkstra.py 2023-08-02 2023-08-02 1.0
# (C) Mikhail Kolodin, 2023

# 1. Make Dijstra shortest path finding algorithm.
# 2. Test it for given graph.

G = (
    ('a', 'b', 2),
    ('b', 'd', 5),
    ('a', 'd', 8),
    ('b', 'e', 6),
    ('d', 'e', 3),
    ('e', 'f', 1),
    ('d', 'f', 2),
    ('e', 'c', 9),
    ('c', 'f', 3)
)

def findpath(D, fromnode, tonode):
    """find best path using result of Dijkstra marking of graph"""
    
    # print(f"shortest path from {fromnode} to {tonode} is {taba[tonode][0]}")
    way = [tonode]
    next = D[tonode][1]
    while next:
        way = [next] + way
        next = D[next][1]
    return D[tonode][0], way


def dodijkstra(g, fromnode):
    """make Dijkstra marking of given graph"""
    
    visited = []
    unvisited = list('abcdef')
    # print(f"{visited=}, {unvisited=}")
    INFTY = 999999

    taba = {node: [INFTY, ''] for node in unvisited}
    taba[fromnode] = [0, '']

    # print(G)
    # print(taba)

    while unvisited:

        # print(f"\nwhile:: {visited=}, {unvisited=}")

        # find node with smallest shortest dictance
        minpath = INFTY
        for k, v in taba.items():
            if k not in visited and v[0] < minpath:
                minpath = v[0]
                curnode = k
        # print(f"iterate with {curnode=}, {minpath=}")

        # next step: get next unvisited node
        for node in unvisited:
            if node == curnode or node in visited:
                continue

            # check if there is link between curnode and node
            for link in g:
                if link[0] == curnode and link[1] == node:
                    dist = link[2]
                    break
                if link[1] == curnode and link[0] == node:
                    dist = link[2]
                    break
            else:
                continue

            # node is good
            if taba[node][0] > dist + taba[curnode][0]:
                taba[node] = [dist + taba[curnode][0], curnode]
                # print(f"update dist {curnode=} -> {node=} as {dist=} \ngiving {taba=}")

        # print(f"shift {curnode=} leads to {visited=} and {unvisited=}")
        visited.append(curnode)
        unvisited.remove(curnode)

    return taba

D = dodijkstra(G, 'a')
print(D)

P = findpath(D, 'a', 'c')
print(P)

# {'a': [0, ''], 'b': [2, 'a'], 'c': [12, 'f'], 'd': [7, 'b'], 'e': [8, 'b'], 'f': [9, 'd']}
# (12, ['a', 'b', 'd', 'f', 'c'])

# https://www.youtube.com/watch?v=bZkzH5x0SKU
# Dijkstras Shortest Path Algorithm Explained | With Example | Graph Theory
# FelixTechTips

# Note: prints are commented out but left here intentinally for educational purposes.
