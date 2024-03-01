# Criando a classe Node com o usuario e o node anterior e próximo
class Node:
    def __init__(self, usuario):
        self.usuario = usuario
        self.anterior = None
        self.proximo = None


# Criando a classe da lista duplamente encadeada, com as funções de imprimir, adicionar, remover e passar pro final
class ListaDuplamenteEncadeada:

    def __init__(self):
        self.head = None
        self.tail = None

    def adicionar_node(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.anterior = self.tail
            self.tail.proximo = node
            self.tail = node

    def remover_node(self, node):
        node_atual = self.head
        while node_atual:
            if node_atual.usuario == node.usuario:
                if node_atual.anterior:
                    node_atual.anterior.proximo = node_atual.proximo
                else:
                    self.head = node_atual.proximo
                if node_atual.proximo:
                    node_atual.proximo.anterior = node_atual.anterior
                else:
                    self.tail = node_atual.anterior
                return
            node_atual = node_atual.proximo

    def passar_final(self, node):
        self.remover_node(node)
        self.adicionar_node(node)

    def imprimir_lista(self):
        node_atual = self.tail
        while node_atual:
            print(node_atual.usuario)
            node_atual = node_atual.anterior


# Criando o Instagram com a lista duplamente encadeada
instagram = ListaDuplamenteEncadeada()

# Criando o que servirá para receber a entrada
entrada = None

# Recebendo as entradas e rodando as funções
while entrada != "Mark fechou o instagram":
    entrada = input()
    if entrada == "Mark fechou o instagram":
        instagram.imprimir_lista()
    else:
        lista_entrada = entrada.split()
        usuario_mencionado = lista_entrada[-1]
        acao = lista_entrada[1]

        if acao == "seguiu":
            node_novo = Node(usuario_mencionado)
            instagram.adicionar_node(node_novo)
        elif acao == "curtiu" or acao == "comentou":
            node_novo = Node(usuario_mencionado)
            instagram.passar_final(node_novo)
        elif acao == "deixou":
            node_novo = Node(usuario_mencionado)
            instagram.remover_node(node_novo)
