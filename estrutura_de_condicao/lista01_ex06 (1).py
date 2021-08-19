#Façaumalgoritmoparacalcularquantasferradurassãonecessáriasparaequi
#partodososcavaloscompradosparaumharas.Ousuáriodeverainformaraquantidadedecavalosadquiridos.

print("-----------------Valor total de ferraduras em R$---------------")

qtdCavalos=int(input("Informe a quantidade de cavalos:"))
valorFerradura=float(input("Informe o valor da ferradura R$:"))

qtdFerraduras = qtdCavalos * 4
totalFerraduras = qtdFerraduras * valorFerradura

if(totalFerraduras > 15000.01 and totalFerraduras <=20000.00 ):
    # Desconto de 10%
    taxaDesconto = totalFerraduras * 0.10
    totalFerraduras = totalFerraduras - taxaDesconto
elif(totalFerraduras >=20000.01 and totalFerraduras <=25000.00):
    # Desconto 12%
    taxaDesconto = totalFerraduras * 0.12
    totalFerraduras = totalFerraduras - taxaDesconto
elif(totalFerraduras >= 25000.01 and totalFerraduras <=30000.00):
    # Desconto 15%
    taxaDesconto = totalFerraduras * 0.15
    totalFerraduras = totalFerraduras - taxaDesconto
elif(totalFerraduras >= 30000.01):
    # Desconto 20%
    taxaDesconto = totalFerraduras * 0.20
    totalFerraduras = totalFerraduras - taxaDesconto

print("A quantidade de ferraduras necessárias é:", qtdFerraduras)
print("O valor total para a compra das ferraduras: R$ %.2f"% round(totalFerraduras,2))


