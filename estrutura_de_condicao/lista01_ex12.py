# Exercício 12 lista 1

print("----------Calcula a quantidade de litros necessário para fazer um refresco--------")

qtdLitros = float(input("Digite a quantidade de litros necessária:"))
concentracaoAgua = float(input("Digite o percentual de concentração da água:"))
concentracaoSuco = float(input("Digite o percentual de concentração do suco:"))

totalConcentracao = concentracaoAgua + concentracaoSuco
controle = 1

# Validando o total de concentração
if(totalConcentracao < 100):
    print("As concentrações não totalizam 100%")
    resposta=input("Deseja enquadrar os valores em escala de 100%[s|n]?")
    
    if(resposta == 's') :
        # Enquadrando o valor de água lido:
        concentracaoEqAgua = concentracaoAgua/ ( concentracaoAgua + concentracaoSuco)
        concentracaoEqSuco = concentracaoSuco/ ( concentracaoAgua + concentracaoSuco)
        
        print("Novo percentual da água: %.2f"%round(concentracaoEqAgua, 2))
        print("Novo percentual do suco: %.2f"%round(concentracaoEqSuco, 2))
        
        qtdAgua = concentracaoEqAgua * qtdLitros
        qtdSuco = concentracaoEqSuco * qtdLitros
        
    else:
        controle = -1
        print("Valores de concentracao incorretos. Processo finalizado!")
else:
    qtdAgua = (concentracaoAgua/100) * qtdLitros
    qtdSuco = (concentracaoSuco/100) * qtdLitros
    
#fazendo o controle da saída   
if(controle == 1) :
    print("A quantidade de água necessária para fazer %.2f"%round(qtdLitros, 2), " de suco é: %.2f"%round(qtdAgua, 2))
    print("A quantidade de suco concentrado de maracujá é: %.2f"%round(qtdSuco))