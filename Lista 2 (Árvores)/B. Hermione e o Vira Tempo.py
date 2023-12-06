# Criando o Node
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

# Criando a arvore
class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, root, key):
        if root is None:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        self.update_height(root)

        balance = self.balance_factor(root)

        # Left Heavy
        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        # Right Heavy
        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def reverse_inorder_traversal(self, root, count, sum_values):
        if root and count[0] > 0:
            # Traverse the right subtree
            self.reverse_inorder_traversal(root.right, count, sum_values)

            # Update sum
            sum_values[0] += root.key

            # Update count
            count[0] -= 1

            # Traverse the left subtree
            self.reverse_inorder_traversal(root.left, count, sum_values)

    def print_highest_values_with_sum(self, count):
        sum_values = [0]
        self.reverse_inorder_traversal(self.root, [count], sum_values)
        print("valor total de conhecimento:", sum_values[0])


# Inicializar a arvore
avl_tree = AVLTree()
# Recebendo as aulas totais
aulasTotais = list(map(int, input().split()))

# Definindo as aulas de Hogwarts
aulasHogwarts = aulasTotais[0]

# Definindo as aulasCin
aulasCin = aulasTotais[1]

# Recebendo os valores Hogwarts
valoresHogwarts = list(map(int, input().split()))

# Recebendo os valores Cin
valoresCin = list(map(int, input().split()))

# Adicionando os valores Hogwarts a arvore
for valor in valoresHogwarts:
    avl_tree.insert_key(valor)

# Adicionando os valores Cin a arvore
for valor in valoresCin:
    avl_tree.insert_key(valor)

# Recebendo as horas disponiveis no viratempo
horasDisponiveis = int(input())

# Imprimindo a soma dos maiores valores considerando as horas disponiveis no viratempo
avl_tree.print_highest_values_with_sum(horasDisponiveis)
