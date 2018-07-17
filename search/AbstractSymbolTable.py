from abc import ABC, abstractmethod


class AbstractSymbolTable(ABC):

    @abstractmethod
    def put(self, key, val):
        pass

    @abstractmethod
    def get(self, key):
        pass

    def delete(self, key):
        self.put(key, None)

    def contains(self, key):
        return self.get(key)

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def keys(self):
        pass

    # ordered symbol table as following method
    def min(self):
        """
        return the key of min value
        :return:
        """
        pass

    def max(self):
        """
        return the key of the max value
        :return:
        """
        pass

    def floor(self, key):
        """
        小于等于key的最大键
        :param key:
        :return:
        """
        pass

    def celling(self, key):
        """
        大于等于key的最小键
        :param key:
        :return:
        """
        pass

    def rank(self, key):
        """
        小于key的键的数量
        :param key:
        :return:
        """
        pass

    def select(self, k):
        """
        排名为k的key
        :param rank:
        :return:
        """
        pass

    def delete_min(self):
        pass

    def delete_max(self):
        pass

    def size(self, lo, hi):
        """
        返回键lo和键hi之间键的数量
        :param lo:
        :param hi:
        :return:
        """
        pass

    def keys(self, lo, hi):
        """
        返回键lo和hi之间的所有keys，已排序。
        :param lo:
        :param hi:
        :return:
        """
        pass
