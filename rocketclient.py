import socket
import time
from rocketsimu import voo  # Importa a simulacao de voo
import random

# Configuracoes do cliente
HOST = '127.0.0.1'  # Endereço do servidor 
PORT = 65440        # Porta do servidor// é como a campainha que tocamos

# Mensagem pos-voo e vetores para guardar os dados
mensagem_pos_voo = "Voo bem sucedido!! iremos enviar os dados todos dentro de 2 segundos"
tempovector = []  # Guarda os tempos do voo
alturavector = []  # Guarda as alturas alcançadas
velocidadevector = []  # Guarda as velocidades registradas
massavector = []  # Guarda as massas durante o voo

# Criacao da conexao do cliente com o servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Criando o socket
client_socket.connect((HOST, PORT))  # Conectando ao servidor


input("Pressione uma tecla para iniciarmos o VOO!!!!") #fica a espera de carregar numa tecla para dar partida

randomnum = random.randint(1, 15) #valores para intreferencia 

# Loop principal: simulamos o voo e mandamos os dados para o servidor
for tempo, altura, velocidade, massa in voo():
    # Criamos uma mensagem com os dados do momento
    mensagem = f"Tempo: {tempo+randomnum:.1f}s | Altura: {altura+randomnum:.2f}m | Velocidade: {velocidade+randomnum:.2f}m/s | Massa: {massa+randomnum:.2f}kg"
    
    # Guardamos os dados veridicos nos respectivos vetores
    tempovector.append(tempo)
    alturavector.append(altura)
    velocidadevector.append(velocidade)
    massavector.append(massa)
    
    # Mandamos os dados para o servidor
    #possibilidade de perca de dados
    if random.random() < 0.8:  # 80% de chance de processar o pacote
        print("enviou")
        client_socket.sendall(mensagem.encode())
        print(f"Enviado para o servidor: {mensagem}")
    else:  # 20% de chance de ignorar o pacote
        print("perdeu-se")
        time.sleep(0.1)
    
    time.sleep(0.1)

#encontramos os highligths do voo
tempo_max = max(tempovector)  # O maior tempo registrado
altura_max = max(alturavector)  # A maior altura alcançada
velocidade_max = max(velocidadevector)  # A maior velocidade atingida

# Preparamos a mensagem final com os recordes
dados_finais = f"Altura maxima = {altura_max:.2f}m que foi atingida com uma velocidade maxima = {velocidade_max:.2f}m/s num voo de {tempo_max:.2f}s"


client_socket.sendall(mensagem_pos_voo.encode())  
client_socket.sendall(dados_finais.encode())  # Dados finais do voo

print("Valores máximos enviados com sucesso")

# Fechamos a conexao porque missao dada e' missão cumprida
client_socket.close()
