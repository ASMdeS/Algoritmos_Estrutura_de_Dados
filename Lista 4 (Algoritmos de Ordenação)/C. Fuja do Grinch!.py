# Definindo a função heapify
def heapify(arranjo, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and arranjo[esquerda] > arranjo[maior]:
        maior = esquerda

    if direita < n and arranjo[direita] > arranjo[maior]:
        maior = direita

    if maior != i:
        arranjo[i], arranjo[maior] = arranjo[maior], arranjo[i]
        heapify(arranjo, n, maior)


# Definindo o heapSort
def heapSort(arranjo):
    tamanho = len(arranjo)

    for i in range(tamanho // 2 - 1, -1, -1):
        heapify(arranjo, tamanho, i)

    for i in range(tamanho - 1, 0, -1):
        arranjo[i], arranjo[0] = arranjo[0], arranjo[i]
        heapify(arranjo, i, 0)


# Recebendo as idades e transformando em uma lista de integers
lista_idades = list(map(int, input().split()))

# O primeiro termo da lista de idades é quem leu primeiro
primeiro_leitor = lista_idades[0]

# Ordenando a lista pelo método heapSort e imprimindo o heapMaximo
heapSort(lista_idades)

# Imprimindo conforme foi pedido
print(
    f'Atenção, Grinch está indo atrás do cidadão de {lista_idades[-1]} anos, e logo após isso ele vai atrás do cidadão de {primeiro_leitor} anos.')
