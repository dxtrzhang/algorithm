# -*- coding: utf8 -*-

from linked_list import Node
from linked_list import generate_linked_list, linked_list_print


def merge(head_1: Node, head_2: Node):
    # 哨兵
    sentinel = Node(0)
    cur = sentinel

    while head_1 or head_2:
        if not head_2:
            cur.next = head_1
            head_1 = head_1.next
        elif not head_1:
            cur.next = head_2
            head_2 = head_2.next
        else:
            if head_1.data <= head_2.data:
                cur.next = head_1
                head_1 = head_1.next
            else:
                cur.next = head_2
                head_2 = head_2.next
        cur = cur.next

    return sentinel.next


if __name__ == '__main__':
    a = generate_linked_list(3, order=True)
    linked_list_print(a)
    b = generate_linked_list(10, start=5, order=True)
    linked_list_print(b)
    print('-=-=-=-=-=-=-=-=')
    linked_list_print(merge(a, b))

    print('+++++++++++++++++++++++ test2')

    sentinel = Node(0)
    cur = sentinel
    for item in range(1, 11, 2):
        cur.next = Node(item)
        cur = cur.next
    a = sentinel.next
    linked_list_print(a)
    sentinel = Node(0)
    cur = sentinel
    for item in range(2, 11, 2):
        cur.next = Node(item)
        cur = cur.next
    b = sentinel.next
    linked_list_print(b)
    print('-=-=-=-=-=-=-=-=')
    linked_list_print(merge(a, b))













