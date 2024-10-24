class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
        
class doublyLL:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def size(self) -> int:
        return self.__size

    def isEmpty(self):
        return self.__size == 0

    def peekFirst(self):
        if self.isEmpty():
            return "Empty List"
        return self.__head.data

    def peekLast(self):
        if self.isEmpty():
            return "Empty List"
        return self.__tail.data

    def indexOf(self, data):

        trav = self.__head
        index = 0

        while trav is not None:
            if trav.data == data:
                return index

            index += 1
            trav = trav.next

        return -1

    def contains(self, data):
        return self.indexOf(data) != -1

    def append(self, elem):
        newnode = Node(elem, None, None)
        if self.isEmpty():
            self.__head = newnode
            self.__tail = newnode
        else:
            newnode.prev = self.__tail
            newnode.next = None
            self.__tail.next = newnode
            self.__tail = self.__tail.next
        self.__size += 1

    def addFirst(self, elem):
        newnode = Node(elem, None, None)
        if self.isEmpty():
            self.__head = newnode
            self.__tail = newnode
        else:
            newnode.next = self.__head
            newnode.prev = None
            self.__head.prev = newnode
            self.__head = self.__head.prev
        self.__size += 1

    def addInd(self, ind, elem):
        if ind < 0:
            raise Exception("Negative Index")

        if ind >= self.__size:
            raise Exception("Index Out of Bound")

        if ind == 0:
            self.addFirst()

        if ind == self.__size:
            self.append()

        trav = self.__head
        for _ in range(0, ind - 1):
            trav = trav.next

        newnode = Node(elem, None, None)

        newnode.next = trav.next
        newnode.prev = trav
        trav.next = newnode
        trav.next.prev = newnode
        
        self.__size+=1
        
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("Empty List")

        self.__head = self.__head.next
        self.__size -= 1

        if self.isEmpty():
            self.__tail = None
        else:
            self.__head.prev = None

    def removeLast(self):
        if self.isEmpty():
            raise Exception("Empty List")

        self.__tail = self.__tail.prev
        self.__size -= 1

        if self.isEmpty():
            self.__head = None
        else:
            self.__tail.next = None

            raise Exception("Empty List")

    def __remove__(self, node):

        if node.prev == None:
            self.removeFirst()
            return

        if node.next == None:
            self.removeLast()
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        del node
        self.__size -= 1
        return None

    def removeAt(self, index):

        if index < 0 or index >= self.__size:
            raise Exception("Invalid index")

        trav = self.__head
        i = 0
        while i != index:
            trav = trav.next
            i += 1

        return self.__remove__(trav)
    
    def mid(self):
        if self.isEmpty():
            return None
        slow = self.__head
        fast = self.__head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def reverse(self):
        prev = None
        curr = self.__head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.__head = prev
        
    def merge(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.data < l2.data:
            self.__head = l1
            l1 = l1.next
        else:
            self.__head = l2
            l2 = l2.next
        current = self.__head
        while l1 and l2:
            if l1.data < l2.data:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l1:
            current.next = l1
        if l2:
            current.next = l2
        return self.__head
    
    def interleave(self, list1, list2):
        l1 = list1
        l2 = list2
        while l1 and l2:
            pl1 = l1.next
            pl2 = l2.next
            l1.next = l2
            l2.next = pl1
            l1 = pl1
            l2 = pl2
        return list1
    
    def split_two(self, ind):
        l2 = self.__head
        for _ in range(ind - 1):
            l2 = l2.next
        r = l2.next
        l2.next = None
        return r
