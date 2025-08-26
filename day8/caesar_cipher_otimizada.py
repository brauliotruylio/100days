import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, direction):
    result_text = ""

    if direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            result_text += letter
        else:
            posicao_deslocada = alphabet.index(letter) + shift_amount
            posicao_deslocada = posicao_deslocada % len(alphabet)  # Corrige o problema de ultrapassar 'z' ou 'a'
            result_text += alphabet[posicao_deslocada]
    print(f"O texto resultante é {result_text}")

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
