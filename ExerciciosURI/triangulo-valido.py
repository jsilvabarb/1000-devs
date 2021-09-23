# Este código tem o objetivo de validar se os números inseridos pelo usuário formam um triângulo válido ou não

a, b, c =  map(int, input("Digite três valores inteiros:").split()) 

# Verificando se os valores são positivos
if((a > 0) and (b > 0) and (c > 0)):
    # Condições para o triângulo ser válido
    if(a<(b+c)):
        if(b < (a+c)):
            if(c < (a+b)):

                # Verificando se é isóceles
                if((a == b) or (b == c)):
                    # Verificando se é equilátero
                    if((a == b) and (b == c)):
                        print("Equilátero.")
                    else:
                        print("Isóceles.")
                else:
                    print("Escaleno.")
            else:
                print("Inválido.")
        else:
            print("Inválido")
    else:
        print("Inválido.")
else:
    print("Inválido.")

