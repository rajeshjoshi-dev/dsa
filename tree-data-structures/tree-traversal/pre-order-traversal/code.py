class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)


# Build tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

if __name__ == "__main__":
    preorder(root)  # 1 2 4 5 3
