import os
import time

senha=0

while senha !=1234:
    senha=int(input("Digite sua senha:"))
    print("Senha incorreta")
    os.system("cls")

print("Iniciando o Sistema em :")
for i in range (5,0,-1):
    print(f"{i}...")
    time.sleep (1)
print("Sistema Iniciado")
print(15*"=")
print("Pressione uma tecla para Iniciar")