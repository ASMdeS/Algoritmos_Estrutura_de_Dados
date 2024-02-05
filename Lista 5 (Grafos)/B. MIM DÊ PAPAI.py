# Criando a Classe Grafo, defnindo-a baseado em vértices e arestas, e calculando o número de conexões por DFS
class Grafo:
    def __init__(self, conexoes, vertices):
        self.conexoes = conexoes
        self.vertices = [str(i) for i in range(1, vertices + 1)]
        self.arestas = {vertice: [] for vertice in self.vertices}
        # Build the dictionary with connections
        for conexao in self.conexoes:
            v1, v2 = conexao
            self.arestas[v1].append(v2)
            self.arestas[v2].append(v1)

    def numero_conexoes(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for neighbor in self.arestas[start]:
            if neighbor not in visited:
                self.numero_conexoes(neighbor, visited)
        return len(visited)


# Recebendo a primeira entrada com N e M e dividindo-a:
primeira_entrada = input().split()

# Criando a lista com todas as conexões entre os vértices
lista_conexoes = []

# Preenchendo a lista com os vértices e suas conexões
for conexao in range(int(primeira_entrada[1])):
    entradas_subsequentes = input().split()
    lista_conexoes.append((entradas_subsequentes[0], entradas_subsequentes[1]))

# Criando o Grafo
grafo_caminhos = Grafo(lista_conexoes, int(primeira_entrada[0]))

# Lista com os valores
lista_numeros = []

# Calculando os valores
for vertice in grafo_caminhos.vertices:
    lista_numeros.append(grafo_caminhos.numero_conexoes(vertice))

# Imprimindo a lista com os valores
print(*lista_numeros)