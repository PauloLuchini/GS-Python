qtd_desastres = int(input("Informe a quantidade de desastres registrados: "))

cont = 0

while cont < qtd_desastres:
    
        tipo_desastre = input("Qual o tipo de desastre? ")
        pais = input("Qual o país onde ocorreu o desastre? ")
        cidade = input("Em qual cidade foi o desastre? ")
        bairro = input("Em qual bairro foi o desastre? ")
        rua = input("Informe a Rua onde ocorreu o desastre: ")
        qtd_pessoas_afetadas = int(input("Informe a quantidade de pessoas afetadas: "))
        qtd_crianca = int(input("Quantas crianças foram afetadas? "))
        qtd_adulto = int(input("Quantos adultos foram afetados? "))
        qtd_idosos = int(input("Quantos idosos foram afetados? "))
        qtd_pessoas_mobilidade = int(input("Quantas pessoas com mobilidade reduzida foram afetadas? "))
        qtd_feridos = int(input("Quantos feridos? "))
        
        qtd_pessoas_categoria = qtd_crianca + qtd_adulto + qtd_idosos + qtd_pessoas_mobilidade + qtd_feridos

        if qtd_pessoas_afetadas != qtd_pessoas_categoria:
            print("A soma das categorias deve ser igual ao número total de pessoas afetadas. Tente novamente!")
            break
        cont += 1

