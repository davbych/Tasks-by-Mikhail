class UnorderedSet:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, value):
        return hash(value) % self.size
    
    def add(self, value):
        index = self._hash(value)
        bucket = self.buckets[index]

        if value not in bucket:
            bucket.append(value)
    
    def remove(self, value):
        index = self._hash(value)
        bucket = self.buckets[index]

        for i, item in enumerate(bucket):
            if item == value:
                del bucket[i]
                return

    def contains(self, value):
        return value in self.buckets[self._hash(value)]
    
    def elements(self):
        els = []
        for i in self.buckets:
            els.extend(i)
        return els
        
my_set = UnorderedSet()

my_set.add(1)
my_set.add(2)
my_set.add(3)

print("Elements:", my_set.elements())

# Check if a value is in the set
value_to_check = 2
print(f"Is {value_to_check} in the set? {my_set.contains(value_to_check)}")

# Remove a value from the set
value_to_remove = 1
my_set.remove(value_to_remove)

print("Elements after removing 1:", my_set.elements())