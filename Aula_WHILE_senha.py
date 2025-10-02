import os
import time
os.system("cls")

contador=0

while contador == 0:
    os.system("cls")
    senha=int(input("Digite sua senha:"))
    contador+=1
    
    if senha == 1234:
        print("Iniciando o Sistema em :")
        for i in range (5,0,-1):
            print(f"{i}...")
            time.sleep (1)
            os.system("cls")
        print("Sistema Iniciado")
        print(15*"=")
        print("Pressione uma tecla para Iniciar")
        contador=1
    else:
        print("Senha incorreta")
        for i in range (5,0,-1):
            print(f"{i}...")
            time.sleep (1)
            os.system("cls")
        
        contador=0