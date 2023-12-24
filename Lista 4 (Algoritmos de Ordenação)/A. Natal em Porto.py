# Definindo o bubble sort para a lista
def bubble_sort_lista(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


# Definindo o bubble sort para o dicionário
def bubble_sort_dicionario(dicionario):
    n = len(dicionario)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if list(dicionario[j].keys())[0] > list(dicionario[j + 1].keys())[0]:
                dicionario[j], dicionario[j + 1] = dicionario[j + 1], dicionario[j]


# Criando a lista de dicionários
lista_dicionarios = []

# Recebendo o número de praças
numero_pracas = int(input())

# Transformando cada entrada em um dicionário com o número como chave e as crianças ordenadas como valor
for praca in range(0, numero_pracas):
    entrada_usuario = input().split()
    praca = int(entrada_usuario[1][:-1])
    nomes_criancas = entrada_usuario[2:]
    bubble_sort_lista(nomes_criancas)
    dicionario_criancas = {praca: nomes_criancas}
    lista_dicionarios.append(dicionario_criancas)

# Ordenando a lista com os dicionários
bubble_sort_dicionario(lista_dicionarios)

# Imprimindo cada dicionário no formato pedido pela questão
for group in lista_dicionarios:
    for key, names in group.items():
        print(f'Praça {key}: {" ".join(names)}')
