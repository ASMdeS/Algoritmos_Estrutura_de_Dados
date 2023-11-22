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

        node_empurrado = Node(numero)
        current = self.head
        previous = None
        next = None
        last = None
        if self.head is None:
            print(f"Node {numero} não existe")
        elif current.numero == node_empurrado.numero:
            next = current.proximo_numero
            if next:
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
                        return
                    if last:
                        if next.numero == last.numero:
                            last = None
                    previous.proximo_numero = next
                    next.proximo_numero = current
                    current.proximo_numero = last
                    print(f"Node {numero} empurrado")
                    return
                else:
                    previous = current
                    current = current.proximo_numero
                    if current.proximo_numero:
                        next = current.proximo_numero
                    if next.proximo_numero:
                        last = next.proximo_numero