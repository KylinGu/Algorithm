from . import AbstractSort


class SelectionSort(AbstractSort.AbstractSort):

    """
    选择排序，N^2，外循环负责向前，内循环负责查找当前最小元素，然后交换到当前外循环的位置。
    """

    def __init__(self):
        super(AbstractSort.AbstractSort, self).__init__()

    def sort(self, a, visual=False):
        self.array = a

        length = len(self.array)
        for i in range(length):
            min = i
            for j in range(i+1, length):
                if not self.less(self.array[min], self.array[j]):
                    min = j
            self.exch(i, min)

            # visualize sort procedure
            if visual:
                self.visualize()

