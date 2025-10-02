# O usuário tenta advinhar um número de 0 a 10

import random
import os

# Cores ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

os.system('cls')

print(CYAN + "╔" + "═"*38 + "╗" + RESET)
print(CYAN + "║" + RESET + "  🔮 ADIVINHE O QUE ESTOU PENSANDO    " + CYAN + "║" + RESET)
print(CYAN + "╚" + "═"*38 + "╝" + RESET)

numero_secreto=random.randint(0,10)
tentativas = 0
acertou = 0 # não acertou = 0 , acertou =1

print(f"\n{YELLOW}🤔 Pensei em um número entre 0 e 10...{RESET}")
print(f"{CYAN}Em qual número estou pensando?{RESET}")

while acertou == 0:
    numero_escolhido = int(input("\n👉 Seu palpite: "))
    tentativas+=1
    os.system('cls')
    if numero_escolhido == numero_secreto:
        os.system('cls')
        print(GREEN + "🎉 PARABÉNS! Você acertou!" + RESET)
        print(f"\n✨ O número pensado foi {CYAN}{numero_secreto}{RESET}")
        print(f"📌 Seu número de tentativas foi: {tentativas}")
        acertou = 1 # Sai do loop
    else:
        if numero_escolhido < numero_secreto:
            print(RED + f"❌ ERROU! Tente um número MAIOR que {numero_escolhido}" + RESET)
        else:
            print(RED + f"❌ ERROU! Tente um número MENOR que {numero_escolhido}" + RESET)
        
        
        if numero_escolhido > 10 or numero_escolhido < 0:
            print(YELLOW + "⚠️ Escolha um número de 0 a 10!" + RESET)        