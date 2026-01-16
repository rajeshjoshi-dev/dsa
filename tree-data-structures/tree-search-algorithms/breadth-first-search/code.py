from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def bfs(root):
    if not root:
        return

    queue = deque([root])

    while queue:
        current = queue.popleft()
        print(current.value, end=" ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)

A.left, A.right = B, C
B.left, B.right = D, E

if __name__ == "__main__":
    bfs(A)  # 1 2 3 4 5
