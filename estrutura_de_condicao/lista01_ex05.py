#Exercicio 5 lista 01
print("-------------Este programa tem o objetivo de dividir o maior número pelo menor--------------|\n")
numero1=int(input("Informe o valor 1:"))
numero2=int(input("Informe o valor 2:"))

maior = 0
menor = 0

if(numero1 > maior):
    maior = numero1
    menor = numero2
    
if(numero2 > maior):
    maior = numero2
    menor = numero1
    
if menor == 0:
    print("Divisão por zero não existe.")
else:
    div = maior / float(menor)
    print("A divisão de ", maior, " por ", menor, " é igual a: %.2f" % round(div,2))
    
