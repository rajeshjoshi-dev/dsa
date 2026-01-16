class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


A = BinaryTreeNode(1)
B = BinaryTreeNode(2)
C = BinaryTreeNode(3)
D = BinaryTreeNode(4)
E = BinaryTreeNode(5)
F = BinaryTreeNode(10)

#         1
#       /   \
#     2       3
#   /   \   /
# 4      5 10

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F


# Recussive DFS Traversal
# Time: O(n)
# Space: O(n)


def recursive_pre_order(node: BinaryTreeNode):
    # Node -> Left -> Right
    if not node:
        return

    print(node)
    recursive_pre_order(node.left)
    recursive_pre_order(node.right)


def recursive_in_order(node: BinaryTreeNode):
    # Left -> Node -> Right
    if not node:
        return

    recursive_in_order(node.left)
    print(node)
    recursive_in_order(node.right)


def recursive_post_order(node: BinaryTreeNode):
    # Left -> Right -> Node
    if not node:
        return

    recursive_post_order(node.left)
    recursive_post_order(node.right)
    print(node)


def pre_order(node: BinaryTreeNode):
    # Node -> Left -> Right
    stack = [node]

    while stack:
        node = stack.pop()

        print(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# Recussive BFS Traversal
# Time: O(n)
# Space: O(n)


def bfs(node: BinaryTreeNode):
    queue = [node]

    while queue:
        node = queue.pop(0)

        print(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# Check if a value exists using DFS
# Time: O(n)
# Space: O(n)


def search(node: BinaryTreeNode, target):
    if not node:
        return False

    if node.val == target:
        return True

    return search(node.left, target) or search(node.right, target)


if __name__ == "__main__":
    recursive_pre_order(A)  # 1, 2, 4, 5, 3, 10
    recursive_in_order(A)  # 4, 2, 5, 1, 10, 3
    recursive_post_order(A)  # 4, 5, 2, 10, 3, 1
    pre_order(A)  # 1, 2, 4, 5, 3, 10
    bfs(A)  # 1, 2, 3, 4, 5, 10
    print(search(A, 100))  # False
    print(search(A, 3))  # True
