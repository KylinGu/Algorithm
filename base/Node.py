"""
This is a node for link list.
"""


class Node:

    item = None
    next = None

    def __init__(self, item=None):
        self.item = item

    def to_string(self):
        print("item:", self.item)
