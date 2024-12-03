import random

# Parâmetros do foguete
massa = 0.500  # kg
massa_vazio = 0.200  # kg
g = 9.81  # aceleração gravitacional em m/s^2
altitude_inicial = 0  # altura inicial (m)
velocidade_inicial = 0  # velocidade inicial (m/s)
vento = random.uniform(0, 5)  # vento entre 0 e 5 m/s
cap_motor = 15  # aceleração máxima do motor em m/s^2
burn_rate = 0.5  # taxa de queima de combustível em kg/s
tempo_voo = 0  # tempo de voo (s)
tempo_maximo_voo = 100  # tempo máximo do voo em segundos

def voo():
    global massa, altitude_inicial, velocidade_inicial, tempo_voo
    # Inicializa as variáveis
    altura = altitude_inicial
    velocidade = velocidade_inicial
    tempo = 0
    massa_atual = massa
    aceleracao = cap_motor - g #condiçao inicial
    # Simulação do voo
    while tempo < tempo_maximo_voo and altura >= 0:  # O voo termina quando o tempo máximo for alcançado ou a altura for negativa
        # Calcular a aceleração do foguete
        if massa_atual > massa_vazio:
            massa_atual = massa_atual - (burn_rate * 0.1)  # O combustível diminui a cada intervalo de tempo
            velocidade += aceleracao * 0.1  # Atualiza a velocidade com a aceleração
            altura += velocidade * 0.1  # Atualiza a altura com a velocidade
            tempo += 0.1  # Atualiza o tempo                         
        else:
            aceleracao = 9.81  # Apenas a gravidade atua após o combustível acabar
            velocidade -= aceleracao * 0.1  # Atualiza a velocidade com a aceleração
            altura += velocidade * 0.1  # Atualiza a altura com a velocidade
            if altura < 0:
                break
            tempo += 0.1  # Atualiza o tempo                         
            velocidade -= vento
        
        yield tempo, altura, velocidade, massa_atual # Retorna os dados do voo a cada passo

