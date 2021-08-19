# Exercício 16 lista1

print("-------------Informa um número por MILHARES-CENTENAS-DEZENAS-UNIDADES------------ ")

numero=int(input("Digite um número de até 4 dígitos"))
if(numero > 9999 or numero < 1):
    print("Numero invalido!")
else:
    milhares = numero / 1000
    milhares = int(milhares)
    
    resto = numero % 1000
    centenas = resto / 100
    centena = int(centenas)
    
    resto = numero % 100
    dezenas = resto / 10
    dezena = int(dezenas)
    
    resto = numero % 10
    unidades = int(resto/1)
    
    print("MILHARES:",milhares)
    print("CENTENAS:",centena)
    print("DEZENAS:",dezena)
    print("UNIDADES:",unidades)



