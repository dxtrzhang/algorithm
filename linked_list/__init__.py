# -*- coding: utf8 -*-

from random import shuffle


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


def linked_list_print(linked: Node):
    """
    打印链表值
    :param linked:
    :return:
    """
    tmp_list = []
    cur = linked
    while cur:
        tmp_list.append(cur.data)
        cur = cur.next
    print(tmp_list, '\n')


def generate_linked_list(n: int, start: int = 0, order=False):
    if n == 0:
        return None

    numbers = list(range(start, n))
    if not order:
        shuffle(numbers)

    head = Node(numbers[0])
    cur = head
    for number in numbers[1:]:
        node = Node(number)
        cur.next = node
        cur = cur.next

    return head


def generate_circle_linked_list(n: int):
    if n == 0:
        return None

    numbers = list(range(n))
    shuffle(numbers)

    head = Node(numbers[0])
    cur = head
    for number in numbers[1:]:
        node = Node(number)
        cur.next = node
        cur = cur.next

    cur.next = head

    return head


if __name__ == '__main__':
    linked = generate_linked_list(10)
    linked_list_print(linked)
