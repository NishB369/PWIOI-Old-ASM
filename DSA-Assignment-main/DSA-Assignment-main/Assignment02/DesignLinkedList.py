class Node:
    def __init__(self, data, next_node=None):
        self.val = data
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if index == 0:
            return self.head.val
        current = self.head
        while index:
            current = current.next
            index -= 1
        return current.val

    def add_at_head(self, data: int) -> None:
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1

    def add_at_tail(self, data: int) -> None:
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = new_node
        self.size += 1

    def add_at_index(self, index: int, data: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.add_at_head(data)
        elif index == self.size:
            self.add_at_tail(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            next_node = current.next
            current.next = new_node
            new_node.next = next_node
            self.size += 1

    def delete_at_index(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            next_head = self.head.next
            del self.head
            self.head = next_head
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            to_delete = current.next
            current.next = current.next.next
            del to_delete
        self.size -= 1
