# -*- coding: utf8 -*-

from typing import List

from random import shuffle


"""
归并排序
使用了递归的思想
"""


def _merge(array_1: List[int], array_2: List[int]):
    tmp = []
    i = j = 0
    while i < len(array_1) and j < len(array_2):
        if array_1[i] < array_2[j]:
            tmp.append(array_1[i])
            i += 1
        elif array_1[i] > array_2[j]:
            tmp.append(array_2[j])
            j += 1
        else:
            tmp.append(array_1[i])
            tmp.append(array_2[j])
            i += 1
            j += 1
    if i < len(array_1):
        tmp.extend(array_1[i:])
    if j < len(array_2):
        tmp.extend(array_2[j:])
    return tmp


def merge_sort(array: List[int]):
    length = len(array)
    if length == 1:
        return array
    mid = length // 2
    array_1 = merge_sort(array[:mid])
    array_2 = merge_sort(array[mid:])

    return _merge(array_1, array_2)


if __name__ == '__main__':
    print(merge_sort([4, 5, 6, 1, 3, 2]))

    a = list(range(19))
    shuffle(a)
    print(merge_sort(a))



