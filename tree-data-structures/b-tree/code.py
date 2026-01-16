class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2 * self.t - 1:
            new_root = BTreeNode()
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.root = new_root
            self.insert_non_full(new_root, key)
        else:
            self.insert_non_full(root, key)

    def split_child(self, parent, i):
        t = self.t
        y = parent.children[i]
        z = BTreeNode(y.leaf)

        parent.keys.insert(i, y.keys[t - 1])
        parent.children.insert(i + 1, z)

        z.keys = y.keys[t:]
        y.keys = y.keys[: t - 1]

        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2 * self.t - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def __str__(self):
        return str(self.root.keys)


root = BTree(5)
keys = [3, 6, 34, 1, 8, 9]
for key in keys:
    root.insert(key)

if __name__ == "__main__":
    print(root)
