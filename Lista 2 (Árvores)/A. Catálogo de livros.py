#Criar classe Node e definir os nodes à direita e à esquerda
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Criar classe Arvore e definir raiz e as funções
class Arvore:
    def __init__(self):
        self.root = None

    def inserir(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)

        return node

    def print_in_order(self):
        self._print_in_order(self.root)

    def _print_in_order(self, node):
        if node:
            # Traverse the left subtree
            self._print_in_order(node.left)

            # Print the current node's value
            print(node.value, end=" ")

            # Traverse the right subtree
            self._print_in_order(node.right)

# Example usage:
arvore = Arvore()
values = list(map(int, input().split()))

for value in values:
    arvore.inserir(value)

arvore.print_in_order()
