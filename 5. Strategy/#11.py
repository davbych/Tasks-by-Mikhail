import math

class SparseTable:
    def __init__(self, array):
        self.n = len(array)
        if self.n == 0:
            self.st = []
            return
        self.log = math.floor(math.log2(self.n)) + 1
        self.st = [[0] * self.log for _ in range(self.n)]
        self.build(array)

    def build(self, array):
        for i in range(self.n):
            self.st[i][0] = array[i]

        for j in range(1, self.log):
            i = 0
            while i + (1 << j) <= self.n:
                self.st[i][j] = min(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])
                i += 1

    def query(self, left, right):
        if left > right or left < 0 or right >= self.n:
            raise IndexError("Некорректные границы диапазона")
        length = right - left + 1
        k = math.floor(math.log2(length))
        return min(self.st[left][k], self.st[right - (1 << k) + 1][k])

array = [1, 3, 2, 7, 9, 11]
sparse_table = SparseTable(array)

print(sparse_table.query(1, 4))
print(sparse_table.query(0, 5))
print(sparse_table.query(2, 2))
