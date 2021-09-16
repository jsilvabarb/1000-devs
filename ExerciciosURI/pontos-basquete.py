# Este código tem o objetivo de calcular a pontuação do jogo de acordo com a distância que o robô está da cesta

distancia = int(input("Digite a distância da sua posição até a cesta:"))

if( distancia > 0 and distancia <= 800):
    print("A cesta vale 1 ponto.")
elif(distancia > 800 and distancia <= 1400):
    print("A cesta vale 2 pontos!")
elif(distancia > 1400 and distancia <= 2000):
    print("A cesta vale 3 pontos!")
else:
    print("Distância inválida.")
