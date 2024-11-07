import math
import random

massa = 500 #g
g = 9.81 #ms^-2
altitude_inicial = 0 #m
velocidade_inicial = 0 #ms^-1
vento = random.uniform (0,5) #ms^-1
cap_motor = 15 #ms^-2
burn_rate = 0.5 #ls^-1

def voo():
    acelaracao = cap_motor-g
'''
#import random

# Parâmetros do foguete
massa = 500  # massa em gramas (precisa ser convertida para kg)
massa /= 1000  # convertendo para kg
g = 9.81  # aceleração gravitacional em m/s^2
altitude_inicial = 0  # altura inicial (m)
velocidade_inicial = 0  # velocidade inicial (m/s)
vento = random.uniform(0, 5)  # vento entre 0 e 5 m/s
cap_motor = 15  # aceleração máxima do motor em m/s^2
burn_rate = 0.5  # taxa de queima de combustível em L/s
tempo_voo = 0  # tempo de voo (s)

# Função de voo
def voo():
    global massa, altitude_inicial, velocidade_inicial, tempo_voo

    # Inicializa as variáveis
    altura = altitude_inicial
    velocidade = velocidade_inicial
    tempo = 0
    tempo_total = 100  # Define um tempo máximo para o voo

    # Simulação do voo
    while tempo < tempo_total and massa > 0:
        # Calcular a aceleração
        aceleracao = cap_motor - g  # Aceleração do foguete (sem resistência do ar)
        
        # Considerar o vento na velocidade
        velocidade += vento

        # Atualizar a velocidade e altura
        velocidade += aceleracao * 0.1  # Atualiza a velocidade com a aceleração
        altura += velocidade * 0.1  # Atualiza a altura com a velocidade

        # Reduz a massa com base na taxa de queima de combustível
        massa -= burn_rate * 0.1  # O combustível diminui a cada intervalo de tempo

        # Atualiza o tempo
        tempo += 0.1

        # Exibe o estado do voo a cada 10 segundos
        if tempo % 10 == 0:
            print(f"Tempo: {tempo:.1f}s | Altura: {altura:.2f}m | Velocidade: {velocidade:.2f}m/s | Massa: {massa:.2f}kg")

    return altura, velocidade, tempo

# Chamada da função
altura_final, velocidade_final, tempo_total_voo = voo()

# Resultado final
print(f"\nResultado final do voo:")
print(f"Altura alcançada: {altura_final:.2f} metros")
print(f"Velocidade final: {velocidade_final:.2f} m/s")
print(f"Tempo total de voo: {tempo_total_voo:.2f} segundos")
'''