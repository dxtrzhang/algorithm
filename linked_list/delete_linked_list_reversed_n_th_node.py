# -*- coding: utf8 -*-

from linked_list import Node
from linked_list import generate_linked_list, linked_list_print


def delete_n_th_reversed(head: Node, n: int):
    sentinel = Node(0)
    sentinel.next = head
    p = sentinel
    q = sentinel
    for _ in range(n + 1):
        p = p.next
    while p:
        p = p.next
        q = q.next
    q.next = q.next.next

    return sentinel.next


if __name__ == '__main__':
    head = generate_linked_list(10, order=True)
    linked_list_print(head)
    linked_list_print(delete_n_th_reversed(head, 5))
