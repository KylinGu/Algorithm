from . import AbstractSymbolTable


class BinarySearchST(AbstractSymbolTable.AbstractSymbolTable):
    capacity = 15
    ratio = 0.5
    N = 0

    def __init__(self):
        self.__keys = [None] * self.capacity
        self.__vals = [None] * self.capacity

    def get(self, key):
        if self.is_empty():
            return None

        i = self.rank(key)
        if i < self.size() and self.__keys[i] == key:
            return self.__vals[i]
        else:
            return None

    def put(self, key, val):
        """
        如果我把key用hash进行转换，作为键是否就成hashmap了？
        :param key:
        :param val:
        :return:
        """
        if self.is_full():
            self.resize()

        i = self.rank(key)

        # print('rank', i, key, val)

        # 找到并更新vals
        if i <= self.size() and self.__keys[i] == key:
            self.__vals[i] = val
            return i

        # 未找到，所以需要根据rank进行插入操作。
        for j in range(self.capacity-1, i, -1):
            self.__keys[j] = self.__keys[j-1]
            self.__vals[j] = self.__vals[j-1]

        self.__keys[i] = key
        self.__vals[i] = val
        self.N += 1

        # print('key val', self.__keys[:self.N], self.__vals[:self.N])

    def rank(self, key):

        lo = 0
        hi = self.N - 1

        while lo <= hi:
            mid = lo + (hi - lo)//2
            # print('rank key:', key, ', mid:', self.__keys[mid])
            if key > self.__keys[mid]:
                lo = mid + 1
            elif key < self.__keys[mid]:
                hi = mid - 1
            else:
                return mid
        return lo

    def resize(self):
        self.__keys = self.__keys + [None] * int(self.capacity * self.ratio)
        self.__vals = self.__vals + [None] * int(self.capacity * self.ratio)
        self.capacity = int(self.capacity * (1+self.ratio))

    def size(self):
        return self.N

    def is_full(self):
        return self.capacity == self.size()

    def keys(self):
        return self.__keys[:self.N-1]

    def max(self):
        return self.__keys[self.N-1]

    def min(self):
        return self.__keys[0]

    def select(self, k):
        return self.__keys[k]

