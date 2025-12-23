class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.bf = 0

class AVLTree:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _update_height(self, node):
        if node:
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self._update_height(z)
        self._update_height(y)
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        self._update_height(z)
        self._update_height(y)
        return y

    def _left_right_rotate(self, z):
        z.left = self._left_rotate(z.left)
        return self._right_rotate(z)

    def _right_left_rotate(self, z):
        z.right = self._right_rotate(z.right)
        return self._left_rotate(z)

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        else:
            return node

        self._update_height(node)
        balance = self._get_balance(node)
        if balance > 1:
            if key < node.left.key:
                return self._right_rotate(node)
            else:
                return self._left_right_rotate(node)

        if balance < -1:
            if key > node.right.key:
                return self._left_rotate(node)
            else:
                return self._right_left_rotate(node)

        return node

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)


avl = AVLTree()

keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    avl.insert(key)
    print(f"Вставлен: {key}")

print("\nIn-order обход (должен быть отсортирован):", avl.inorder_traversal())
print("Высота дерева:", avl._get_height(avl.root))
print("Поиск 25:", avl.search(25))   # True
print("Поиск 100:", avl.search(100)) # False