from typing import Any
from linked_list import LinkedList


class Queue:
    _storage: LinkedList
    length: int

    def __init__(self) -> None:
        self.storage = LinkedList()
        self.length = 0

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        fifo: LinkedList = LinkedList()

        for element in self.storage:
            fifo.append(str(element))

        return ', '.join(fifo)

    def peek(self) -> Any:
        return self.storage.node(0)

    def enqueue(self, element: Any) -> None:
        self.storage.append(element)
        self.length += 1

    def dequeue(self) -> Any:
        deleted: Any = self.storage.pop()
        self.length -= 1

        return deleted


if __name__ == '__main__':
    queue = Queue()
    print(queue)
    assert len(queue) == 0
    queue.enqueue('klient1')
    queue.enqueue('klient2')
    queue.enqueue('klient3')
    assert str(queue) == 'klient1, klient2, klient3'
    print(queue)
    client_first = queue.dequeue()
    assert client_first == 'klient1'
    assert str(queue) == 'klient2, klient3'
    assert len(queue) == 2
    print(queue)
    queue.dequeue()
    queue.dequeue()
    print(queue)
