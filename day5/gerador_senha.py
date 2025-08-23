# criar app de gerador de senha

import random
import string

letras = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation

print("Bem vindo ao gerador de senhas!")

qtd_letras = int(input("Quantas letras você deseja? "))
qtd_numeros = int(input("Quantos números você deseja? "))
qtd_simbolos = int(input("Quantos símbolos você deseja? "))

senha_lista = []
for letra in range(qtd_letras):
    senha_lista.append(random.choice(letras))
for numero in range(qtd_numeros):
    senha_lista.append(random.choice(numeros))
for simbolo in range(qtd_simbolos):
    senha_lista.append(random.choice(simbolos))
random.shuffle(senha_lista)
senha = ''.join(senha_lista)
print(f"Sua senha gerada é: {senha}")
