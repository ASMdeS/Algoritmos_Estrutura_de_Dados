class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)  # Adding ASCII values of characters
        return total % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    self.table[index][i] = (key, value)
                    break
            else:
                self.table[index].append((key, value))

    def get(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for existing_key, value in self.table[index]:
                if existing_key == key:
                    return value
        raise KeyError(f"Key '{key}' not found in the hash table.")

    def remove(self, key):
        index = self._hash_function(key)
        if self.table[index] is not None:
            for i, (existing_key, _) in enumerate(self.table[index]):
                if existing_key == key:
                    del self.table[index][i]
                    break
        else:
            raise KeyError(f"Key '{key}' not found in the hash table.")


# Example usage:
hash_table = HashTable(size=10)


def create_groups(s):
    groups = []
    seen_students = set()

    for student in s:
        if student not in seen_students:
            seen_students.add(student)
            groups.append(student)
        else:
            # Start a new group when a student is repeated
            yield ''.join(groups)
            groups = [student]
            seen_students = {student}

    # Yield the last group
    yield ''.join(groups)

# Example usage:
result_groups = list(create_groups(input()))
print(result_groups)


hash_table.insert("name", "John")
hash_table.insert("age", 25)
hash_table.insert("city", "New York")

print(hash_table.get("name"))  # Output: John
print(hash_table.get("age"))  # Output: 25
print(hash_table.get("city"))  # Output: New York

hash_table.remove("age")
# Trying to access the removed key will raise a KeyError
# print(hash_table.get("age"))  # Uncommenting this line will raise KeyError
