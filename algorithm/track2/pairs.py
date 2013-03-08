#!/usr/bin/env python

class Node:
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self, data):
        """
        Node constructor

        @param data node data object
        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Insert new node with data

        @param data node object to insert
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def lookup(self, data, parent=None):
        """
        Lookup node containing data
 
        @param data node data object to look up
        @param parent node's parent
        @returns node and node's parent if found or None, None
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent


def pairs(ar, k):
    count = 0
    root = Node(ar[0])
    for num in ar[1:]:
        root.insert(num)
    for num in ar:
        if root.lookup(num+k) != (None, None):
            count += 1
        if root.lookup(num-k) != (None, None):
            count += 1
    print count/2


(n, k) = (int(i) for i in raw_input().strip().split())
ar = [int(i) for i in raw_input().strip().split()]
pairs(ar, k)
