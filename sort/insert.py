# -*- coding: utf8 -*-


from typing import List


def insert_sort(target: List[int]):
    length = len(target)

    for idx in range(1, length):
        value = target[idx]
        cur = idx
        while cur >= 0:
            cur -= 1
            # 往后移动数据
            if target[cur] > value:
                target[cur + 1] = target[cur]
            else:
                break
        # 插入数据(由于上一步当前游标 - 1, 所以需要 + 1 才表示当前游标)
        target[cur + 1] = value

        print('-=-=-=-=', target)

    return target


if __name__ == '__main__':
    print(insert_sort([4, 5, 6, 1, 3, 2]))
