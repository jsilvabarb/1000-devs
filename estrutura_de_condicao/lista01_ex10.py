# Exercício 10 lista 01 

print("----------Calcula as áreas de formas geométricas e informa qual a maior área calculada----------")

# Pegando dados de entrada
print("Área do trapézio")
baseMaior=float(input("Informe o valor da base maior:"))
baseMenor=float(input("Informe o valor da base menor:"))
alturaTrapezio=float(input("Informe o valor da altura:"))

print("Área do Quadrado")
lado=float(input("Informe o valor do lado:"))

print("Área do Retângulo")
largura= float(input("Informe o valor da largura:"))
alturaRetangulo = float(input("Informe o valor da altura:"))

print("Área do Círculo")
raio = float(input("Informe o valor do raio:"))

print("Área do Triângulo")
base = float(input("Informe o valor da base:"))
alturaTriangulo= float(input("Informe o valor da altura:"))

# Execução dos cálculos da área de cada obj
areaTrapezio = ((baseMaior + baseMenor) * alturaTrapezio)/2

areaQuadrado = lado * lado

areaRetangulo = largura * alturaRetangulo

areaCirculo = 3.14 * ( raio * raio)

areaTriangulo = (base* alturaTriangulo)/2

# Entregando a saída
print("A area do trapézio é: %.2f"%round(areaTrapezio, 2))
print("A area do quadrado é: %.2f"%round(areaQuadrado, 2))
print("A area do retângulo é: %.2f"%round(areaRetangulo, 2))
print("A area do círculo é: %.2f"%round(areaCirculo, 2))
print("A area do triângulo é: %.2f"%round(areaTriangulo, 2))

# Validando qual a maior Área
if(areaTriangulo > areaCirculo and areaTriangulo > areaRetangulo and areaTriangulo > areaQuadrado and areaTriangulo > areaTrapezio):
    # areaTriangulo é a maior area
    print("O objeto com a maior área é o Triângulo com: %.2f"%round(areaTriangulo, 2))
elif( areaCirculo > areaTriangulo and areaCirculo > areaRetangulo and areaCirculo > areaQuadrado and areaCirculo > areaTrapezio ):
    # areaCirculo é a maior area
    print("O objeto com a maior área é o Círculo com: %.2f"%round(areaCirculo, 2))
elif(areaRetangulo > areaTriangulo and areaRetangulo > areaCirculo and areaRetangulo > areaQuadrado and areaRetangulo > areaTrapezio ):
    # areaRetangulo é a maior area
    print("O objeto com a maior área é o Retângulo com: %.2f"%round(areaRetangulo, 2))
elif(areaQuadrado > areaTriangulo and areaQuadrado > areaCirculo and areaQuadrado > areaRetangulo and areaQuadrado > areaTrapezio):
    # areaQuadrado é a maior area
    print("O objeto com a maior área é o Quadrado com: %.2f"%round(areaQuadrado))
elif(areaTrapezio > areaTriangulo and areaTrapezio > areaCirculo and areaTrapezio > areaRetangulo and areaTrapezio > areaQuadrado):
    # areaTrapezio é a maior area
    print("O objeto com a maior área é o Trapézio com: %.2f"%round(areaTrapezio, 2))



