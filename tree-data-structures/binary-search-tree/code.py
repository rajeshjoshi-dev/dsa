class BSTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def insert(root: BSTNode, value: int):
    if root is None:
        return BSTNode(value)

    if value < root.val:
        root.left = insert(root.left, value)
    elif value > root.val:
        root.right = insert(root.right, value)

    return root


root = BSTNode(50)

values = [30, 20, 40, 70, 60, 80]
for v in values:
    root = insert(root, v)


# Recussive DFS Traversal (DFS)
# Time: O(n)
# Space: O(n)
def recursive_in_order(node: BSTNode):
    # Left -> Node -> Right
    if not node:
        return

    recursive_in_order(node.left)
    print(node)
    recursive_in_order(node.right)


# Check if a value exists using DFS
# Time: O(log n)
# Space: O(log n)
def search(root, key):
    if root is None or root.val == key:
        return root

    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


# Deleting a Node in BST

# Case 1: Node is a leaf
# → Remove it directly

# Case 2: Node has one child
# → Replace node with its child

# Case 3: Node has two children
# → Replace with inorder successor (smallest in right subtree)


def find_min(node):
    while node.left:
        node = node.left
    return node


def delete(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        # Case 1 & 2
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Case 3
        temp = find_min(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)

    return root


if __name__ == "__main__":
    recursive_in_order(root)  # 20 30 40 50 60 70 80
    print(search(root, 60))  # 60
    delete(root, 60)
    print(search(root, 60))  # None
    recursive_in_order(root)  # 20 30 40 50 70 80
