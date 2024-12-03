import socket
import time
from rocketsimu import voo  # Importa a simulação de voo
import random

# Configurações do cliente
HOST = '127.0.0.1'  # Endereço do servidor
PORT = 65440        # Porta do servidor

mensagem_pos_voo = "Voo bem sucedido!! iremos enviar os dados todos dentro de 2 segundos"
tempovector = []
alturavector= []
velocidadevector=[]
massavector= []

# Criação do socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
#receber a confirmaçao para comecar a voar
input ("pressione uma tecla para iniciarmos o VOO!!!!")

for tempo, altura, velocidade, massa in voo():
    # Cria a mensagem a ser enviada para o servidor
    randomval = random.randint(1, 10)
    mensagem = f"Tempo: {tempo+randomval:.1f}s | Altura: {altura+randomval:.2f}m | Velocidade: {velocidade+randomval:.2f}m/s | Massa: {massa+randomval:.2f}kg"
    tempovector.append(tempo)
    alturavector.append(altura)
    velocidadevector.append(velocidade)
    massavector.append(massa)
    # os valores são guardados em voo por causa dos valores random e depois de voo serem estudados
    
    client_socket.sendall(mensagem.encode())  # Envia a mensagem para o servidor
    print(f"Enviado para o servidor: {mensagem}")
    
    time.sleep(0.1)  # Aguarda 0.1s antes de enviar o próximo dado
    

client_socket.sendall(str(mensagem_pos_voo).encode())
time.sleep(2)
#espera 2 segundos
client_socket.sendall(str(tempovector).encode())
client_socket.sendall(str(alturavector).encode())
client_socket.sendall(str(velocidadevector).encode())
client_socket.sendall(str(massavector).encode())

print("Enviado com sucesso")

client_socket.close()
