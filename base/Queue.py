from . import Node

class Queue:

    first = None
    last = None
    N = 0

    def enqueue(self, item):
        node = Node.Node(item)
        node.next = None
        if self.first is None:
            self.first = node
            self.last = self.first
        else:
            self.last.next = node
            self.last = node

        self.N += 1

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            old_first = self.first
            self.first = self.first.next
            self.N -= 1

        return old_first

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