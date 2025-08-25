import random
from word_list import word_list
from forcas_art import stages
from forcas_art import logo


# TODO 1: Escolher aleatoriamente uma palavra de uma lista e atribua a uma variável e imprima
print(logo)

chosen_word = random.choice(word_list)

# TODO 2: Perguntar ao usuário para adivinhar uma letra e fazer a suposição em letra minúscula
# TODO 2.1: Criar a palceholder com o mesmo número de letras na palavra escolhida e imprimi-la
# TODO 2.2: Atualizar a placeholder para que, se o usuário adivinhar corretamente a letra,
#  a letra seja revelada na posição correta na palavra e imprimi-la (não é necessário lidar com várias ocorrências da mesma letra)

display = []
for _ in chosen_word:
    display += "_"
print(f'Palavra: {"".join(display)}\n')

game_over = False
lives = 6  # Número de tentativas erradas permitidas

while not game_over:
    print(f"******* Você tem {lives} vidas restantes. *******\n")
    guess = input("Adivinhe uma letra: \n").lower()

    if guess in display:
        print(f'Você já adivinhou a letra {guess}. Tente outra letra.\n')
        continue  # Pular o restante do loop e pedir uma nova letra

# TODO 3: Verificar se o usuário adivinhou a letra correta, se sim, revelar a letra na posição correta
# TODO 3.1: Criar um loop para verificar todas posições na palavra escolhida

    for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    print(f'Palavra: {"".join(display)}')

    if "_" not in display:
        game_over = True
        print("*********Parabéns! Você adivinhou a palavra!**********\n")
# TODO 4: Se o usuário errar a letra, mostrar a próxima parte do corpo do boneco da forca
# TODO 4.1: Criar uma variável para controlar o número de tentativas erradas
# TODO 4.2: Se o número de tentativas erradas chegar a 6, o jogo acaba e o usuário perde
# TODO 4.3: Imprimir a arte da forca correspondente ao número de tentativas erradas

    if guess not in chosen_word:
        print('Você errou a letra {guess}.\n')
        lives -= 1

        if lives == 0:
            game_over = True
            print(f'***********Você perdeu. A palavra era {chosen_word}.***********\n')
    print(stages[lives])









