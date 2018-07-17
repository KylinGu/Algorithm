from abc import ABC, abstractmethod
import pandas as pd
import matplotlib.pyplot as plt


class AbstractSort(ABC):

    def __init__(self):
        self.array = []

    @abstractmethod
    def sort(self): pass

    def exch(self, i, j):
        # print('exch', self.array[i], self.array[j])
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def less(self, a, b):
        return True if a <= b else False

    def show(self):
        print(self.array)

    def is_sorted(self, sorted_array=None):
        if sorted_array is not None:
            a = sorted_array
        else:
            a = self.array

        length = len(a)
        for i in range(length-1):
            if not self.less(a[i], a[i+1]):
                return False
        return True

    def visualize(self):
        series = pd.Series(self.array)
        bar1 = plt.bar(series.index, series.values)
        for rect in bar1:
            height = rect.get_height()
            plt.text(rect.get_x() + rect.get_width() / 2.0, height, '%d' % int(height), ha='center', va='bottom')
        plt.show()
