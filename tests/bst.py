#!/usr/bin/env python
# Mikhail Kolodin, 2023
# 2023-02-17 2023-02-17 1.2
# bst.py

# my class for BST: binary search trees

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
                return
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
                return

    def search(self, val):
        """check if data is in BST"""
        if val==self.data:
            return True
        elif val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def insertUnique(self, data):
        """insert unique element"""

        if self.search(data):
            return
        self.insert(data)

    # print functions
    def print(self):
        """print element or tree with parens"""
        print('(', end='')
        self.printBST()
        print(')', end=' ')
        
    def printBST(self):
        """print tree with parens"""
        if self.left:
            self.left.print()
        print(self.data, end=', ')
        if self.right:
            self.right.print()

    def printLinear(self):
        """print element or tree without parens"""
        self.printLinearBST()

    def printLinearBST(self):
        """print tree without parens"""
        if self.left:
            self.left.printLinear()
        print(self.data, end=', ')
        if self.right:
            self.right.printLinear()

        

# tests

if __name__ == "__main__":
    root = Node(27)
    root.insert(7)
    root.insert(14)
    root.insert(433)
    root.insert(42)
    root.insert(4)
    root.insertUnique(0)
    root.insertUnique(0)
    root.insertUnique(0)
    root.insertUnique(0)
    print("\nprint without parens:")
    root.printLinear()
    print("\nprint with parens:")
    root.print()
    print()

# ~ print without parens:
# ~ 0, 4, 7, 14, 27, 42, 433, 
# ~ print with parens:
# ~ ((((0, ) 4, ) 7, (14, ) ) 27, ((42, ) 433, ) ) 
