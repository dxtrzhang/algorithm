# -*- coding: utf8 -*-

from typing import List

from random import shuffle


def select_sort(array: List[int]):
    length = len(array)

    for i in range(length):
        smallest = i
        for j in range(i, length):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]

    return array


if __name__ == '__main__':
    a = list(range(20))
    shuffle(a)
    print(select_sort(a))
