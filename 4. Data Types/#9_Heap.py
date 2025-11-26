class Heap:
    def __init__(self, max_heap=True):
        self.heap = []
        self.max_heap = max_heap

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract(self):
        if self.is_empty():
            raise IndexError("extract from empty heap")
        
        root = self.heap[0]
        last = self.heap.pop()
        
        if not self.is_empty():
            self.heap[0] = last
            self._heapify_down(0)
        return root

    def peek(self):

        if self.is_empty():
            raise IndexError("peek from empty heap")
        return self.heap[0]

    def _heapify_up(self, index):
        if index == 0:
            return
        
        parent_index = (index - 1) // 2
        parent_value = self.heap[parent_index]
        current_value = self.heap[index]

        should_swap = (
            (self.max_heap and current_value > parent_value) or
            (not self.max_heap and current_value < parent_value)
        )
        
        if should_swap:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        smallest_or_largest = index
        
        if left_index < self.size():
            left_value = self.heap[left_index]
            current_value = self.heap[smallest_or_largest]
            
            should_choose_left = (
                (self.max_heap and left_value > current_value) or
                (not self.max_heap and left_value < current_value)
            )
            
            if should_choose_left:
                smallest_or_largest = left_index
        
        if right_index < self.size():
            right_value = self.heap[right_index]
            current_value = self.heap[smallest_or_largest]
            
            should_choose_right = (
                (self.max_heap and right_value > current_value) or
                (not self.max_heap and right_value < current_value)
            )
            
            if should_choose_right:
                smallest_or_largest = right_index
        
        if smallest_or_largest != index:
            self.heap[index], self.heap[smallest_or_largest] = \
                self.heap[smallest_or_largest], self.heap[index]
            self._heapify_down(smallest_or_largest)


h = Heap(max_heap=True)

h.insert(10)
h.insert(4)
h.insert(15)
h.insert(20)
h.insert(3)

print("Корень кучи:", h.peek())

while not h.is_empty():
    print("Извлеченный элемент:", h.extract())
