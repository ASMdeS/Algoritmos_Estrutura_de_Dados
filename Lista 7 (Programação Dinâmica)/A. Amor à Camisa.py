# Criando a classe Soma e definindo a função de calcular a máxima soma
class Soma:
    def __init__(self, lista_numeros):
        self.lista_numeros = lista_numeros

    def calcular_soma(self):
        maior_soma = [0] * len(self.lista_numeros)
        maior_soma[0] = self.lista_numeros[0]
        maior_soma[1] = max(self.lista_numeros[0], self.lista_numeros[1])

        for i in range(2, len(self.lista_numeros)):
            maior_soma[i] = max(maior_soma[i - 1], maior_soma[i - 2] + self.lista_numeros[i])

        return maior_soma[-1]

# Recebendo o número de setores
numero_setores = int(input())

# Recebendo a quantidade de torcedores por setor
torcedores_setor = input().split()

# Transformando em uma lista de integers
numero_torcedores = [int(x) for x in torcedores_setor]

# Criando a Soma
soma_torcedores = Soma(numero_torcedores)

# Imprimindo como desejado
print(f'{soma_torcedores.calcular_soma()} torcedores podem ser fotografados.')