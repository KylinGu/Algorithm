from . import AbstractSort


class MergeSort(AbstractSort.AbstractSort):

    """
    MergeSort 归并排序，主要思想是分而治之。通过递归，不断将数组对半分，直至将其分为两两一组，
    然后每组内进行排序，然后进行归并排序。
    """

    def __init__(self):
        super(AbstractSort.AbstractSort, self).__init__()

    def sort(self, a):
        self.array = a
        length = len(a)
        self.aux = [0]*length

        lo = 0
        hi = length - 1
        self.sort_func(lo, hi)

    def sort_func(self, lo, hi):

        if lo >= hi:
            return

        mid = lo + (hi-lo)//2
        self.sort_func(lo, mid)
        self.sort_func(mid+1, hi)
        self.merge(lo, mid, hi)

    def merge(self, lo, mid, hi):

        """
        左边lo到mid, 右边应该是mid+1,hi。所以我们需要让j从mid + 1开始。
        与sort_func()里传入的一致。
        :param lo:
        :param mid:
        :param hi:
        :return:
        """
        for k in range(lo, hi+1):
            self.aux[k] = self.array[k]
        i = lo
        j = mid + 1

        for k in range(lo, hi+1):
            if i > mid:
                self.array[k] = self.aux[j]
                j += 1
            elif j > hi:
                self.array[k] = self.aux[i]
                i += 1
            elif self.less(self.aux[i], self.aux[j]):
                self.array[k] = self.aux[i]
                i += 1
            else:
                self.array[k] = self.aux[j]
                j += 1

