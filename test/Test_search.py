"""
Frequency Cunter
"""

from search import BinarySearchST
from search import SequentialSearchST
from search import SeparateChainingHashST
import time


def get_search_func():
    # bst = BinarySearchST.BinarySearchST()
    # search_func = SequentialSearchST.SequentialSearchST()
    search_func = SeparateChainingHashST.SeparateChainingHashST(3000)

    return search_func


def test_tiny_tale(search_func):
    with open(r'C:\Users\carye\PycharmProjects\Algorithims\search\tale.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace('\n', '')
            for word in line.split(' '):
                if search_func.get(word) is None:
                    search_func.put(word, 1)
                else:
                    count = search_func.get(word)
                    search_func.put(word, count + 1)


    # max = ' '
    # search_func.put(max, 0)
    #
    # for key in search_func.keys():
    #     if search_func.get(key) > search_func.get(max):
    #         max = key
    #
    # print('max key:', max, ', val: ', search_func.get(max))

def test_tiny_tale_baseline():
    d = {}
    with open(r'C:\Users\carye\PycharmProjects\Algorithims\search\tale.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace('\n', '')
            for word in line.split(' '):
                if d.get(word) is None:
                    d.update({word: 1})
                else:
                    count = d.get(word)
                    d.update({word: count + 1})

def test_example(search_func):
    for alphabelt in 'SEARCHEXAMPLE':
        if search_func.get(alphabelt) is None:
            search_func.put(alphabelt, 1)
        else:
            count = search_func.get(alphabelt)
            search_func.put(alphabelt, count + 1)


if __name__ == '__main__':

    search_func = get_search_func()

    start = time.clock()
    test_tiny_tale(search_func)
    print('tale story time consuming:', time.clock() - start)

    start = time.clock()
    test_tiny_tale_baseline()
    print('tale story base line time consuming:', time.clock() - start)

    start = time.clock()
    test_example(search_func)
    print('search example time consuming:', time.clock() - start)

    # for key in search_func.keys():
    #     print('key:',  key, 'val:', search_func.get(key))


