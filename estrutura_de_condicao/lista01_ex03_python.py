#Façaumalgoritmoparalertrêsnotasdeumalunoemumadisciplinaeimprimirasuamédiaponderada
#(asnotastempesosrespectivosde 1,2 e 3).

nota1=float(input("Informe a nota 1:"))
nota2=float(input("Informe a nota 2:"))
nota3=float(input("Informe a nota 3:"))

notaPeso1 = 1*nota1
notaPeso2 = 2*nota2
notaPeso3 = 3*nota3


mediaPonderada= ( notaPeso1 + notaPeso2 + notaPeso3 )/ 6

print("A média ponderada das notas %.2f"%round(nota1), ", %.2f"%round(nota2), " e %.2f"%round(nota3), "é igual a: %.2f\n"%round(mediaPonderada))

if((notaPeso1 > notaPeso2) and (notaPeso1 > notaPeso3)):
    print("A nota 1( %.2f ) é a maior nota após o cálculo do peso 1"% round(nota1), "(%.2f)"% round(notaPeso1) )
elif((notaPeso2> notaPeso1 ) and (notaPeso2 > notaPeso3)):
    print("A nota 2( %.2f ) é a maior nota após o cálculo do peso 1"% round(nota2), "(%.2f)"% round(notaPeso2) )
elif((notaPeso3> notaPeso1 ) and (notaPeso3 > notaPeso2)):
    print("A nota 3( %.2f ) é a maior nota após o cálculo do peso 1"% round(nota3), "(%.2f)"% round(notaPeso3) )
elif((notaPeso1 > notaPeso3) and (notaPeso2 > notaPeso3) and (notaPeso1 == notaPeso2)):
    print("As notas 1( %.2f )"% round(nota1), "e 2(%.2f) são as maiores notas após o cálculo dos pesos 1"% round(nota2),"(%.2f) "% round(notaPeso1), " e 2(%.2f)"% round(notaPeso2) )
elif((notaPeso1 > notaPeso2) and (notaPeso3 > notaPeso2) and (notaPeso1 == notaPeso3)):
    print("As notas 1( %.2f )"% round(nota1), "e 3(%.2f) são as maiores notas após o cálculo dos pesos 1"% round(nota2),"(%.2f) "% round(notaPeso1), " e 3(%.2f)"% round(notaPeso3) )
elif((notaPeso2 > notaPeso1) and (notaPeso3 > notaPeso1) and (notaPeso2 == notaPeso3)):
    print("As notas 2( %.2f )"% round(nota2), "e 3(%.2f) são as maiores notas após o cálculo dos pesos 2"% round(nota3),"(%.2f) "% round(notaPeso2), " e 3(%.2f)"% round(notaPeso3) )
elif((notaPeso1 == notaPeso2) and (notaPeso1== notaPeso3)):
    print("As três notas foram iguais.")
    
    


