class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.dicionario = {}
        for sala, chave in self.vertices:
            if sala in self.dicionario:
                self.dicionario[sala].append(chave)
            else:
                self.dicionario[sala] = [chave]
        print(self.dicionario)

    def checar_possibilidade(self, sala, chave, caminho=[]):
        caminho = caminho + [sala]
        if sala == chave:
            return [caminho]
        if sala not in self.dicionario:
            return []

        lista_caminhos = []

        for node in self.dicionario[sala]:
            if node not in caminho:
                novos_caminhos = self.checar_possibilidade(node, chave, caminho)
                for caminho in novos_caminhos:
                    lista_caminhos.append(caminho)

        return lista_caminhos

caminhos = [
    ("1", "4"),
    ("1", "5"),
    ("2", "1"),
    ("3", "10"),
    ("3", "8"),
    ("4", "6"),
    ("5", "2")
]

Sala = "1"
Chave = "6"

grafo_caminhos = Grafo(caminhos)

print(grafo_caminhos.checar_possibilidade(Sala, Chave))

