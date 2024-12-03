import socket

HOST= "127.0.0.1"
PORT = 65440


s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((HOST, PORT))
while True:
    mensagem = input("Digite alguma coisa para enviar, ou 'sair' para terminar: ")    
    
    if mensagem.lower() == "sair":
        print("Você escolheu sair. Conexão será encerrada.")
        break  
    # Envia a mensagem digitada
    s.sendall(mensagem.encode('utf-8'))
s.close()