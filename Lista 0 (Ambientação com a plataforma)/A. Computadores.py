# Importando a biblioteca math
import math


# Definindo a função de calcular a velocidade
def calcular_velocidade(quantidade, capacidade, complexidade):
    if complexidade == "2n^2":
        return (2 * (quantidade ** 2)) / capacidade
    elif complexidade == "n.logn":
        return (quantidade * math.log10(quantidade)) / capacidade
    if complexidade == "2^n":
        return (2 ** quantidade) / capacidade
    if complexidade == "n":
        return quantidade / capacidade


# Recebendo a quantidade de instrucoes
quantidade_instrucoes = int(input())

# Recebendo as informações do primeiro computador
primeiro_computador = input().split(" - ")
primeiro_nome = primeiro_computador[0]
primeiro_capacidade = int(primeiro_computador[1])
primeiro_algoritmo = primeiro_computador[2]
primeiro_complexidade = primeiro_computador[3]
primeiro_velocidade = calcular_velocidade(quantidade_instrucoes, primeiro_capacidade, primeiro_complexidade)
print(f'Velocidade do {primeiro_nome}: {primeiro_velocidade:.2f} segundos')

# Recebendo as informações do segundo computador
segundo_computador = input().split(" - ")
segundo_nome = segundo_computador[0]
segundo_capacidade = int(segundo_computador[1])
segundo_algoritmo = segundo_computador[2]
segundo_complexidade = segundo_computador[3]
segundo_velocidade = calcular_velocidade(quantidade_instrucoes, segundo_capacidade, segundo_complexidade)
print(f'Velocidade do {segundo_nome}: {segundo_velocidade:.2f} segundos')

# Checando qual o mais rápido
if primeiro_velocidade < segundo_velocidade:
    print(f'O {primeiro_nome} foi mais rápido!')
else:
    print(f'O {segundo_nome} foi mais rápido!')
