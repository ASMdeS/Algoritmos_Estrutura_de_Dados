class Mapa:
    def __init__(self):
        self.lista_mapa = []

    def adicione(self, numero):
        if numero not in self.lista_mapa:
            self.lista_mapa.append(numero)
            print(f"Node {numero} adicionado")
        else:
            print(f"Node {numero} já existe")

    def remova(self, numero):
        if numero in self.lista_mapa:
            self.lista_mapa.remove(numero)
            print(f"Node {numero} foi removido")
        else:
            print(f"Node {numero} não existe")

    def empurre(self, numero):
        if numero in self.lista_mapa:
            posicao = self.lista_mapa.index(numero) + 1
            if posicao < len(self.lista_mapa):
                self.lista_mapa.remove(numero)
                self.lista_mapa.insert(posicao, numero)
                print(f"Node {numero} empurrado")
            else:
                print(f"Não existe Node depois de {numero}")
        else:
            print(f"Node {numero} não existe")

    def puxe(self, numero):
        if numero in self.lista_mapa:
            if self.lista_mapa.index(numero) > 0:
                posicao = self.lista_mapa.index(numero) - 1
                self.lista_mapa.remove(numero)
                self.lista_mapa.insert(posicao, numero)
                print(f"Node {numero} puxado")
            else:
                print(f"Não existe node antes de {numero}")
        else:
            print(f"Node {numero} não existe")

    def exibir_mapa(self):
        print("mapa:" + "->".join(map(str, self.lista_mapa)))


def main():
    mapa = Mapa()
    entrada = None

    while entrada != "fim!":
        entrada = input()

        if entrada != "fim!":
            lista_entrada = entrada.split(":")
            numero = lista_entrada[0]
            instrucao = lista_entrada[1]

            if instrucao == "adicione-me!":
                mapa.adicione(numero)
            elif instrucao == "remova-me!":
                mapa.remova(numero)
            elif instrucao == "empurre-me!":
                mapa.empurre(numero)
            elif instrucao == "puxe-me!":
                mapa.puxe(numero)
        else:
            mapa.exibir_mapa()


main()
