# Criar classe Node e definir os nodes à direita e à esquerda
class Node:
    def __init__(self, valor):
        self.valor = valor
        self.left = None
        self.right = None


# Criar classe Arvore e definir raiz e as funções inserir, modificar, imprimirArvore e imprimirSubarvores
class Arvore:
    def __init__(self):
        self.raiz = None
        self.lista = []

    def inserir(self, valor):
        self.raiz = self.modificar(self.raiz, valor)

    def modificar(self, node, valor):
        if node is None:
            return Node(valor)

        if valor < node.valor:
            node.left = self.modificar(node.left, valor)
        elif valor > node.valor:
            node.right = self.modificar(node.right, valor)

        return node

    def imprimirArvore(self):
        self.imprimirSubarvores(self.raiz)

    def imprimirSubarvores(self, node):
        if node:
            self.imprimirSubarvores(node.left)
            self.lista.append(node.valor)
            self.imprimirSubarvores(node.right)


# Definindo Arvore:
arvore = Arvore()

# Definindo os valores pela input
valores = list(map(int, input().split()))

# Adicionando os valores na arvore
for valor in valores:
    arvore.inserir(valor)

# Imprimindo a arvore
arvore.imprimirArvore()
print(" ".join(map(str, arvore.lista)))