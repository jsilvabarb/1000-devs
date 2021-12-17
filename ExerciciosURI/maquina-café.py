# Este código tem o objetivo de prever quanto tempo será gasto para os funcionários buscarem café com a máquina no melhor posicionamento possível

a1 = int(input("Quantidade de pessoas do 1º andar:"))
a2 = int(input("Quantidade de pessoas do 2º andar:"))
a3 = int(input("Quantidade de pessoas do 3º andar:"))

# Validando valores 

if((a1 > 0 and a1 < 1000) and (a2 > 0 and a2 < 1000) and (a3 > 0 and a3 < 1000)):

else:
    print("Valores inválidos.") 