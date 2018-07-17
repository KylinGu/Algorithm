from . import Node


class LinkedList:

    head = None
    current = None

    def __init__(self):

        pass

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.head is None:
            raise StopIteration()

        if self.current is None:
            raise StopIteration()

        if isinstance(self.current, Node.Node):
            ret = self.current
            self.current = self.current.next
            return ret
        else:
            raise StopIteration()
