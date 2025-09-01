# Criar jogo de comparação Higher Lower
from art import logo, versus
from game_data import data
import random

def formata_dados(conta):
    '''Formata os dados da conta'''
    conta_nome = conta['name']
    conta_descricao = conta['description']
    conta_pais = conta['country']
    return f"{conta_nome}, a {conta_descricao}, from {conta_pais}."

def checar_resposta(escolha, a_conta_seguidor, b_conta_seguidor):
    '''Checa a resposta do usuário'''
    if a_conta_seguidor > b_conta_seguidor:
        return escolha == 'a'
    else:
        return escolha == 'b'

print(logo)
score = 0
game_should_continue = True
conta_b = random.choice(data)

while game_should_continue:
    conta_a = conta_b
    conta_b = random.choice(data)
    if conta_a == conta_b:
        conta_b = random.choice(data)

    print(f"Compare A: {formata_dados(conta_a)}.")
    print()
    print(versus)
    print()
    print(f"Contra B: {formata_dados(conta_b)}.")
    escolha = input('Quem tem mais seguidores? Digite "A" or "B": ').lower()

    print('\n' * 20)
    print(logo)

    a_conta_seguidor = conta_a['follower_count']
    b_conta_seguidor = conta_b['follower_count']
    resposta_certa = checar_resposta(escolha, a_conta_seguidor, b_conta_seguidor)

    if resposta_certa:
        score += 1
        print("Você acertou! Escore atual: {score}")
    else:
        print("Você errou! Score final: {score}")
        game_should_continue = False






