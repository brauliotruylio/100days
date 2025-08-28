import art

print(art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Não é possível dividir por zero.")
    return n1 / n2

# Adicionar as 4 funções em um dicionário. Keys = '+ - * /', values = funções
operacoes = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

n1 = float(input("Digite o primeiro número: "))

for simbolo in operacoes:
    print(simbolo)

operacao = input("Escolha uma operação: ")

n2 = float(input("Digite o próximo número: "))

funcao_escolhida = operacoes[operacao]
resultado = funcao_escolhida(n1, n2)

print(f"{n1} {operacao} {n2} = {resultado}")

while input(f"Deseja continuar calculando com {resultado}? (s/n): ") == "s":
    n1 = resultado
    for simbolo in operacoes:
        print(simbolo)

    operacao = input("Escolha uma operação: ")

    n2 = float(input("Digite o próximo número: "))

    funcao_escolhida = operacoes[operacao]
    resultado = funcao_escolhida(n1, n2)

    print(f"{n1} {operacao} {n2} = {resultado}")

print("Obrigado por usar a calculadora!")
