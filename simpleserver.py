import socket
import rocketsimu


HOST = "192.168.1.244"
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
        