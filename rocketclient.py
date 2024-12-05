import socket
import time
from rocketsimu import voo  # Importa a simulação de voo

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

# Receber a confirmação para começar a voar
input("Pressione uma tecla para iniciarmos o VOO!!!!")

for tempo, altura, velocidade, massa in voo():
    # Cria a mensagem a ser enviada para o servidor
    mensagem = f"Tempo: {tempo:.1f}s | Altura: {altura:.2f}m | Velocidade: {velocidade:.2f}m/s | Massa: {massa:.2f}kg"
    tempovector.append(tempo)
    alturavector.append(altura)
    velocidadevector.append(velocidade)
    massavector.append(massa)
    
    client_socket.sendall(mensagem.encode())  # Envia a mensagem para o servidor
    print(f"Enviado para o servidor: {mensagem}")
    
    time.sleep(0.1)  # Aguarda 0.1s antes de enviar o próximo dado

# Calcula os valores máximos após o loop de voo
client_socket.sendall(mensagem_pos_voo.encode())
tempo_max = max(tempovector) 
altura_max = max(alturavector) 
velocidade_max = max(velocidadevector)

# Formata os valores com duas casas decimais e converte para string
dados_finais = f"Altura maxima = {tempo_max:.2f} que foi atingida com uma velocidade maxima = {altura_max:.2f} num voo de {velocidade_max:.2f}"

# Envia os valores máximos para o servidor
client_socket.sendall(dados_finais.encode()) 

print("Valores máximos enviados com sucesso")

# Fecha a conexão após enviar todos os dados
client_socket.close()
