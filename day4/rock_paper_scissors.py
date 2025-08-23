# Jogo rock paper scissors
# mostrar código ASCII ART nas escolhas
import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
pedra
'''
papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
papel
'''
tesouras = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
tesouras
'''
opcoes = [pedra, papel, tesouras]
print("Bem vindo ao jogo de Pedra, Papel e Tesouras!")

escolha_usuario = int(input("O que você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesouras.\n"))

if escolha_usuario >= 3 or escolha_usuario < 0:
    print("Você digitou um número inválido. Você perde!")
else:
    print(opcoes[escolha_usuario])
    escolha_computador = random.randint(0, 2)
    print("Computador escolheu:")
    print(opcoes[escolha_computador])

    if escolha_usuario == 0 and escolha_computador == 2:
        print("Você ganha!")
    elif escolha_computador == 0 and escolha_usuario == 2:
        print("Você perde!")
    elif escolha_computador > escolha_usuario:
        print("Você perde!")
    elif escolha_usuario > escolha_computador:
        print("Você ganha!")
    elif escolha_computador == escolha_usuario:
        print("Empate!")



