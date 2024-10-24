class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.arr = [None] * size

    def hash(self, key):
        return key % self.size

    def find(self, key):
        index = self.hash(key)
        node = self.arr[index]
        while node:
            if node.key == key:
                return True
            node = node.next
        return False

    def insert(self, key, value):
        index = self.hash(key)
        node = self.arr[index]
        prev = None

        while node:
            if node.key == key:
                node.value = value
                return
            prev = node
            node = node.next

        new_node = Node(key, value)
        if prev is None:
            self.arr[index] = new_node
        else:
            prev.next = new_node

    def remove(self, key):
        index = self.hash(key)
        node = self.arr[index]
        prev = None

        while node and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return

        if prev is None:
            self.arr[index] = node.next
        else:
            prev.next = node.next
