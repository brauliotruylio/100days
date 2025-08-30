# Criar jogo de adivinhar o número

import art
from random import randint

print(art.logo)
print("Bem-vindo ao jogo de adivinhar o número!")
print("Estou pensando em um número entre 1 e 100.")

num = randint(1, 100)
nivel = input("Escolha a dificuldade. Digite 'facil' ou 'dificil': ")

if nivel == "facil":
    tentativas = 10
    print(f"Você tem {tentativas} tentativas para adivinhar o número.")
elif nivel == "dificil":
    tentativas = 5
    print(f"Você tem {tentativas} tentativas para adivinhar o número.")
else: # Default to easy if invalid input
    tentativas = 10
    print("Opção inválida. Dificuldade definida para 'facil'.")
    print(f"Você tem {tentativas} tentativas para adivinhar o número.")

def adivinhar(tentativas):
    global num # Declare num as global to access the variable from the outer scope
    while tentativas > 0:
        print(f"Você tem {tentativas} tentativas restantes.")
        chute_input = input("Tente adivinhar o número: ")
        if not chute_input.isdigit():
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue # Skip the rest of the loop and ask for input again

        chute = int(chute_input)
        if chute == num:
            print(f"Parabéns! Você acertou o número {num}!")
            return
        elif chute < num:
            print("Tente um número maior.")
            print()
        else:
            print("Tente um número menor.")
            print()
        tentativas -= 1
    print(f"Você perdeu! O número correto era {num}.")

adivinhar(tentativas)
