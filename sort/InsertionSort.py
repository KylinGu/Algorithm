from . import AbstractSort


class InsertionSort(AbstractSort.AbstractSort):

    """
    插入排序，N^2。思想：两层循环，外循环负责向前，内循环负责对比当前外循环的值与前一个元素的大小，然后交换彼此位置。
    内循环，继续向后对比，依次交换。最终实现当前外循环元素和其之前的元素排好序。
    """

    def __init__(self):
        super(AbstractSort.AbstractSort, self).__init__()

    def sort(self, a, visual=False):
        self.array = a
        length = len(self.array)

        for i in range(1, length):
            temp = i
            for j in range(i, -1, -1):
                # 将当前i左边的值与i比较，大于i就交换位置，如果继续向左边尝试比较交换
                if not self.less(self.array[j], self.array[temp]):
                    self.exch(temp, j)
                    temp = j

                    if visual:
                        self.visualize()
                else:
                    continue
