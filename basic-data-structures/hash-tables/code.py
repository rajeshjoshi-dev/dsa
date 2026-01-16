class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # list of buckets

    def hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)
        # Check if key exists already
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self.hash_function(key)
        self.table[index] = [(k, v) for (k, v) in self.table[index] if k != key]

    def __str__(self):
        return str(self.table)


# Example usage
ht = HashTable()

ht.put("apple", 100)
ht.put("banana", 200)
ht.put("orange", 300)
print(
    ht
)  # [[], [], [('banana', 200)], [('orange', 300)], [], [], [], [], [], [('apple', 100)]]

ht.put(
    "apple", 400
)  # [[], [], [('banana', 200)], [('orange', 300)], [], [], [], [], [], [('apple', 400)]]
print(ht)

print(ht.get("banana"))  # 200

ht.remove("banana")
print(ht)  # [[], [], [], [('orange', 300)], [], [], [], [], [], [('apple', 400)]]
