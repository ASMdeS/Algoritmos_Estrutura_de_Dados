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
        print(f"Node {numero} adicionado")

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
            print(f"Node {numero} empurrado")
        else:
            while current:
                if current.numero == node_empurrado.numero:
                    if current.numero == next.numero:
                        print(f"Não existe Node depois de {current.numero}")
                        break
                    if last:
                        if next.numero == last.numero:
                            last = None
                    previous.proximo_numero = next
                    next.proximo_numero = current
                    current.proximo_numero = last
                    print(f"Node {numero} empurrado")
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
        current = self.head
        previous = None
        next = None
        first = None
        if self.head is None:
            print(f"Node {numero} não existe")
        elif current.numero == node_empurrado.numero:
            print(f"Não existe node antes de {current.numero}")
        else:
            while current:
                if current.numero == node_empurrado.numero:
                    print(current.numero)
                    print(previous.numero)
                    print(next.numero)
                    if previous == self.head:
                        current = previous
                        previous = previous.proximo_numero
                        if current.proximo_numero:
                            current.proximo_numero = next
                    else:
                        if first and first.proximo_numero:
                            first.proximo_numero = current
                        current = previous
                        current.proximo_numero = next
                        if first and first.proximo_numero:
                            previous = first.proximo_numero
                        previous.proximo_numero = current
                        current.proximo_numero = next
                        print(f"Node {numero} puxado")
                        break
                else:
                    if previous:
                        first = previous
                        first.proximo_numero = previous
                    previous = current
                    current = current.proximo_numero
                    if current.proximo_numero:
                        next = current.proximo_numero

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

    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("mapa:%s" % current.numero)
            else:
                nodes.append("%s" % current.numero)
            current = current.proximo_numero
        return '->'.join(nodes)


Mapa = lista_encadeada()
entrada = None
entrada = None

#while entrada != "fim!":
    #entrada = input()
    #if entrada != "fim!":
        #lista_entrada = entrada.split(":")
        #numero = lista_entrada[0]
        #instrucao = lista_entrada[1]

        #if instrucao == "adicione-me!":
          #  Mapa.adicionar(numero)
        #elif instrucao == "remova-me!":
           # Mapa.remover(numero)
      #  elif instrucao == "empurre-me!":
       #     Mapa.empurrar(numero)
        #elif instrucao == "puxe-me!":
         #   Mapa.puxar(numero)
    #else:
     #   print(Mapa)

Mapa.adicionar(1)
Mapa.adicionar(2)
Mapa.adicionar(3)
Mapa.adicionar(4)
Mapa.adicionar(5)
Mapa.puxar(2)
print(Mapa)