# Você vai escrever um programa que imprime automaticamente a solução do jogo FizzBuzz. Estas são as regras do jogo FizzBuzz:

# Seu programa deve imprimir cada número de 1 a 100, um por vez, incluindo o número 100.

# Mas quando o número for divisível por 3, em vez de imprimir o número, ele deve imprimir "Fizz".

# Quando o número for divisível por 5, em vez de imprimir o número, ele deve imprimir "Buzz".

# E se o número for divisível por 3 e 5, por exemplo, 15, em vez do número, ele deve imprimir "FizzBuzz".

print("Iniciando o FizzBuzz")

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
