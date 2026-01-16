from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def dfs(root):
    if not root:
        return

    print(root.value, end=" ")
    dfs(root.left)
    dfs(root.right)


A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)

A.left, A.right = B, C
B.left, B.right = D, E

if __name__ == "__main__":
    dfs(A)  # 1 2 4 5 3
