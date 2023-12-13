class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            # No collision, create a new node
            self.table[index] = Node(key, value)
        else:
            # Collision occurred, add to the linked list
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        previous = None
        while current is not None:
            if current.key == key:
                if previous is None:
                    # If the node to be deleted is the first in the list
                    self.table[index] = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next

    def imprimir_tabela(self):
        lista_impressao = []
        for i, bucket in enumerate(self.table):
            if bucket is not None:
                for key, value in bucket:
                    lista_impressao.append(key)
            else:
                lista_impressao.append('vago')
        print(lista_impressao)

# Example usage:
hash_table = HashTable(10)

hash_table.insert("apple", 5)
hash_table.insert("banana", 8)
hash_table.insert("orange", 3)

print(hash_table.search("apple"))  # Output: 5
print(hash_table.search("banana"))  # Output: 8
print(hash_table.search("grape"))   # Output: None

hash_table.delete("banana")

print(hash_table.search("banana"))  # Output: None

# Recebendo entrada, dividindo ela em ordem e valor, e adicionando ou buscando e criando nova árvore
try:
    while True:
        entrada_usuario = input().split()
        hash_table.insert(entrada_usuario[0], entrada_usuario[1])

# Except para a entrada vazia
except:
    hash_table.imprimir_tabela()
