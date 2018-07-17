'''
This is a LIFO stack based on link list.
'''

from . import Node


class Stack:

    first = None
    N = 0
    current = None

    def pop(self):
        if self.is_empty():
            return None

        item = self.first.item
        self.first = self.first.next
        self.N -= 1
        return item

    def push(self, item):
        old_first = self.first
        node = Node.Node()
        node.item = item
        node.next = old_first
        self.first = node
        self.N += 1

    def is_empty(self):
        return True if self.N == 0 else False

    def size(self):
        return self.N

    def __iter__(self):
        self.current = self.first
        return self

    def __next__(self):
        if self.first is None:
            raise StopIteration()

        if self.current is None:
            raise StopIteration()

        if isinstance(self.current, Node.Node):
            ret = self.current
            self.current = self.current.next
            return ret
        else:
            raise StopIteration()