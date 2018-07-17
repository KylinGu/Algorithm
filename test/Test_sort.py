from sort import SelectionSort as sst
from sort import InsertionSort as ist
from sort import ShellSort as shst
from sort import QuickSort as qst
from sort import BubbleSort as bst
from sort import MergeSort as mst
from sort import MinPQ as mpq
from base import Stack
import numpy as np
import time


"""
测试数组
test_array = np.random.randint(1, 10000, 5000).tolist()
N^2的排序
Bubble Sort Time Consume:  6.510536099093616
Selection Sort Time Consume:  2.1769541338356015
Insertion Sort Time Consume:  3.7019110559128823

Shell Sort Time Consume:  3.4329716775509542

NLOGN的排序
Quick Sort Time Consume:  0.008955889852117593
Merge Sort Time Consume:  0.028297774341597304

N的排序
Min Priority Queue Time Consume:  1.208901194255727

堆排序LOGN

"""


def test_bubble_sort(a):
    bubble_sort = bst.BubbleSort()
    bubble_sort.sort(a)

    return bubble_sort


def test_selection_sort(a):
    selection_sort = sst.SelectionSort()
    selection_sort.sort(a, visual=False)

    return selection_sort


def test_insertion_sort(a):
    insertion_sort = ist.InsertionSort()
    insertion_sort.sort(a, visual=False)

    return insertion_sort


def test_shell_sort(a):
    shell_sort = shst.ShellSort()
    shell_sort.sort(a, visual=False)

    return shell_sort


def test_quick_sort(a):
    quick_sort = qst.QuickSort()
    ret = quick_sort.sort(a, visual=False, inplace=False)

    return ret


def test_merge_sort(a):
    merge_sort = mst.MergeSort()
    merge_sort.sort(a)

    return merge_sort


def test_priority_queue(a, M):
    min_pq = mpq.MinPriorityQueue()
    for item in a:
        min_pq.insert(item)
        if min_pq.size() > M:
            min_pq.del_min()
            # print('drop current min:', )

    stack = Stack.Stack()
    for i in range(min_pq.size()):
        stack.push(min_pq.del_min())

    # for item in stack:
    #     print('stack：', item.item)


if __name__ == '__main__':

    test_array = np.random.randint(1, 10000, 5000).tolist()
    print('原始数组: \n', test_array)

    np.random.shuffle(test_array)
    t0 = time.clock()
    sort_func = test_bubble_sort(test_array)
    print('Bubble Sort Time Consume: ', time.clock() - t0)
    assert sort_func.is_sorted()

    t0 = time.clock()
    sort_func = test_selection_sort(test_array)
    print('Selection Sort Time Consume: ', time.clock() - t0)
    assert sort_func.is_sorted()

    np.random.shuffle(test_array)
    t0 = time.clock()
    sort_func = test_insertion_sort(test_array)
    print('Insertion Sort Time Consume: ', time.clock() - t0)
    assert sort_func.is_sorted()

    np.random.shuffle(test_array)
    t0 = time.clock()
    sort_func = test_shell_sort(test_array)
    print('Shell Sort Time Consume: ', time.clock() - t0)
    assert sort_func.is_sorted()

    np.random.shuffle(test_array)
    t0 = time.clock()
    ret = test_quick_sort(test_array)
    print('Quick Sort Time Consume: ', time.clock() - t0)
    assert sort_func.is_sorted(ret)

    np.random.shuffle(test_array)
    t0 = time.clock()
    sort_func = test_merge_sort(test_array)
    print('Merge Sort Time Consume: ', time.clock() - t0)
    assert sort_func.is_sorted()

    # np.random.shuffle(test_array)
    # t1 = time.clock()
    # sorted(test_array)
    # print('Lib Sort Time Consume:', time.clock() - t1)

    np.random.shuffle(test_array)
    t0 = time.clock()
    test_priority_queue(test_array, 50)
    print('Min Priority Queue Time Consume: ', time.clock() - t0)
