class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t
        self.keys = []
        self.children = []
        self.leaf = leaf

class BTree:
    def __init__(self, t):
        self.root = None
        self.t = t

    def _split_child(self, parent, i):
        t = self.t
        full_node = parent.children[i]
        new_node = BTreeNode(t, full_node.leaf)
        new_node.keys = full_node.keys[t:]
        if not full_node.leaf:
            new_node.children = full_node.children[t:]
        median_key = full_node.keys[t - 1]
        full_node.keys = full_node.keys[:t - 1]
        full_node.children = full_node.children[:t]
        parent.children.insert(i + 1, new_node)
        parent.keys.insert(i, median_key)

    def _insert_non_full(self, node, key):
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
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def insert(self, key):
        if self.root is None:
            self.root = BTreeNode(self.t, True)
            self.root.keys.append(key)
        else:
            if len(self.root.keys) == 2 * self.t - 1:
                new_root = BTreeNode(self.t, False)
                new_root.children.append(self.root)
                self._split_child(new_root, 0)
                self.root = new_root
            self._insert_non_full(self.root, key)

    def search(self, key, node=None):
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return (node, i)
        if node.leaf:
            return None
        return self.search(key, node.children[i])

    def traverse(self):
        if self.root:
            self._traverse(self.root)
            print()

    def _traverse(self, node):
        for i in range(len(node.keys)):
            if not node.leaf:
                self._traverse(node.children[i])
            print(node.keys[i], end=" ")
        if not node.leaf:
            self._traverse(node.children[len(node.keys)])


btree = BTree(t=2)

keys = [10, 20, 5, 6, 12, 30, 7, 17]
for key in keys:
    btree.insert(key)
    print(f"Вставлен: {key}")

print("\nОбход дерева (in-order):")
btree.traverse()

print("Поиск 6:", "найден" if btree.search(6) else "не найден")
print("Поиск 15:", "найден" if btree.search(15) else "не найден")
