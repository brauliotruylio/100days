# TODO 1: Crie uma função chamada encrypt() que receba 'original_text' e 'shift_amount' como 2 entradas.
# TODO 2: Dentro da função encrypt(), deslocar cada letra do 'original_text' para frente no alfabeto pelo 'shift_amount' e imprime o texto criptografado.
# TODO 4: What happens if you try to shift z forwards by 9? Can you fix this?
#
# TODO 3: Chame a função encrypt() e passe as entradas do usuário. Você conseguirá testar seu código e criptografar uma mensagem.
# Usar index()
# TODO 5: Crie a função decrypt() que pega 'original_text' e 'shift_amount' como entradas.
# TODO 6: Dentro da função decrypt(), desloque cada letra do 'original_text' para trás no alfabeto pelo 'shift_amount' e imprime o texto descriptografado.
# TODO 7: - Combine as funções encrypt() e decrypt() em uma única função chamada caesar()
        # - use o valor de 'direction' para decidir se deve criptografar ou descriptografar a mensagem.
        # - Chame a função caesar() em vez de chamar as funções encrypt() e decrypt() separadamente e passe as 3 entradas, direction, text e shift.

import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    cipher_texto = ""

    for letter in original_text:
        if letter not in alphabet:
            cipher_texto += letter
        else:
            posicao_deslocada = alphabet.index(letter) + shift_amount
            posicao_deslocada = posicao_deslocada % len(alphabet)  # Corrige o problema de ultrapassar 'z
            cipher_texto += alphabet[posicao_deslocada]

    print(f"O texto criptografado é {cipher_texto}")

def decrypt(original_text, shift_amount):
    decipher_texto = ""

    for letter in original_text:
        posicao_deslocada = alphabet.index(letter) - shift_amount
        posicao_deslocada = posicao_deslocada % len(alphabet)  # Corrige o problema de ultrapassar 'a'
        decipher_texto += alphabet[posicao_deslocada]

    print(f"O texto descriptografado é {decipher_texto}")

def caesar(original_text, shift_amount, direction):
    if direction == "encode":
        encrypt(original_text, shift_amount)
    elif direction == "decode":
        decrypt(original_text, shift_amount)
    else:
        print("Direção inválida. Use 'encode' ou 'decode'.")
should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
if restart == "no":
    should_continue = False
    print("Goodbye")
