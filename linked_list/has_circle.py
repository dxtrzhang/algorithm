# -*- coding: utf8 -*-

from linked_list import Node
from linked_list import generate_circle_linked_list, generate_linked_list


def has_circle_1(head: Node) -> bool:
    flag = False
    cur_1 = head
    cur_2 = head.next
    while cur_1:
        while cur_2:
            if cur_2.next == cur_1:
                flag = True
                break
            cur_2 = cur_2.next
        if flag:
            break
        cur_1 = cur_1.next

    return flag


def has_circle_2(head: Node) -> bool:
    flag = False
    cur_1 = head
    cur_2 = head
    step = 0
    while cur_1 and cur_2:
        if cur_1 == cur_2 and step != 0:
            flag = True
            break

        step += 1
        cur_1 = cur_1.next
        if cur_2.next:
            cur_2 = cur_2.next.next
        else:
            cur_2 = None

    return flag


if __name__ == '__main__':
    linked = generate_linked_list(3)
    print(has_circle_3(linked))
    linked = generate_circle_linked_list(3)
    print(has_circle_3(linked))

