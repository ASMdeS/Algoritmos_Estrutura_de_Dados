# Criando a classe TabelaHash e definindo a função de hash, como inserir elementos e como imprimir a tabela
class TabelaHash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def funcao_hash(self, value):
        return value % self.size

    def inserir(self, key, value):
        indice = self.funcao_hash(value)

        if self.table[indice] is None:
            self.table[indice] = [(key, value)]
        else:
            while self.table[indice]:
                indice = (indice + 1) % self.size
            self.table[indice] = [(key, value)]

    def imprimir_tabela(self):
        lista_impressao = []
        for i, bucket in enumerate(self.table):
            if bucket is not None:
                for key, value in bucket:
                    lista_impressao.append(key)
            else:
                lista_impressao.append('vago')
        print(lista_impressao)


# Criando a tabela de hash:
hash_table = TabelaHash(size=10)

# Definindo a função de criar os grupos
def criar_grupos(s):
    grupos = []
    estudantes_vistos = set()

    for student in s:
        if student not in estudantes_vistos:
            estudantes_vistos.add(student)
            grupos.append(student)
        else:
            yield grupos, sum(ord(char) for char in grupos)
            grupos = [student]
            estudantes_vistos = {student}

    yield grupos, sum(ord(char) for char in grupos)


# Criando os grupos baseados na input:
grupos_finais = list(criar_grupos(input()))

# Inserindo cada grupo na tabela hash
for element in grupos_finais:
    hash_table.inserir(element[0], element[1])

# Imprimindo a tabela hash
hash_table.imprimir_tabela()
