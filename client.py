import socket
import time
from rocketsimu import voo  # Importa a simulação de voo

# Configurações do cliente
HOST = '192.168.1.244'  # Endereço do servidor
PORT = 65440        # Porta do servidor

# Criação do socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
for tempo, altura, velocidade, massa in voo():
    # Cria a mensagem a ser enviada para o servidor
    mensagem = f"Tempo: {tempo:.1f}s | Altura: {altura:.2f}m | Velocidade: {velocidade:.2f}m/s | Massa: {massa:.2f}kg"
    client_socket.sendall(mensagem.encode())  # Envia a mensagem para o servidor
    print(f"Enviado para o servidor: {mensagem}")
    
    time.sleep(0.1)  # Aguarda 0.1s antes de enviar o próximo dado

# Finaliza a conexão
client_socket.close()
