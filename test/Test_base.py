'''
This is a test class.
'''

from base import Node
from base import LinkedList
# from collections import Iterable
from base import Stack
from base import Queue
from base import Bag


def gen_arrays():
    return ['I', 'Am', 'Kylin', 123, '+', 456]

def link_list():

    llinklist = LinkedList.LinkedList()

    first = Node.Node('I ')
    second = Node.Node('AM ')
    third = Node.Node('KYLIN ')
    four = Node.Node(123)

    llinklist.head = first
    first.next = second
    second.next = third
    third.next = four

    # print(first.item, first.next.item, first.next.next.item)

    for node in llinklist:
        print(node.item)


def test_stack(array):
    stack = Stack.Stack()
    for item in array:
        stack.push(item)

    print('pop out one element from stack ', stack.pop())

    for node in stack:
        print(node.item)


def test_queque(array):
    queue = Queue.Queue()
    for item in array:
        queue.enqueue(item)

    print('dequeue 1: ', queue.dequeue().item)
    print('dequeue 2: ', queue.dequeue().item)

    for item in queue:
        print(item.item)


def test_bag(array):
    bag = Bag.Bag()
    for item in array:
        bag.add(item)

    for item in bag:
        print(item.item)


if __name__ == '__main__':
    arrays = gen_arrays()
    # link_list()

    # stack
    # test_stack(arrays)

    # queue
    # test_queque(arrays)

    # bag
    test_bag(arrays)
