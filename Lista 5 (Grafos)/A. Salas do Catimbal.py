# Criando a classe Grafo, formada por um dicionário, contendo a função que checará se é possível chegar ao Tesouro
class Grafo:
    def __init__(self, dicionario):
        self.dicionario = dicionario

    def checar_possibilidade(self, sala, chave, caminho=[]):
        caminho = caminho + [sala]
        if sala == chave:
            return [caminho]
        if sala not in self.dicionario:
            return []

        lista_caminhos = []

        for elemento in self.dicionario[sala]:
            if elemento not in caminho:
                novos_caminhos = self.checar_possibilidade(elemento, chave, caminho)
                for caminho in novos_caminhos:
                    lista_caminhos.append(caminho)

        return lista_caminhos


# Criando o Dicionário
dicionario_grafos = {}

# Criando o que será usado como entrada
entrada = None

# Atribuindo o número de salas
numero_salas = 0

# Pegando as entradas e adicionando ao Dicionário no formado [sala] = lista de chaves
while entrada != "Tesouro":
    numero_salas += 1
    entrada = input()
    lista_chaves = entrada.split()
    dicionario_grafos[str(numero_salas)] = lista_chaves

# Definindo a sala inicial
Sala = "1"

# Definindo a chave que queremos pegar
Chave = "Tesouro"

# Criando o grafo
grafo_caminhos = Grafo(dicionario_grafos)

# Checando se foi formado um caminho
grafo_caminhos.checar_possibilidade(Sala, Chave)
