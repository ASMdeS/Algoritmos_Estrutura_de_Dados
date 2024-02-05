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
primeira_entrada = input().split()
numero_salas = int(primeira_entrada[0])

# Criando a lista de caminhos
caminhos = []

# Pegando as entradas e adicionando ao Grafo
for i in range(numero_salas - 1):
    entrada = input()
    entrada_modificada = entrada.replace("Bairro ", "").replace(":", ",")
    entrada_final = entrada_modificada.split(", ")
    for elemento in entrada_final[1:]:
        caminhos.append((entrada_final[0], elemento))

# Criando o grafo
grafo_caminhos = Grafo(caminhos)

# Imprimindo da forma desejada conforme a resposta da função checar possibilidades
for i in range(1, numero_salas):
    if grafo_caminhos.checar_possibilidades("0", str(i)):
        print(f"Bairro {i}: Pode!")
    else:
        print(f"Bairro {i}: Não pode!")
