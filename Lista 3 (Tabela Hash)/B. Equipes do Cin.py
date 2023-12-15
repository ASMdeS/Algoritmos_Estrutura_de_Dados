# Criando a classe Node e definindo a chave, valor e o próximo node
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Criando a classe Hash Table com o tamanho e a tabela em si, alpem de definir o método de inserir e imprimir a tabela
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key, value):
        index = value
        node_novo = Node(key, value)

        if self.table[index] is None or key < self.table[index].key:
            node_novo.next = self.table[index]
            self.table[index] = node_novo
        else:
            current = self.table[index]

            while current.next is not None and key > current.next.key:
                current = current.next

            node_novo.next = current.next
            current.next = node_novo

    def print_table(self):
        lista_impressao = []
        for index, node in enumerate(self.table):
            lista_index = []
            while node:
                lista_index.append(node.key)
                node = node.next
                if len(lista_index) % index == 0:
                    lista_impressao.append(lista_index)
                    lista_index = []
        print(lista_impressao)


# Criando a Hash Table com tamanho 10
hash_table = HashTable(10)

# Recebendo o input e inserindo as informações na Hash Table
try:
    while True:
        entrada_usuario = input().split()
        hash_table.insert(entrada_usuario[0], int(entrada_usuario[1]))

# Quando a input for vazia, a tabela hash é impressa e o código termina
except:
    hash_table.print_table()
