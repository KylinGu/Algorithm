from . import AbstractSymbolTable
from . import SequentialSearchST


class SeparateChainingHashST(AbstractSymbolTable.AbstractSymbolTable):

    def __init__(self, capacity=15, per_element=4):
        """
        :param capacity:
        :param per_element: 拉链碰撞冲突解决法，其中每个bucket中可最多放入的元素，默认是4个。
        """
        self.capacity = capacity
        self.array = [None] * capacity
        self.per_element = per_element

    def put(self, key, val):
        """
        当N/M=2，即平均每个bucket上放入两个node，那么超过两个时候就需要resize。
        :param key:
        :param val:
        :return:
        """
        # if self.capacity*self.per_element < self.size():
        #     self.resize()

        index = self.hash(key)
        # print('key:', key, 'hash:', index)
        if self.array[index] is not None:
            self.array[index].put(key, val)
        else:
            self.array[index] = SequentialSearchST.SequentialSearchST()
            self.array[index].put(key, val)

    def get(self, key):
        if self.is_empty():
            return None

        index = self.hash(key)
        if self.array[index] is not None:
            return self.array[index].get(key)
        else:
            return None

    def size(self):
        msize = 0
        for bucket in self.array:
            if bucket is not None:
                msize += bucket.size()

        return msize

    def keys(self):
        mkeys = []
        for bucket in self.array:
            if bucket is not None:
                mkeys += bucket.keys()

        return mkeys

    def hash(self, key):
        # if isinstance(key, int):
        #     return key % self.capacity
        # elif isinstance(key, float):
        #     pass
        # elif isinstance(key, str):
        #     hash = 0
        #     for char in key:
        #         hash = (hash * 31 + ord(char)) % self.capacity
        #     return hash
        # else:
        return key.__hash__() & 0x7fffffff % self.capacity

    def resize(self, ratio=1.5):
        """
        resize的做法就是copy当前的key val，然后重新put到新的ST中。
        :return:
        """

        mkeys = self.keys()

        mvals = []
        for key in mkeys:
            mvals.append(self.get(key))

        self.capacity = int(self.capacity*ratio)
        self.array = [None] * self.capacity

        for key, val in zip(mkeys, mvals):
            self.put(key, val)


