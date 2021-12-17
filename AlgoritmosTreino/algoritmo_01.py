# Construa um algoritmo que calcule e apresente quanto deve ser pago por um produto considerando a leitura do preço de etiqueta (PE) e o código da condição de pagamento (CP).

def aplicaDesconto(precoEtiqueta, percentual) :

    taxaDesconto = precoEtiqueta * float(percentual/100)
    precoEtiqueta = precoEtiqueta - taxaDesconto

    return precoEtiqueta

def aplicaAcrescimo(precoEtiqueta, percentual) :
    acrescimo = precoEtiqueta * float(percentual/100)
    precoEtiqueta = precoEtiqueta + acrescimo

    return precoEtiqueta
precoEtiqueta=float(input("Digite o preço de etiqueta do produto: "))

print("Opções de Pagamento\n")
print("1 - À vista em dinheiro ou cheque, com 10%% de desconto\n")
print("2 - À vista com cartão de crédito, com 5%% de desconto\n")
print("3 - Em 2 vezes, preço normal de etiqueta sem juros\n")
print("4 - Em 3 vezes, preço de etiqueta com acréscimo de 10%% \n")

codigoOpcao=int(input("Digite o código da condição: "))

if(codigoOpcao == 1) :
   print("Novo valor do produto: R$%.1f"%aplicaDesconto(precoEtiqueta, 10))
elif (codigoOpcao == 2) :
      print("Novo valor do produto: R$%.1f"%aplicaDesconto(precoEtiqueta, 5))
elif (codigoOpcao == 3) :
      print("Dividindo em 2X o valor é: R$%.1f"%aplicaAcrescimo(precoEtiqueta, 0))
elif (codigoOpcao == 4) :
      print("Dividindo em 3X o valor é: R$%.1f"%aplicaAcrescimo(precoEtiqueta, 10))

    

