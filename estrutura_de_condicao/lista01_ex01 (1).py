#Umaimobiliáriavendeapenasterrenosretangulares.Façaumalgoritmoparaimprimiraáreadoterrenoeovalordevendadomesmo.
#Paraistoseránecessárioousuárioinformarasdimensõesemmetros(frenteelateral)
#doterrenoalémdovalorcobradopelometroquadrado.

frente=float(input("Quantos metros o terreno possui de frente:"))
lado=float(input("Quantos metros o terreno possui de lado:"))
valorMetroQuadrado=float(input("Informe o valor do metro²:"))

areaTerreno= frente * lado
diferencaMetragem = abs(frente - lado)
valorInicial=areaTerreno*valorMetroQuadrado
valorFinal=areaTerreno*valorMetroQuadrado
aux = 1

print("A area total do terreno de %.2f m de frente"%round(frente), "e %.2f m de lado \n"%round(lado), "é: %.2f\n"% round(areaTerreno))
#Caso a diferença de metragem entre a frente e a lateral seja menor que 10% da
#metragem da frente, o cliente terá um acréscimo de 22% no valor final do terreno.
if (diferencaMetragem < (0.1 * frente)):
    taxaAcrescimo =  valorInicial * 0.22
    valorFinal = valorFinal + taxaAcrescimo
    aux = -1
    print("O terreno sofreu um acréscimo de 22%% e custará: %.2f"% round (valorFinal))
    
#Caso a metragem da frente for menor que 40% da lateral, o cliente terá um desconto de 12% no
#valor final do terreno    
if (frente < (0.4 * lado)):
    taxaDesconto = valorFinal * 0.12
    valorFinal = valorFinal - taxaDesconto
    aux = -1
    
    print("O terreno sofreu um desconto de 12%% e custará: %.2f"% round (valorFinal))
    
# Caso a metragem da frente for maior que 70% da lateral, o cliente terá um
#desconto de 15%   
if (frente > (0.70 * lado)):
    taxaDesconto = valorFinal * 0.15
    valorFinal = valorFinal - taxaDesconto
    aux = -1
    
    print("O terreno sofreu um desconto de 15%% e custará: %.2f"% round (valorFinal))

if(aux == 1):
    print("O terreno não recebeu nenhuma alteração e custara: %.2f"%round(valorFinal))
    

