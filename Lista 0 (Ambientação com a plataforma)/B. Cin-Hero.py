class Animal:
    def __init__(self):
        self.listaAnimais = []

    def cadastro(self, local, raca, data):
        self.listaAnimais.append((local, raca, data))

    def imprimeRelatorio(self):
        for animal in self.listaAnimais:
            print(f"Local: {animal[0]}\nRaça: {animal[1]}\nData: {animal[2]}\n")

    def dataInteresse(self, data):
        diaI, mesI, anoI = data.split("/")

        for animal in self.listaAnimais:
            dia, mes, ano = animal[2].split("/")

            if int(ano) > int(anoI):
                print("Local encontrado:", animal[0], "- Raça:", animal[1], "- Data:", animal[2])
                print()

            elif int(ano) == int(anoI) and int(mes) > int(mesI):
                print("Local encontrado:", animal[0], "- Raça:", animal[1], "- Data:", animal[2])
                print()

            elif int(ano) == int(anoI) and int(mes) == int(mesI) and int(dia) > int(diaI):
                print("Local encontrado:", animal[0], "- Raça:", animal[1], "- Data:", animal[2])
                print()

    def removerAnimal(self, raca, data):
        for animal in self.listaAnimais:
            if animal[1] == raca and animal[2] == data:
                self.listaAnimais.remove(animal)


sistema = Animal()
entrada = None

while entrada != "5":
    entrada = input()
    if entrada == "1":
        registros = input().split()
        sistema.cadastro(registros[0], registros[1], registros[2])
    elif entrada == "2":
        sistema.imprimeRelatorio()
    elif entrada == "3":
        data = input()
        sistema.dataInteresse(data)
    elif entrada == "4":
        remover = input().split()
        sistema.removerAnimal(remover[0], remover[1])
