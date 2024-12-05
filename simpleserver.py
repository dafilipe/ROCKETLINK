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

    mensagem_pos_voo = conn.recv(1024).decode('utf-8')

    print( f"{mensagem_pos_voo}" )
   
    dadosfinais = conn.recv(1024).decode('utf-8')
    print(f"{dadosfinais}")

s.close()