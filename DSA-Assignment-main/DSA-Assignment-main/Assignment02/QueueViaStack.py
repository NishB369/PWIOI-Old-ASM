class MyQueue:

    def __init__(self):
        self.size = 0
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)
        self.size += 1

    def pop(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())
        a = self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        self.size -= 1
        return a

    def peek(self) -> int:
        while self.s1:
            self.s2.append(self.s1.pop())
        b = self.s2[-1]
        while self.s2:
            self.s1.append(self.s2.pop())
        return b

    def empty(self) -> bool:
        return self.size == 0
