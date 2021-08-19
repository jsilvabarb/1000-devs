# Exercício 9 lista 

print("--------Define quantos cada amigo ira pagar de acordo com os centavos da divisao da conta-----------")

conta=float(input("Informe o valor da conta:"))

div = (conta / 3)

centavos = abs(div - int(div))

if(centavos <= 0.30):
    # Os dois primeiros amigos não pagarão os centavos
    andreCarlos = int(div)
    felipe = int(div) + (3 * centavos)
    print("Carlos pagará: R$%.2f"%round(andreCarlos, 2))
    print("André pagará: R$%.2f"%round(andreCarlos, 2))
    print("Felipe pagará: R$%.2f"%round(felipe, 2))
else :
    # Todos pagarão valores iguais
    print("Carlos pagará %.2f"%round(div, 2))
    print("André pagará %.2f"%round(div, 2))
    print("Felipe pagará %.2f"%round(div, 2))

