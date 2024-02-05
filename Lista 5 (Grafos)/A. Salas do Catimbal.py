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

    def checar_possibilidades(self, sala, chave, caminhos=None):
        if caminhos is None:
            caminhos = set()
        caminhos.add(sala)
        if sala == chave:
            return True
        if sala not in self.arestas:
            return False
        for vizinho in self.arestas[sala]:
            if vizinho not in caminhos:
                if self.checar_possibilidades(vizinho, chave, caminhos):
                    return True
        return False


# Criando o que será usado como entrada
entrada = None

# Atribuindo o número de salas
numero_salas = 0

# Criando a lista de caminhos
caminhos = []

# Pegando as entradas e adicionando ao Grafo
while entrada != "Tesouro":
    numero_salas += 1
    entrada = input()
    lista_chaves = entrada.split()
    for elemento in lista_chaves:
        caminhos.append((str(numero_salas), elemento))

# Sala inicial
Sala = "1"

# Sala final desejada
Chave = "Tesouro"

# Criando o grafo
grafo_caminhos = Grafo(caminhos)

# Imprimindo da forma desejada conforme a resposta da função checar possibilidades
if grafo_caminhos.checar_possibilidades(Sala, Chave):
    print("TESOURO :)")
else:
    print("SEM TESOURO :(")
