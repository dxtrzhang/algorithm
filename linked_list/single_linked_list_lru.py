# -*- coding: utf8 -*-

from linked_list import Node


def simulate_apply_ram(data: int):
    """
    模拟申请内存操作
    :param data:
    :return:
    """
    return False if data > 100 else True


def _delete_by_data(linked: Node, data: int):
    """
    从链表中删除值为 data 的节点
    若 data 不在链表中, 返回 False, 否则返回 True
    :param linked:
    :param data:
    :return:
    """
    # 游标
    cur = linked
    exist = False
    while cur:
        if cur.data == data or (cur.next and cur.next.data == data):
            cur.next = cur.next.next
            exist = True
            break
        cur = cur.next
    return exist


def single_linked_list_lru(linked: Node, data: int):
    """
    用单链表实现 lru 算法
    :param linked:
    :param data:
    :return:
    """
    node = Node(data)
    if linked:
        # 删除链表中相同的数据
        _delete_by_data(linked, data)
        # linked_list_print(linked)
        # print('---')
        # 申请内存失败, 删除链表的尾节点
        if not simulate_apply_ram(data):
            cur = linked
            while cur:
                if not cur.next.next:
                    cur.next = None
                cur = cur.next
        # 将数据插入到链表头部
        node.next = linked

    return node


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


if __name__ == '__main__':
    # 构建初始化 LRU 链表
    tmp = Node(97)
    origin = tmp
    for i in reversed(range(98, 105)):
        i_node = Node(i)
        tmp.next = i_node
        tmp = tmp.next
    print('origin')
    linked_list_print(origin)

    # 插入链表中存在的数据
    print('insert exists 97')
    origin = single_linked_list_lru(origin, 97)
    linked_list_print(origin)
    print('insert exists 99')
    origin = single_linked_list_lru(origin, 99)
    linked_list_print(origin)
    # 插入链表中不存在的数据
    print('insert not exists 66')
    origin = single_linked_list_lru(origin, 66)
    linked_list_print(origin)
    print('insert fail ram 105')
    # 分配内存失败
    origin = single_linked_list_lru(origin, 105)
    linked_list_print(origin)
