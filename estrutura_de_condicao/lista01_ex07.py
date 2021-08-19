#Código que prevê o peso do usuário caso ele(a) engorde ou emagreça

peso=float(input("Informe seu peso atual:"))

engordarUm = peso +(peso * 0.15)
engordarDois = peso +(peso * 0.20)

diferencaAcrescimo = engordarDois - engordarUm 

print("Caso você engorde 15%% ficara com: %.2f"% round(engordarUm,2)," KG")
print("Caso você engorde 20%% ficara com: %.2f"% round(engordarDois,2)," KG")

if(diferencaAcrescimo >= 4.5):
    print("Você deve procurar um(a) nutricionista!")
