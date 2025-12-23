import random

class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return

        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]


dsu = DisjointSetUnion(5)
dsu.union(0, 1)
dsu.union(1, 2)
print(dsu.find(0))
print(dsu.find(2))
dsu.union(3, 4)
print(dsu.find(3))
