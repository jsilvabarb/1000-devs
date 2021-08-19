#Calculadora simples

sinal=input("Informe o sinal para o cálculo da tabuada:")
numero=int(input("Informe o número para o cálculo da tabuada:"))

cont= 0
print("A tabuada do", sinal,"para o número:", numero)

if(sinal == "+"):
    while cont <= 9:
        soma= numero + cont
        print(numero," + ", cont, "= ",soma)
        cont += 1
        
cont = 0

if(sinal == "-"):
     while cont <= 9:
        sub = abs(numero- cont)
        print(numero," - ", cont, "= ",sub)
        cont += 1
        
cont = 0
 
if(sinal == "*"):
     while cont <= 9:
        mult= numero * cont
        print(numero," * ", cont, "= ",mult)
        cont += 1
        
cont = 0

if(sinal == "/"):
    while cont <= 9:
        if cont == 0:
            print(numero," / ", cont,"= Divisão por 0 não existe")
        else:
            div= float(numero / cont)
            print(numero," / ", cont,"= %.2f" % round(div,2))
        cont += 1   
  




