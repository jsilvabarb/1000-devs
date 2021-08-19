# Exercicio 15 lista 1

print("-------------Informa a quantidade de litros que o comerciante comprou------------------")

qtdLatas= int(input("Digite a quantidade de latas de 350ml:"))
qtdGarrafas600= int(input("Digite a quantidade de garrafas de 600ml:"))
qtdGarrafas2L= int(input("Digite a quantidade de garrafas de 2L:"))

totalLatas = qtdLatas * 0.350


margem600 = float(totalLatas / 0.600)
margem350 = float(totalLatas / 0.350)

qtdLitros = float((qtdLatas * 0.350) + (qtdGarrafas600 * 0.600) + (qtdGarrafas2L * 2))
print("A quantidade de Litros é: %.2f"%round(qtdLitros, 2))
if(margem600 >= margem350):
    print("Considere substituir a compra de:")
    print(qtdLatas, " latas de 350 ml por %.2f"%round(margem600, 2))









