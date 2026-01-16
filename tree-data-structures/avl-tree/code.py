class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.key)


def height(node):
    return node.height if node else 0


def balance_factor(node):
    return height(node.left) - height(node.right)


def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


def insert(node, key):
    if not node:
        return AVLNode(key)

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    node.height = 1 + max(height(node.left), height(node.right))
    bf = balance_factor(node)

    # Rotations
    if bf > 1 and key < node.left.key:
        return right_rotate(node)
    if bf < -1 and key > node.right.key:
        return left_rotate(node)
    if bf > 1 and key > node.left.key:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if bf < -1 and key < node.right.key:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node


root = AVLNode(5)
keys = [3, 6, 34, 1, 8, 9]
for key in keys:
    insert(root, key)

if __name__ == "__main__":
    print(root)
