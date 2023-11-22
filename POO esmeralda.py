class Node:

    def __init__(self, numero):
        self.numero = numero
        self.proximo_numero = None

class lista_encadeada:

    def __init__(self):
        self.head = None

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

    def empurrar(self, numero):
        node_empurrado = Node(numero)
        current = self.head
        previous = None
        next = None
        last = None
        if self.head is None:
            print(f"Node {numero} não existe")
        elif current.numero == node_empurrado.numero:
            next = current.proximo_numero
            last = next.proximo_numero
            next = current
            current = current.proximo_numero
            current.proximo_numero = next
            next.proximo_numero = last
            self.head = current
        else:
            while current:
                if current.numero == node_empurrado.numero:
                    if next.numero == last.numero:
                        last = None
                    previous.proximo_numero = next
                    next.proximo_numero = current
                    current.proximo_numero = last
                    break
                else:
                    previous = current
                    current = current.proximo_numero
                    if current.proximo_numero:
                        next = current.proximo_numero
                    if next.proximo_numero:
                        last = next.proximo_numero
    def puxar(self, numero):
        node_empurrado = Node(numero)
        if self.head is None:
            print(f"Node {numero} não existe")
        else:
            current = self.head
            previous = None
            next = None
            first = None
            while current:
                if current.numero == node_empurrado.numero:
                    if first.proximo_numero:
                        first.proximo_numero = current
                    current = previous
                    current.proximo_numero = next
                    if first.proximo_numero:
                        previous = first.proximo_numero
                    previous.proximo_numero = current
                    current.proximo_numero = next
                    break
                else:
                    if previous:
                        first = previous
                        first.proximo_numero = previous
                    previous = current
                    current = current.proximo_numero
                    if current.proximo_numero:
                        next = current.proximo_numero


    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("Mapa:%s" % current.numero)
            else:
                nodes.append("%s" % current.numero)
            current = current.proximo_numero
        return '->'.join(nodes)

Mapa = lista_encadeada()
Mapa.adicionar(1)
Mapa.adicionar(2)
Mapa.adicionar(3)
Mapa.adicionar(4)
Mapa.adicionar(5)
Mapa.puxar()
print(Mapa)