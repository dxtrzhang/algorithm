# -*- coding: utf8 -*-

from typing import List


def partition(array: List[int], p: int, r: int):
    i = j = p
    pivot = array[r]
    while j < r:
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
        j += 1
    array[i], array[r] = array[r], array[i]

    return i


def quick_sort(array: List[int], p: int, r: int):
    if p >= r:
        return
    # get partition
    q = partition(array, p, r)
    # sort left part
    quick_sort(array, p, q-1)
    # sort right part
    quick_sort(array, q+1, r)

    return


if __name__ == '__main__':
    a = [3, 4, 6, 11, 3, 7, 9, 8]
    print(a)
    quick_sort(a, 0, len(a)-1)
    print(a)

