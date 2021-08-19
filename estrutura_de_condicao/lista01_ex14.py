# Exercicio 14
print("Informa quantos dias se passaram desde o início do ano")

diaFinal= int(input("Digite o dia final:"))
mesFinal= int(input("Digite o mês final"))
qtdDias = 0
cont = 1

# Validando dias do mês e quantidade de meses no ano
if((mesFinal < 1 or mesFinal > 12) or(diaFinal < 1 or diaFinal > 31) or (mesFinal == 2 and diaFinal <=29)):
    print("Impossível calcular dias, mes/dia inválido")
else:
    while cont <= mesFinal:
        if (cont == mesFinal):
            qtdDias = qtdDias + diaFinal
        elif(cont == 1 or cont == 3 or cont == 5 or cont == 7 or cont == 8 or cont == 10 or cont == 12):
            qtdDias = qtdDias + 31
        elif(cont == 2):
            qtdDias = qtdDias + 28
        else:
            qtdDias = qtdDias + 30
        cont += 1
        
    print("Quantidade de dias:", qtdDias)  
