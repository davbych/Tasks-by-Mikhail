class AVLNode:
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None



class AVLTree:
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)


    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y


    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))


        return y


    def insert(self, root, data):
        if not root:
            return AVLNode(data)
        
        
        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        else:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and data < root.left.data:
            return self.rotate_right(root)

        if balance < -1 and data > root.right.data:
            return self.rotate_left(root)

        if balance > 1 and data > root.left.data:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and data < root.right.data:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, data):
        if not root:
            return root

        if data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)


        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left),
                                 self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def search(self, root, data):
        if not root or root.data == data:
            return root
        if data < root.data:
            return self.search(root.left, data)
        return self.search(root.right, data)

    def in_order_traversal(self, root):
        result = []
        if root:
            result.extend(self.in_order_traversal(root.left))
            result.append(root.data)
            result.extend(self.in_order_traversal(root.right))
        return result


avl_tree = AVLTree()
root = None
root = avl_tree.insert(root, 10)
root = avl_tree.insert(root, 20)
root = avl_tree.insert(root, 30)


print(avl_tree.in_order_traversal(root))
