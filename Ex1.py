import time

print("Contagem regressiva para os fogos de artifício")

for i in range (10,0,-1):
    print(f"{i}...")
    time.sleep (1) # Pausa de 1 segundo

print("BOOM!") 