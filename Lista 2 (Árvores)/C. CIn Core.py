# Criando a classe TreeNode que contem o valor, nível, node à esquerda e à direita
class TreeNode:
    def __init__(self, key, level):
        self.key = key
        self.level = level
        self.left = None
        self.right = None


# Criando a Árvore Binária de Busca e definindo as funções ordem de inserir, inserir, em ordem e encontrar node
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert_order(self, key):
        self.root = self.insert(self.root, key, level=0)

    def insert(self, root, key, level):
        if root is None:
            return TreeNode(key, level)

        if key < root.key:
            root.left = self.insert(root.left, key, level + 1)
        elif key > root.key:
            root.right = self.insert(root.right, key, level + 1)

        return root

    def inorder_traversal(self, root):
        result = []
        if root:
            result += self.inorder_traversal(root.left)
            result.append(root.key)
            result += self.inorder_traversal(root.right)
        return result

    def find_node(self, value, root):
        if root is None:
            return -1
        elif root.key == value:
            return root.level

        if value < root.key:
            return self.find_node(value, root.left)
        else:
            return self.find_node(value, root.right)


# Criando a Árvore de Busca Binária
bst = BinarySearchTree()

# Recebendo entrada, dividindo ela em ordem e valor, e adicionando ou buscando e criando nova árvore
try:
    while True:
        entrada_usuario = input().split()
        if entrada_usuario[0] == "ADD":
            bst.insert_order(int(entrada_usuario[1]))
            print(bst.find_node(int(entrada_usuario[1]), bst.root))

        elif entrada_usuario[0] == "SCH":
            result = bst.find_node(int(entrada_usuario[1]), bst.root)
            print(result)
            if result >= 0:
                lista = bst.inorder_traversal(bst.root)
                lista.remove(int(entrada_usuario[1]))
                lista.insert(0, int(entrada_usuario[1]))
                bst = BinarySearchTree()
                for elemento in lista:
                    bst.insert_order(elemento)

# Except para a entrada vazia
except:
    pass
