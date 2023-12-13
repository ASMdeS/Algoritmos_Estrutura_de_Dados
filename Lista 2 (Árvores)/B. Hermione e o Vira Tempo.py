class Node:
    def __init__(self, valor):
        self.valor = valor
        self.pai = None
        self.direita = None
        self.esquerda = None


class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        item = Node(valor)

        if self.raiz == None:
            self.raiz = item

        else:
            adicionado = False
            itemAtual = self.raiz
            while not adicionado:
                if itemAtual.valor < item.valor:
                    if itemAtual.direita == None:
                        itemAtual.direita = item
                        item.pai = itemAtual
                        adicionado = True
                    else:
                        itemAtual = itemAtual.direita
                else:
                    if itemAtual.esquerda == None:
                        itemAtual.esquerda = item
                        item.pai = itemAtual
                        adicionado = True
                    else:
                        itemAtual = itemAtual.esquerda

    def buscaCulpado(self):
        culpado = self.raiz
        while culpado and culpado.esquerda:
            culpado = culpado.esquerda
        return culpado.valor if culpado else None

arvore = Arvore()
numeros = list(map(int, input().split()))
for num in numeros:
    arvore.inserir(num)

culpado = arvore.buscaCulpado()
print(f"{culpado} puxou a camisa de {arvore.raiz.valor}")
# Criando o Node
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.altura = 1
        self.esquerda = None
        self.direita = None


# Criando a árvore e definindo suas funções principais
class AVLTree:
    def __init__(self):
        self.raiz = None

    def altura(self, node):
        if node is None:
            return 0
        return node.altura

    def modificar_altura(self, node):
        if node is not None:
            node.altura = 1 + max(self.altura(node.esquerda), self.altura(node.direita))

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.altura(node.esquerda) - self.altura(node.direita)

    def rotacionar_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        self.modificar_altura(y)
        self.modificar_altura(x)

        return x

    def rotacionar_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        self.modificar_altura(x)
        self.modificar_altura(y)

        return y

    def inserir(self, raiz, key):
        if raiz is None:
            return AVLNode(key)

        if key < raiz.key:
            raiz.esquerda = self.inserir(raiz.esquerda, key)
        else:
            raiz.direita = self.inserir(raiz.direita, key)

        self.modificar_altura(raiz)

        balance = self.balance_factor(raiz)

        if balance > 1:
            if key < raiz.esquerda.key:
                return self.rotacionar_direita(raiz)
            else:
                raiz.esquerda = self.rotacionar_esquerda(raiz.esquerda)
                return self.rotacionar_direita(raiz)

        if balance < -1:
            if key > raiz.direita.key:
                return self.rotacionar_esquerda(raiz)
            else:
                raiz.direita = self.rotacionar_direita(raiz.direita)
                return self.rotacionar_esquerda(raiz)

        return raiz

    def inserir_chave(self, key):
        self.raiz = self.inserir(self.raiz, key)

    def emOrdemReverso(self, raiz, sum_values, horasDisponiveis):
        if raiz is not None:
            self.emOrdemReverso(raiz.direita, sum_values, horasDisponiveis)

            if len(sum_values) < horasDisponiveis:
                sum_values.append(raiz.key)
            else:
                if raiz.key > min(sum_values):
                    sum_values.remove(min(sum_values))
                    sum_values.append(raiz.key)

            self.emOrdemReverso(raiz.esquerda, sum_values, horasDisponiveis)

    def MaiorSoma(self, horasDisponiveis):
        sum_values = []
        self.emOrdemReverso(self.raiz, sum_values, horasDisponiveis)
        print("valor total de conhecimento:", sum(sum_values))


# Inicializar a árvore
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

# Adicionando os valores Hogwarts à árvore
for valor in valoresHogwarts:
    avl_tree.inserir_chave(valor)

# Adicionando os valores Cin à árvore
for valor in valoresCin:
    avl_tree.inserir_chave(valor)

# Recebendo as horas disponíveis no vira-tempo
horasDisponiveis = int(input())

# Imprimindo a soma dos maiores valores considerando as horas disponíveis no vira-tempo
avl_tree.MaiorSoma(horasDisponiveis)
