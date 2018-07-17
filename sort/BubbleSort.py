from . import AbstractSort


class BubbleSort(AbstractSort.AbstractSort):

    def __init__(self):
        super(AbstractSort.AbstractSort, self).__init__()

    def sort(self, a):
        self.array = a
        length = len(self.array)

        for i in range(length-1):
            for j in range(0, length-1):
                if not self.less(self.array[j], self.array[j+1]):
                    self.exch(j, j+1)

