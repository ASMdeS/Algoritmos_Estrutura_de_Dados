# Criar o Node
class Node:

    def __init__(self, numero):
        self.numero = numero
        self.proximo_numero = None


# Criar a lista encadeada
class lista_encadeada:
    # Definir a cabeça da lista encadeada
    def __init__(self):
        self.head = None

    # Adicionar novo elemento
    def adicionar(self, numero):
        novo_node = Node(numero)
        if self.head == None:
            self.head = novo_node
        else:
            current = self.head
            previous = None
            while current:
                previous = current
                current = current.proximo_numero
            current = novo_node
            previous.proximo_numero = current
        print(f"Node {numero} adicionado")

    # empurrar determinado elemento
    def empurrar(self, numero):
        previous = None
        current = self.head
        next = None
        if not self.head:
            print(f"Node {numero} não existe")
        else:
            while current and current.numero != numero:
                previous = current
                if current.proximo_numero:
                    next = current.proximo_numero
                current = next
                if next:
                    next = next.proximo_numero
                # else:
                # print(f"Não existe Node depois de {numero}")
                # return
            if not current:
                print(f"Node {numero} não existe")
            elif not current.proximo_numero:
                print(f"Não existe Node depois de {numero}")
            else:
                print(f"Node {numero} empurrado")
                if current == self.head:
                    next = current.proximo_numero
                    self.head = next
                    if not next.proximo_numero:
                        next.proximo_numero = current
                        current.proximo_numero = None
                    else:
                        current.proximo_numero = next.proximo_numero
                        next.proximo_numero = current
                elif next.proximo_numero:
                    previous.proximo_numero = next
                    current.proximo_numero = next.proximo_numero
                    next.proximo_numero = current
                else:
                    previous.proximo_numero = next
                    next.proximo_numero = current
                    current.proximo_numero = None

    # puxar determinado elemento
    def puxar(self, numero):
        first = None
        previous = None
        current = self.head
        if not self.head:
            print(f"Node {numero} não existe")
        elif self.head.numero == numero:
            print(f"Não existe Node antes de {numero}")
        else:
            while current and current.numero != numero:
                first = previous
                previous = current
                current = current.proximo_numero
            if not current:
                print(f"Node {numero} não existe")
            else:
                if first:
                    first.proximo_numero = current
                    previous.proximo_numero = current.proximo_numero
                    current.proximo_numero = previous
                else:
                    previous.proximo_numero = current.proximo_numero
                    current.proximo_numero = previous
                    self.head = current

                print(f"Node {numero} puxado")

    # remover determinado elemento
    def remover(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.numero == key and current is self.head:
                found = True
                self.head = current.proximo_numero
            elif current.numero == key:
                found = True
                previous.proximo_numero = current.proximo_numero
            else:
                previous = current
                current = current.proximo_numero
        if found == True:
            print(f"Node {key} foi removido")
        else:
            print(f"Node {key} não existe")

        return current

    # definir a representação da lista encadeada
    def __repr__(self):
        nodes = []
        current = self.head
        if current:
            while current:
                if current is self.head:
                    nodes.append("mapa:%s" % current.numero)
                else:
                    nodes.append("%s" % current.numero)
                current = current.proximo_numero
            return '->'.join(nodes)
        else:
            return "mapa:"


# definindo a entrada e a lista encadeada
entrada = None
Mapa = lista_encadeada()

# trabalhando com entradas
while entrada != "fim!":
    entrada = input()
    if entrada != "fim!":
        lista_entrada = entrada.split(":")
        numero = lista_entrada[0]
        instrucao = lista_entrada[1]

        if instrucao == "adicione-me!":
            Mapa.adicionar(numero)
        elif instrucao == "remova-me!":
            Mapa.remover(numero)
        elif instrucao == "empurre-me!":
            Mapa.empurrar(numero)
        elif instrucao == "puxe-me!":
            Mapa.puxar(numero)
    else:
        print(Mapa)
