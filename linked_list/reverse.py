# -*- coding: utf8 -*-


from linked_list import Node
from linked_list import generate_linked_list, linked_list_print


def reverse_1(head: Node):
    """
    用三个指针做翻转
    p 表示翻转后的链表头指针
    q 表示正在翻转的节点
    r 表示剩余的链表
    :param head:
    :return:
    """
    p = head
    q = head.next
    head.next = None
    while q:
        r = q.next
        q.next = p
        p = q
        q = r

    return p


def reverse_2(head: Node):
    """
    递归
    :param head:
    :return:
    """
    # 找到最后一个节点
    if head.next is None or head is None:
        return head
    new_head = reverse_2(head.next)
    head.next.next = head
    head.next = None
    return new_head


if __name__ == '__main__':
    linked = generate_linked_list(10)
    linked_list_print(linked)
    print('reverse linked list')
    linked = reverse_1(linked)
    linked_list_print(linked)
    print('reverse back')
    linked = reverse_2(linked)
    linked_list_print(linked)



