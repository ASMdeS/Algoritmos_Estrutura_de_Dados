entrada = input().split("-")
lista_nomes = ["endrick", "neymar", "cr7", "messi"]
lista_marcas = ["new balance", "puma", "nike", "adidas"]
lista_final = []
tem_problemas = False

for item in entrada:
    if item in lista_nomes:
        if item not in lista_final:
            lista_final.append(item)
        else:
            tem_problemas = True
    elif item in lista_marcas:
        if item == "new balance":
            if "endrick" in lista_final:
                numero = lista_final.index("endrick") + 1
                lista_final.insert(numero, item)
            else:
                tem_problemas = True
                break
        elif item == "puma":
            if "neymar" in lista_final:
                numero = lista_final.index("neymar") + 1
                lista_final.insert(numero, item)
            else:
                tem_problemas = True
                break
        elif item == "nike":
            if "cr7" in lista_final:
                numero = lista_final.index("cr7") + 1
                lista_final.insert(numero, item)
            else:
                tem_problemas = True
                break
        elif item == "adidas":
            if "messi" in lista_final:
                numero = lista_final.index("messi") + 1
                lista_final.insert(numero, item)
            else:
                tem_problemas = True
                break
    else:
        tem_problemas = True
        break

nomes_comuns = set(lista_nomes) & set(lista_final)
marcas_comuns = set(lista_marcas) & set(lista_final)
if len(nomes_comuns) == len(marcas_comuns) and not tem_problemas:
    print("Correto")
else:
    print("Incorreto")