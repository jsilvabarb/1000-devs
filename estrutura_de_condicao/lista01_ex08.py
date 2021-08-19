#Exercício 08 lista 1

print("-----------------Computa os descontos do INSS +FGTS+IR de um salario aumentado em 5%--------------------")
salario=float(input("Informe seu salário:"))

salarioAumento= salario + (salario * 0.05)

inss=salarioAumento * 0.11
fgts=salarioAumento * 0.08

salarioReajustado= salarioAumento - (inss + fgts)

if(salarioAumento <= 1903.98):
    #0%
    pct = 0
    taxaIrenda = 0
    salarioFinal = salarioReajustado - taxaIrenda
elif(salarioAumento >= 1903.99 and salarioAumento<= 2826.65):
    # 7.5 Desconto ir
    pct = 7.5
    taxaIrenda = 0.075 * salarioAumento
    salarioFinal = salarioReajustado - taxaIrenda
elif(salarioAumento >= 2826.66 and salarioAumento <= 3751.05):
    # 15% desconto ir
    pct = 15
    taxaIrenda = 0.15 * salarioAumento
    salarioFinal = salarioReajustado - taxaIrenda


print("Salário Inicial: R$ %.2f"% round(salario, 2))
print("Salário Rajustado: R$ %.2f"% round(salarioAumento, 2))
print("Desconto 11%% INSS: R$ %.2f"% round(inss, 2))
print("Desconto 8%% FGTS: R$ %.2f"% round(fgts, 2))
print("Desconto %.2f%%"%round(pct,1), "Imposto de Renda: R$ %.2f"% round(taxaIrenda, 2))
print("Total de descontos INSS+FGT+IR: %.2f"% round((inss+fgts+taxaIrenda), 2))
print("Salário Final: R$ %.2f"% round(salarioFinal, 2))

if(salarioFinal < salario) :
    print("O novo salario final é menor do que o salario recebido antes do aumento!")


