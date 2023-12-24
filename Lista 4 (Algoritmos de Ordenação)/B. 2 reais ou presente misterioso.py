# Definindo o método insertion_sort
def insertion_sort(arranjo):
    for i in range(1, len(arranjo)):
        chave = arranjo[i]
        j = i - 1
        while j >= 0 and chave < arranjo[j]:
            arranjo[j + 1] = arranjo[j]
            j -= 1
        arranjo[j + 1] = chave


# Definindo o método quick_sort
def quick_sort(arranjo):
    if len(arranjo) <= 1:
        return arranjo
    else:
        pivo = arranjo[0]
        esquerda = [x for x in arranjo[1:] if x <= pivo]
        direita = [x for x in arranjo[1:] if x > pivo]
        return quick_sort(esquerda) + [pivo] + quick_sort(direita)


# Definindo o método merge_sort
def merge_sort(arranjo):
    if len(arranjo) > 1:
        meio = len(arranjo) // 2
        esquerda = arranjo[:meio]
        direita = arranjo[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arranjo[k] = esquerda[i]
                i += 1
            else:
                arranjo[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            arranjo[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            arranjo[k] = direita[j]
            j += 1
            k += 1


# Definindo o método shell_sort
def shell_sort(arranjo):
    tamanho = len(arranjo)
    diferenca = tamanho // 2

    while diferenca > 0:
        for i in range(diferenca, tamanho):
            tempo = arranjo[i]
            j = i
            while j >= diferenca and arranjo[j - diferenca] > tempo:
                arranjo[j] = arranjo[j - diferenca]
                j -= diferenca
            arranjo[j] = tempo
        diferenca //= 2


# Definindo o método selection_sort
def selection_sort(arranjo):
    for i in range(len(arranjo)):
        indice_minimo = i
        for j in range(i + 1, len(arranjo)):
            if arranjo[j] < arranjo[indice_minimo]:
                indice_minimo = j
        arranjo[i], arranjo[indice_minimo] = arranjo[indice_minimo], arranjo[i]


# Definindo como ordenar e dobrar os elementos caso necessário
def ordenar_dobrar(lista_presentes, metodo_ordenacao, dobrar):
    if metodo_ordenacao == "Insertion Sort":
        insertion_sort(lista_presentes)
    elif metodo_ordenacao == "Quick Sort":
        lista_presentes = quick_sort(lista_presentes)
    elif metodo_ordenacao == "Merge Sort":
        merge_sort(lista_presentes)
    elif metodo_ordenacao == "Shell Sort":
        shell_sort(lista_presentes)
    elif metodo_ordenacao == "Selection Sort":
        selection_sort(lista_presentes)

    if dobrar:
        lista_presentes = [2 * presente for presente in lista_presentes]

    return lista_presentes


# Recebendo a lista com os presentes
entrada_presentes = list(map(int, input().split(", ")))

# Recebendo o método que deverá ser utilizado
entrada_metodo = input()

# Descobrindo se o presente virá dobrado ou não
if input() == "não dobre!":
    dobrado = False
else:
    dobrado = True

# Ordenando (e dobrando) os presentes
print(ordenar_dobrar(entrada_presentes, entrada_metodo, dobrado))
