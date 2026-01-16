class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")


# Build tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

if __name__ == "__main__":
    postorder(root)  # 4 5 2 3 1
