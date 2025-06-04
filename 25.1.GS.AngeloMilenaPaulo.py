# Angelo Rabello RM 564338
# Milena Barbosa RM 558913
# Paulo Henrique RM 561477  

qtd_desastres = int(input("Informe a quantidade de desastres registrados: "))

cont = 0
dict_info_desastre = {}
dict_afetados_desastre = {}
dict_desastres = {}
total_crianca = 0 
total_adulto = 0
total_idosos = 0
total_mobilidade = 0 
total_feridos = 0 

while cont < qtd_desastres:

        tipo_desastre = input("Qual o tipo de desastre? ")
        dict_info_desastre['tipo'] = tipo_desastre
        pais = input("Qual o país onde ocorreu o desastre? ")
        dict_info_desastre['pais'] = pais
        cidade = input("Em qual cidade foi o desastre? ")
        dict_info_desastre['cidade'] = cidade
        bairro = input("Em qual bairro foi o desastre? ")
        dict_info_desastre['bairro'] = bairro
        rua = input("Informe a Rua onde ocorreu o desastre: ")
        dict_info_desastre['rua'] = rua
        qtd_pessoas_afetadas = int(input("Informe a quantidade de pessoas afetadas: "))
        dict_info_desastre['Total Afetados'] = qtd_pessoas_afetadas
        

        qtd_crianca = int(input("Quantas crianças foram afetadas? "))
        dict_afetados_desastre['criança'] = qtd_crianca
        qtd_adulto = int(input("Quantos adultos foram afetados? "))
        dict_afetados_desastre['adulto'] = qtd_adulto
        qtd_idosos = int(input("Quantos idosos foram afetados? "))
        dict_afetados_desastre['idosos'] = qtd_idosos
        qtd_pessoas_mobilidade = int(input("Quantas pessoas com mobilidade reduzida foram afetadas? "))
        dict_afetados_desastre['Mobilidade'] = qtd_pessoas_mobilidade
        qtd_feridos = int(input("Quantos feridos? "))
        dict_afetados_desastre['Feridos'] = qtd_feridos

        dict_desastres[cont + 1] = {**dict_info_desastre, **dict_afetados_desastre}

        qtd_pessoas_categoria = qtd_crianca + qtd_adulto + qtd_idosos + qtd_pessoas_mobilidade + qtd_feridos

        if qtd_pessoas_afetadas != qtd_pessoas_categoria:
            print("A soma das categorias deve ser igual ao número total de pessoas afetadas. Tente novamente!")
            break
        cont += 1

for i in range(qtd_desastres):
    total_crianca += dict_desastres[i + 1]['criança']
    total_adulto += dict_desastres[i + 1]['adulto']
    total_idosos += dict_desastres[i + 1]['idosos']
    total_mobilidade += dict_desastres[i + 1]['Mobilidade']
    total_feridos += dict_desastres[i + 1]["Feridos"]

dict_maior = {"crianca":total_crianca,"adulto" : total_adulto,"idosos":total_idosos,"mobilidade":total_mobilidade,"feridos":total_feridos}

total_afetados = total_crianca + total_adulto + total_idosos + total_mobilidade + total_feridos
    
max_afetados = 0
desastre_mais_afetado = None

for i in range(1, qtd_desastres + 1):
    if dict_desastres[i]["Total Afetados"] > max_afetados:
        max_afetados = dict_desastres[i]["Total Afetados"]
        desastre_mais_afetado = i  


if desastre_mais_afetado is not None:
    tipo_desastre_max = dict_desastres[desastre_mais_afetado]['tipo']
    rua_max = dict_desastres[desastre_mais_afetado]['rua']
    bairro_max = dict_desastres[desastre_mais_afetado]['bairro']
    cidade_max = dict_desastres[desastre_mais_afetado]['cidade']
    pais_max = dict_desastres[desastre_mais_afetado]['pais']

print("Relatório dos dados\n")
print(f"Crianças: {total_crianca} | Adultos: {total_adulto}| Idosos: {total_idosos} | Mobilidade Reduzida: {total_mobilidade} | Feridos: {total_feridos}\n")
print(f"Categoria mais afetada: {max(dict_maior)}\n")
print(f"Total geral de pessoas afetadas: {total_afetados}\n")
print(f"\nDesastre com maior número de afetados:\n")
print(f"Tipo: {tipo_desastre_max}")
print(f"Local: {rua_max}, {bairro_max}, {cidade_max}, {pais_max}")

