from . import AbstractSort
from . import InsertionSort
import numpy as np


class QuickSort(AbstractSort.AbstractSort):

    """
    仍然是分而治之的思想，但是它的思想是先进行划分。划分的左边是小于该划分点，右边是大于划分点。
    这样通过不断的划分，划分的同时需要交换元素的位置，最终就能够完成排序。
    """

    def __init__(self):
        super(AbstractSort.AbstractSort, self).__init__()

    def sort(self, a, visual=False, inplace=True):
        np.random.shuffle(a)
        self.array = a
        if inplace:
            self.sort_func(0, len(a)-1, visual)
        else:
            return self.non_inplace_quick_sort(a)

    def sort_func(self, lo, hi, visual=False):
        # if (lo+15) >= hi:
        #     InsertionSort.InsertionSort().sort(self.array)
        #     return

        if lo >= hi:
            return

        p = self.partition(lo, hi)

        if visual:
            self.visualize()

        self.sort_func(lo, p-1)
        self.sort_func(p + 1, hi)

    def partition(self, lo, hi):
        if lo >= hi:
            return

        i = lo + 1
        j = hi
        pivot = self.array[lo]

        while True:
            while self.less(self.array[i], pivot):
                i += 1
                if i == j:
                    break

            while self.less(pivot, self.array[j]):
                j -= 1
                if j == lo:
                    break

            if i >= j:
                break
            else:
                self.exch(i, j)

        self.exch(lo, j)
        return j

    def non_inplace_quick_sort(self, a):
        if len(a) < 2:
            return a

        pivot = a[0]
        less = [x for x in a[1:] if x <= pivot]
        greater = [x for x in a[1:] if x > pivot]

        return self.non_inplace_quick_sort(less) + [pivot] + self.non_inplace_quick_sort(greater)
