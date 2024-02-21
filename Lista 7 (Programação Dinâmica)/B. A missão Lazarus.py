# Criando a classe VisitandoPlanetas e definindo a função de descobrir possibilidades
class VisitandoPlanetas:
    def __init__(self, lista_visitacao):
        self.lista_visitacao = lista_visitacao

    def todas_possibilidades(self):
        lista_visitados = [[]]
        for elemento in self.lista_visitacao:
            combinacoes_atuais = []
            for componente in lista_visitados:
                combinacoes_atuais.append(componente + [elemento])
            lista_visitados.extend(combinacoes_atuais)
        return lista_visitados


# Recebendo os planetas a serem visitados
entrada_usuario = input()

if entrada_usuario != ' ':
    planetas_visitacao = sorted(entrada_usuario.split(", "))
else:
    planetas_visitacao = []

# Criando o VisitandoPlanetas
planetas_visitacao = VisitandoPlanetas(planetas_visitacao)

# Pegando a lista com PossibilityU
lista_final = planetas_visitacao.todas_possibilidades()

# Imprimindo o número de possibilidades
print(f"O número de subsets de visitação é {len(lista_final)}")

# Imprimindo a lista com todas as possibilidades
print(f"São eles: {sorted(lista_final)}")
