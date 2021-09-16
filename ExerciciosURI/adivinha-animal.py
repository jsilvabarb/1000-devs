# Este código tem o objetivo de adivinhar qual animal o usuário pensou de acordo com três palavras

palavra1, palavra2, palavra3 = input("Dê três dicas de qual animal você está pensando: ").split()

print("________________________________________________________________________________")

 # Casos vertebrados
if(palavra1 == "vertebrado"):   
    print("Animal vertebrado")

    # Aves
    if(palavra2 == "ave"):
        print("O animal é um vertebrado e é uma ave.")

        if(palavra3 == "carnivoro"):
            print("O animal é um vertebrado, é uma ave e é carnívoro.")
            print("---------------------O animal é uma águia!----------------------")
        elif(palavra3 == "onivoro"):
            print("O animal é um vertebrado, é uma ave e é onívoro.")
            print("---------------------O animal é uma pomba!------------------")
        else:
            print("Palavra inválida!")
    # mamiferos
    elif(palavra2 == "mamifero"):
        print("O animal é um vertebrado e é um mamífero.")

        if(palavra3 == "onivoro"):
            print("O animal é um vertebrado, é uma ave e é onivoro.")
            print("-----------------O animal é um ser humano!----------------------")
        elif(palavra3 == "herbivoro"):
            print("O animal é um vertebrado, é uma ave e é herbívoro.")
            print("-----------------O animal é uma vaca!--------------------------")
        else:
            print("Palavra inválida!")
    else:
        print("Palavra inválida!")
 # Casos invertebrados
elif(palavra1 == "invertebrado"):
   
    print("Animal Invertebrado")

    # Insetos
    if(palavra2 == "inseto"):
        print("O animal é um vertebrado e é um inseto.")

        if(palavra3 == "hematofago"):
            print("O animal é um invertebrado, é um inseto e é hematofago.")
            print("------------------------O animal é uma pulga!-----------------------")
        elif(palavra3 == "herbivoro"):
            print("O animal é um invertebrado, é um inseto e é herbivoro.")
            print("------------------------------O animal é uma lagarta!-----------------------!")
        else:
            print("Palavra inválida!")

    # Anelideos
    elif(palavra2 == "anelideo"):
        print("O animal é um invertebrado e é um anelideo.")

        if(palavra3 == "hematofago"):
            print("O animal é um invertebrado, é um anelideo e é hematofago.")
            print("-----------------O animal é uma sanguessuga!----------------------")
        elif(palavra3 == "onivoro"):
            print("O animal é um invertebrado, é um anelideo e é onivoro.")
            print("-----------------O animal é uma minhoca!--------------------------")
        else:
            print("Palavra inválida!")
    else:
        print("Palavra inválida!")
else: 
    print("Palavra Invalida")