# Method 1: Using a List
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # O(1)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()  # O(1)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.pop())  # 30
print(s.peek())  # 20
print(s.size())  # 2

# Method 2: Using collections.deque
from collections import deque

stack = deque()

stack.append(10)  # push
stack.append(20)
stack.append(30)

print(stack.pop())  # 30 (pop)
print(stack[-1])  # 20 (peek)
print(len(stack))  # 2 (size)


# Method 3: Using queue.LifoQueue
from queue import LifoQueue

stack = LifoQueue(maxsize=5)

stack.put(10)  # push
stack.put(20)
stack.put(30)

print(stack.get())  # 30 (pop)
print(stack.qsize())  # 2 (size)
print(stack.full())  # False
