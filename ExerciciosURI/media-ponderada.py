#  Este código tem o objetivo de fazer o cálculo de média ponderada e validação de aprovação do aluno

def calculaMediaPonderada(nota1, nota2, nota3, nota4):
    media = (float) ((nota1 * 2) + (nota2 * 3) + (nota3 * 4) + (nota4 * 1)) / (2 + 3 + 4 + 1)

    return media

# Coletando dados
nota1, nota2, nota3, nota4 = map(float, input("Digite as notas do aluno:").split())

notaExame = 0.0

# Calculando a média ponderada
media = calculaMediaPonderada(nota1, nota2, nota3, nota4)
print("Média: %.1f"%media)

# Validando os casos de aprovação ou não
if (media < 5.0) :
    print("Aluno reprovado.")
elif (media >= 5.0 and media <=6.9):
    print("Aluno em exame.")
    notaExame = float(input("Digite a pontuação do exame: "))

    print("Nota exame: %.1" %media)
    media = (float) (media + notaExame) / 2

    if(media >= 5.0):
        print("Aluno aprovado.")
    else :
        print("Aluno reprovado.")
    
    print("Media Final: %.1f"%media)
elif (media >= 7.0) :
    print("Aluno aprovado.")

















# conta=float(input("Informe o valor da conta:"))

# div = (conta / 3)

# centavos = abs(div - int(div))

# if(centavos <= 0.30):
#     # Os dois primeiros amigos não pagarão os centavos
#     andreCarlos = int(div)
#     felipe = int(div) + (3 * centavos)
#     print("Carlos pagará: R$%.2f"%round(andreCarlos, 2))
#     print("André pagará: R$%.2f"%round(andreCarlos, 2))
#     print("Felipe pagará: R$%.2f"%round(felipe, 2))
# else :
#     # Todos pagarão valores iguais
#     print("Carlos pagará %.2f"%round(div, 2))
#     print("André pagará %.2f"%round(div, 2))
#     print("Felipe pagará %.2f"%round(div, 2))
