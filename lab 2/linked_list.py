from typing import Any


class _Node:
    value: Any
    next: None

    def __init__(self, value: Any) -> None:
        self.value = value
        self.next: None = None


class LinkedList:
    head: _Node
    tail: _Node
    copy: _Node
    length: int

    def __init__(self) -> None:
        self.head: None = None
        self.copy: None = None
        self.tail: None = None
        self.length: int = 0

    def __iter__(self):
        if self.head:
            self.copy = _Node(self.head.value)
            self.copy.next = self.head.next

        return self

    def __len__(self) -> int:
        return self.length

    def __next__(self):
        if self.copy:
            if self.copy.next:
                self.copy = self.copy.next

                return self.copy.value

        raise StopIteration

    def __str__(self) -> str:
        linked_list: LinkedList = LinkedList()

        for node in self:
            linked_list.append(str(node))

        return ' -> '.join(linked_list)

    def append(self, value: Any) -> None:
        if self.head:
            node: _Node = _Node(value)
            self.tail.next = node
            self.tail = node

        else:
            self.head = _Node(None)
            self.tail = _Node(value)
            self.head.next = self.tail
            self.copy = _Node(self.head.value)
            self.copy.next = self.head.next

        self.length += 1

    def insert(self, value: Any, after: _Node) -> None:
        new: _Node = _Node(value)
        node: _Node = after.next
        after.next = new
        new.next = node

        if self.head:
            self.copy = _Node(self.head.value)
            self.copy.next = self.head.next

        else:
            self.copy: None = None

        self.length += 1

    def node(self, at: int) -> _Node:
        node: _Node = self.head.next

        for index in range(at):
            node = node.next

        return node

    def pop(self) -> Any:
        node: _Node = self.head.next
        self.head.next = node.next

        if self.head:
            self.copy = _Node(self.head.value)
            self.copy.next = self.head.next

        else:
            self.copy: None = None

        self.length -= 1

        return node.value

    def push(self, value: Any) -> None:
        if self.head:
            node: _Node = self.head.next
            new: _Node = _Node(value)
            self.head.next = new
            new.next = node

        else:
            self.head = _Node(None)
            self.tail = _Node(value)
            self.head.next = self.tail
            self.copy = _Node(self.head.value)
            self.copy.next = self.head.next

        self.length += 1

    def remove(self, after: _Node) -> Any:
        node: _Node = after.next
        after.next = node.next

        if self.head:
            self.copy = _Node(self.head.value)
            self.copy.next = self.head.next

        else:
            self.copy: None = None

        self.length -= 1

        return node.value

    def remove_last(self) -> Any:
        node: _Node = self.head

        while node.next.next:
            node = node.next

        value: Any = node.next.value
        node.next = None

        if self.head:
            self.copy = _Node(self.head.value)
            self.copy.next = self.head.next

        else:
            self.copy: None = None

        self.length -= 1

        return value


if __name__ == '__main__':
    li: LinkedList = LinkedList()
    print(li)
    assert li.head is None
    li.push(1)
    li.push(0)
    assert str(li) == '0 -> 1'
    li.append(9)
    li.append(10)
    assert str(li) == '0 -> 1 -> 9 -> 10'
    middle_node = li.node(at=1)
    li.insert(5, after=middle_node)
    assert str(li) == '0 -> 1 -> 5 -> 9 -> 10'
    print(li)
    first_element = li.node(at=0)
    returned_first_element = li.pop()
    assert first_element.value == returned_first_element
    last_element = li.node(at=3)
    returned_last_element = li.remove_last()
    assert last_element.value == returned_last_element
    assert str(li) == '1 -> 5 -> 9'
    second_node = li.node(at=1)
    li.remove(second_node)
    assert str(li) == '1 -> 5'
