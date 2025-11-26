class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def _hash(self, key):
        return sum(ord(char) for char in str(key)) % self.size

    def put(self, key, value):
        hash_value = self._hash(key)
        
        if self.slots[hash_value] is None or self.slots[hash_value] == key:
            self.slots[hash_value] = key
            self.data[hash_value] = value
            return
        
        next_slot = (hash_value + 1) % self.size
        while self.slots[next_slot] is not None and self.slots[next_slot] != key:
            next_slot = (next_slot + 1) % self.size
        
        self.slots[next_slot] = key
        self.data[next_slot] = value

    def get(self, key, default=None):
        start_hash = self._hash(key)
        position = start_hash
        
        while self.slots[position] is not None:
            if self.slots[position] == key:
                return self.data[position]
            position = (position + 1) % self.size
            if position == start_hash:
                break
        
        return default

    def remove(self, key):
        start_hash = self._hash(key)
        position = start_hash
        
        while self.slots[position] is not None:
            if self.slots[position] == key:
                self.slots[position] = None
                self.data[position] = None
                
                next_position = (position + 1) % self.size
                while self.slots[next_position] is not None:
                    curr_key = self.slots[next_position]
                    curr_value = self.data[next_position]

                    self.slots[next_position] = None
                    self.data[next_position] = None
                    
                    self.put(curr_key, curr_value)
                    next_position = (next_position + 1) % self.size
                return
            
            position = (position + 1) % self.size
            if position == start_hash:
                break
        
        raise KeyError(key)

    def keys(self):
        return [key for key in self.slots if key is not None]

    def values(self):
        return [value for value in self.data if value is not None]

    def items(self):
        return [(self.slots[i], self.data[i]) 
                for i in range(self.size)
                if self.slots[i] is not None]
    
# Пример использования 
my_hashmap = HashMap() 
my_hashmap.put("name", "John") 
my_hashmap.put("age", 25) 
my_hashmap.put("city", "Example City") 
print("Keys:", my_hashmap.keys()) # Ожидаемый вывод: Keys: ['name', 'age', 'city'] 
print("Values:", my_hashmap.values()) # Ожидаемый вывод: Values: ['John', 25, 'Example City'] 
print("Items:", my_hashmap.items()) # Ожидаемый вывод: Items: [('name', 'John'), ('age', 25), ('city', 'Example City')] 

# Доступ к значениям по ключу 
print("Name:", my_hashmap.get("name")) # Ожидаемый вывод: Name: John
print("Gender:", my_hashmap.get("gender", "Not specified")) # Ожидаемый вывод: Gender: Not specified 

# Удаление пары ключ-значение 
my_hashmap.remove("age") 
print("Keys after removing 'age':", my_hashmap.keys()) # Ожидаемый вывод: Keys after removing 'age': ['name', 'city']
