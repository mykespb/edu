#! /usr/bin/env python3
# myke 2019-01-22 1.4

from random import randint as ri

# ----------------------- trees

class Node:
    """ simple 2-links tree structure with utilities
    incl. properties
    with lisp-like print
    """

    def __init__ (self, val=0):
        self.value = val
        self.left = None
        self.right = None

    def __str__ (self):
        return str(f"(Node {self.value})") if self.value != None else ""

    def printall (self):
        print ("(Tree ", end="")
        self._printall ()
        print (")", end="")

    def _printall (self):
        if self.left:
            self.left._printall ()
        print (self, end=" ")
        if self.right:
            self.right._printall ()

    @property
    def max (self):
        res = self.value
        if self.left:
            res = max (res, self.left.max)
        if self.right:
            res = max (res, self.right.max)
        return res

    @property
    def min (self):
        res = self.value
        if self.left:
            res = min (res, self.left.min)
        if self.right:
            res = min (res, self.right.min)
        return res

# tests

def rix():
    """ give random integer in range """
    return ri (-50, 51)

t = Node (rix())
t.left = Node (rix())
t.right = Node (rix())
t.left.right = Node (rix())
t.right.right = Node (rix())
t.right.right.right = Node (rix())
t.right.left = Node ()

print ("tree=", t, ", max=", t.max, ", min=", t.min)
t.printall()

# ----------------------------- // done

# ~ tree= (Node -8) , max= 39 , min= -34
# ~ (Tree (Node 39) (Node 10) (Node -8) (Node 0) (Node -34) (Node -10) (Node 26) )
