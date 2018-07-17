from . import AbstractSort


class ShellSort(AbstractSort.AbstractSort):
    """
    希尔排序是对插入排序的一个改进，改进的地方在于规避频繁交换，比如从尾部交换到头部。
    通过一个递增序列，将数组切割成h份，在每份上运用插入排序，这样就能够让交换在大范围内进行。
    然后h遵从递增序列，开始递减，直至递减到1，成为一个彻底的插入排序
    """

    def __init__(self):
        super(AbstractSort.AbstractSort, self).__init__()

    def sort(self, a, visual=False):
        self.array = a

        length = len(a)
        h = 1

        # h_seq = []
        while h < length/3:
            h = h*3 + 1
            # h_seq.append(h)

        while h > 0:
            for i in range(h, length):
                temp = i
                for j in range(temp, 0, -h):
                    if not self.less(self.array[j-h], self.array[temp]):
                        self.exch(temp, j-h)
                        temp = j-h

                        if visual:
                            self.visualize()
                    else:
                        continue
            h = h//3
