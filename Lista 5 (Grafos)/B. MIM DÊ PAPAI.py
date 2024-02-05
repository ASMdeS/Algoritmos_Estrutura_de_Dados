# Crição da classe Grafo, com os vértices e arestas, além da função que checará se o caminho é possível
class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.arestas = {}
        for sala, chave in self.vertices:
            if sala in self.arestas:
                self.arestas[sala].append(chave)
            else:
                self.arestas[sala] = [chave]


entrada = (input().split())
numero_usuarios = int(entrada[0])
conexoes_usuarios = int(entrada[1])

lista_conexoes = []

for i in range(0, conexoes_usuarios):
    entrada = input()
    lista_chaves = entrada.split()
    lista_conexoes.append((lista_chaves[0], lista_chaves[1]))

# Criando o grafo
grafo_caminhos = Grafo(lista_conexoes)
