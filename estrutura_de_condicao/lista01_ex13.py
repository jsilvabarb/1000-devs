# Exercício 13 lista 1

print("--------Calcula o gasto total da granja para identificar todos os frangos-----------")

qtdFrangos = int(input("Digite a quantidade de frangos:"))
chipAlimentacao = float(input("Digite o valor do chip alimentação:"))
chipIdentidade = float(input("Digite o valor do chip identificação:"))

diferencaValor = abs(chipAlimentacao - chipIdentidade)
maior = 0

print(diferencaValor)

if(chipIdentidade > chipAlimentacao):
    
    if( diferencaValor <= (0.20 * chipIdentidade)):
        totalChipIdentidade = chipIdentidade * qtdFrangos
        aumento = qtdFrangos* 0.20
        qtdFrangosAjustada = qtdFrangos + aumento
        totalChipAlimentacao = (qtdFrangosAjustada * chipAlimentacao) * 2
        
        print("Os chips de alimentação sofreram um aumento de 20% :",qtdFrangosAjustada)
    else:
        totalChipAlimentacao = (qtdFrangos * chipAlimentacao) * 2
        totalChipIdentidade = qtdFrangos * chipIdentidade
        
else:
    if( diferencaValor <= (0.20 * chipAlimentacao)):
        aumento = qtdFrangos* 0.20
        qtdFrangosAjustada = qtdFrangos + aumento
        totalChipIdentidade = (chipIdentidade * qtdFrangosAjustada) 
        totalChipAlimentacao = (qtdFrangos * chipAlimentacao) * 2
        
        print("Os chips de identificação sofreram um aumento de 20% :",qtdFrangosAjustada)
    else:
        totalChipAlimentacao = (qtdFrangos * chipAlimentacao) * 2
        totalChipIdentidade = qtdFrangos * chipIdentidade
    
print("O valor total para identificar os frangos é:")
print("Chip alimentação: R$ %.2f"%round(totalChipAlimentacao, 2))
print("Chip identificação: R$ %.2f"%round(totalChipIdentidade, 2))
print("Valor total: R$ %.2f"%round((totalChipIdentidade + totalChipAlimentacao), 2))










