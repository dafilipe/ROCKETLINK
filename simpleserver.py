import socket
import ast



HOST = "127.0.0.1"
PORT = 65440


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  #criar um server
     s.listen() 
     print("esperando conexão...")
     conn, addr = s.accept()  
                                                                


with conn:  #o servidor fica neste momento a "ouvir" 
    print(f"Foi conectado por {addr}")
  
    while True:
        data = conn.recv(1024)  # Recebe dados do lançamento em sequencia
        if not data:
            break
        print(f"{data.decode('utf-8')}")

    mensagem_pos_voo = conn.recv(1024).decode('utf-8') 

    print( f"{mensagem_pos_voo}" )
   
    dadosfinais = conn.recv(1024).decode('utf-8')   
    print(f"{dadosfinais}")                     #imprime os highlights do voo

s.close() #fecha o servidor porque missao dada e' missao cumprida 