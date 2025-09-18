# Method 1: Using a List
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())  # 10
print(q.peek())  # 20
print(q.size())  # 2


# Method 2: Using collections.deque ✅ (Efficient)
from collections import deque

queue = deque()

queue.append(10)  # enqueue
queue.append(20)
queue.append(30)

print(queue.popleft())  # 10 (dequeue)
print(queue[0])  # 20 (peek)
print(len(queue))  # 2 (size)

# Method 3: Using queue.Queue
from queue import Queue

q = Queue(maxsize=5)

q.put(10)  # enqueue
q.put(20)
q.put(30)

print(q.get())  # 10 (dequeue)
print(q.qsize())  # 2
print(q.empty())  # False
