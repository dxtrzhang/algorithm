# -*- coding: utf8 -*-

from typing import List

from random import shuffle


def bubble_sort(array: List[int]):
    length = len(array)
    count = 0
    for _ in range(length - 1):
        count += 1
        flag = False
        for i in range(length - 1):
            if array[i] > array[i+1]:
                flag = True
                array[i], array[i+1] = array[i+1], array[i]
        print(f'count: {count}')
        print(array)
        # 若无交换, 则表示已经有序
        if not flag:
            break
    return array


if __name__ == '__main__':
    a = list(range(20))
    shuffle(a)
    bubble_sort(a)
    print('-=-=-=-=-=-=-=-=-=-=')

    a = [4, 5, 6, 3, 2, 1]
    bubble_sort(a)
    print('-=-=-=-=-=-=-=-=-=-=')

    a = [3, 5, 4, 1, 2, 6]
    bubble_sort(a)
    print('-=-=-=-=-=-=-=-=-=-=')

    a = [3, 5, 4, 1, 2, 6, 3]
    bubble_sort(a)
    print('-=-=-=-=-=-=-=-=-=-=')

    a = [6, 5, 4, 3, 2, 1]
    bubble_sort(a)
    print('-=-=-=-=-=-=-=-=-=-=')
