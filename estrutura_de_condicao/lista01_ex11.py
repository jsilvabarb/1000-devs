# Exercício 11 lista 01

print("---------Calcula a idade do Usuário em anos, meses e dias--------------")

mesNascimento = int(input("Digite o mês do seu nascimento:"))
anoNascimento = int(input("Digite o ano do seu nascimento:"))

mesAtual = int(input("Digite o mês atual:"))
anoAtual = int(input("Digite o ano atual"))

idadeAnos = 0
idadeMeses = 0
idadeDias = 0
aux = mesNascimento
cont = 0 

# Validando dados de Entrada 
if((mesNascimento < 1 or mesNascimento > 12) or (mesAtual < 1 or mesAtual > 12) or (anoAtual < anoNascimento)):
    print("Impossível calcular idade, mes/anos inválido")
else:
    if (anoNascimento == anoAtual) :
        if(mesAtual == mesNascimento):
            idadeMeses = 1
        elif(mesAtual < mesNascimento):
            print("Impossível calcular idade, mes/anos inválido")
        else:
            idadeMeses = mesAtual - mesNascimento
    else:
        if( mesAtual == mesNascimento):
            idadeAnos = anoAtual - anoNascimento
            idadeMeses = idadeAnos * 12
        
        elif(mesAtual > mesNascimento) :
            idadeAnos = anoAtual - anoNascimento
            idadeMeses = (idadeAnos * 12) + (mesAtual)
            
        elif(mesAtual < mesNascimento):
            idadeAnos = (anoAtual - anoNascimento) - 1
            if(idadeAnos == 0):
                idadeMeses = (12 - mesNascimento) + mesAtual #somando +1 daria o valor do exemplo mas o Usuário teria 10 meses e não 9
                print(cont)
            else:
                idadeMeses = (idadeAnos * 12) + mesAtual
    while cont < idadeMeses :
        if(aux == 1 or aux == 3 or aux == 5 or aux == 7 or aux == 8 or aux == 10 or aux == 12):
            idadeDias = idadeDias + 31
        elif(aux == 2):
            idadeDias = idadeDias + 28
        else:
            idadeDias = idadeDias + 30
        aux += 1
        
        print(cont)
        
        if(aux == 13):
            aux = 1
        cont += 1
    print("Idade anos:", idadeAnos)
    print("Idade meses:", idadeMeses)
    print("Idade Dias:", idadeDias)

