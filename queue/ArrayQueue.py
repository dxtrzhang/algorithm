# -*- coding: utf8 -*-


class ArrayQueue:

    def __init__(self):
        self._head = 0
        self._tail = 0
        self._array = []

    @property
    def head(self):
        if not self._array:
            raise AttributeError('Queue is empty.')
        return self._array[0]

    @property
    def tail(self):
        if not self._array:
            raise AttributeError('Queue is empty.')
        return self._array[-1]

    def enqueue(self, item: int):
        self._array.append(item)

    def dequeue(self):
        if not self._array:
            raise AttributeError('Queue is empty.')
        item = self._array[0]
        self._array = self._array[1:]
        return item

    def show(self):
        print(' '.join([str(item) for item in self._array]))


if __name__ == '__main__':
    queue = ArrayQueue()
    queue.enqueue(2)
    queue.enqueue(4)
    queue.show()

    queue.enqueue(3)
    queue.show()
    queue.dequeue()
    queue.show()
