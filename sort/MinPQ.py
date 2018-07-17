from . import AbstractSort


class MinPriorityQueue(AbstractSort.AbstractSort):

    __SIZE = 15
    __N = 0

    def __init__(self):
        super(AbstractSort.AbstractSort, self).__init__()
        self.array = [None]*self.__SIZE

    def sort(self):
        pass

    def insert(self, item):
        if self.is_full():
            self.array = self.array + [None] * len(self.array)

        self.array[self.__N] = item
        self.__N += 1

        for i in range(1, self.__N):
            temp = i
            for j in range(temp-1, -1, -1):
                if self.less(self.array[temp], self.array[j]):
                    self.exch(temp, j)
                    temp = j
        # self.show()

    def min(self):
        if not self.is_empty():
            return self.array[0]
        else:
            return None

    def del_min(self):
        if self.min() is not None:
            min = self.array.pop(0)
            self.__N -= 1
            return min
        else:
            return None

    def is_empty(self):
        return True if self.__N == 0 else False

    def is_full(self):
        return True if self.__N == len(self.array) else False

    def size(self):
        return self.__N
