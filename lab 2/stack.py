from typing import Any
from linked_list import LinkedList


class Stack:
    _storage: LinkedList
    length: int

    def __init__(self) -> None:
        self.storage = LinkedList()
        self.length = 0

    def __len__(self) -> int:
        return self.length

    def __str__(self) -> str:
        lifo: LinkedList = LinkedList()

        for element in self.storage:
            lifo.push(str(element))

        return '\n'.join(lifo)

    def push(self, element: Any) -> None:
        self.storage.append(element)
        self.length += 1

    def pop(self) -> Any:
        deleted: Any = self.storage.remove_last()
        self.length -= 1

        return deleted


if __name__ == '__main__':
    stack = Stack()
    print(stack)
    print(stack.storage)
    assert len(stack) == 0
    stack.push(3)
    stack.push(10)
    stack.push(1)

    for x in stack.storage:
        print(x)

    print(stack)
    print(stack.storage)
    assert len(stack) == 3
    top_value = stack.pop()
    assert top_value == 1
    assert len(stack) == 2
