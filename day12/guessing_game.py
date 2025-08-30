# Criar jogo de adivinhar o número

import art
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def definir_dificuldade():
    """Pede a dificuldade ao usuário e retorna o número de tentativas."""
    nivel = input("Escolha a dificuldade. Digite 'facil' ou 'dificil': ")
    if nivel == "dificil":
        return HARD_LEVEL_TURNS
    else:
        if nivel != "facil":
            print("Opção inválida. Dificuldade definida para 'facil'.")
        return EASY_LEVEL_TURNS

def adivinhar(numero_secreto, tentativas):
    """Executa o loop principal do jogo de adivinhação."""
    while tentativas > 0:
        print(f"\nVocê tem {tentativas} tentativas restantes.")
        chute_input = input("Tente adivinhar o número: ")

        if not chute_input.isdigit():
            print("Entrada inválida. Por favor, digite um número inteiro.")
            continue

        chute = int(chute_input)
        if chute == numero_secreto:
            print(f"Parabéns! Você acertou o número {numero_secreto}!")
            return
        elif chute < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

        tentativas -= 1
    print(f"Você perdeu! O número correto era {numero_secreto}.")

# --- Início do Jogo ---
print(art.logo)
print("Bem-vindo ao jogo de adivinhar o número!")
print("Estou pensando em um número entre 1 e 100.")

numero_aleatorio = randint(1, 100)
total_tentativas = definir_dificuldade()

print(f"Você tem {total_tentativas} tentativas para adivinhar o número.")
adivinhar(numero_secreto=numero_aleatorio, tentativas=total_tentativas)
