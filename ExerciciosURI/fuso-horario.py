# Este código tem como objetivo retornar a hora local do destino quando o usuário informa:
#   - A hora de Saída;
#   - O tempo de Viagem;
#   - E o fuso horário de destino em relação à origem.

# ----------------Regras-----------------------
def validaPartida(partida) :
    if (partida >= 0 and partida <=23):
        return True
    else:
        return False

def validaTempoDeViagem(tempoDeViagem):
    if(tempoDeViagem >=1 and tempoDeViagem <= 12):
        return True
    else: 
        return False

def validaFuso(fuso):
    if(fuso >= -5 and fuso <= 5):
        return True
    else:
        return False
# map(float, input("Digite as notas do aluno:").split())

partida, tempoDeViagem, fuso = map(int, input("Digite a hora de partida, tempo de viagem e fuso em relação a origem, respectivamente: ").split()) 

print("\n______________________________________________________\n")

# Casos todas as regras retonem verdadeiro então damos continuidade ao processamento
if(validaPartida(partida) and validaTempoDeViagem(tempoDeViagem) and validaFuso(fuso)) :
    horaDestino = partida + tempoDeViagem + (fuso)

    if(horaDestino >= 24):
        horaDestino = horaDestino - 24
    elif(horaDestino < 0):
        horaDestino = horaDestino + 24
    print("Serão", horaDestino, "horas quando você chegar ao seu destino.")
# Caso contrário mandamos um alerta para o usuário
else:
    print("Valores inválidos.")
