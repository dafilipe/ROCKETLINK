import socket
import ast



HOST = "127.0.0.1"
PORT = 65440

#criar um server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  
     s.bind((HOST,PORT)) 
     s.listen() 
     print("esperando conexão...")
     conn, addr = s.accept()  
                                                                

#receber data
with conn:
    print(f"Foi conectado por {addr}")
  
    while True:
        data = conn.recv(1024)  # Recebe dados do cliente
        if not data:
            break
        print(f"{data.decode('utf-8')}")

    mensagem_pos_voo = conn.recv(1024)
    print(f"{mensagem_pos_voo.decode('utf-8')}")

    tempo_pos_voo = ast.literal_eval(conn.recv(1024))
    altura_pos_voo = ast.literal_eval(conn.recv(1024))
    velocidade_pos_voo = ast.literal_eval(conn.recv(1024))
    massa_pos_voo = ast.literal_eval(conn.recv(1024))

maxvel = max(velocidade_pos_voo)
print (f"velocidade Maxima = {maxvel}")
maxalt = max(altura_pos_voo)
print (f"Altura Maxima = {maxalt}")
maxtmp = max(tempo_pos_voo) + 1
print(f"Tempo de voo foi = {maxtmp}")    
        

s.close()