from . import AbstractSymbolTable


class SequentialSearchST(AbstractSymbolTable.AbstractSymbolTable):

    first = None
    N = 0

    def put(self, key, val):
        current = self.first
        while current is not None:
            if current.key == key:
                current.val = val
                return
            current = current.next

        self.first = Node(key, val, self.first)
        self.N += 1

    def get(self, key):
        if self.is_empty():
            return None

        current = self.first
        while current is not None:
            if key == current.key:
                return current.val
            current = current.next

    def size(self):
        return self.N

    def keys(self):
        if self.is_empty():
            return None

        current = self.first
        keys = []
        while current is not None:
            keys.append(current.key)
            current = current.next

        return keys


class Node:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next