# Criar máquina de café digital
# Listar os TODOs
# TODO: 1. Perguntar ao usuário qual café ele quer
# TODO: 2. Checar se os recursos são suficientes
# TODO: 3. Processar moedas
# TODO: 4. Checar se a transação foi bem sucedida
# TODO: 5. Fazer café


MENU = {
    "espresso": {
        "ingredientes": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredientes": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredientes": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 900,
    "milk": 300,
    "coffee": 100,
}

money = 0

def imprimir_relatorio():
    """Imprime o relatório de recursos e dinheiro."""
    print(f"Água: {resources['water']}ml")
    print(f"Leite: {resources['milk']}ml")
    print(f"Café: {resources['coffee']}g")
    print(f"Dinheiro: ${money:.2f}")

def recursos_sao_suficientes(ingredientes_do_pedido):
    """Retorna True quando o pedido pode ser feito, False se os ingredientes forem insuficientes."""
    for item in ingredientes_do_pedido:
        if ingredientes_do_pedido[item] > resources[item]:
            print(f"Desculpe, não há {item} suficiente.")
            return False
    return True

def processar_moedas():
    """Retorna o total calculado a partir das moedas inseridas."""
    print("Por favor, insira as moedas.")
    total = int(input("Quantas moedas de 25 centavos?: ")) * 0.25
    total += int(input("Quantas moedas de 10 centavos?: ")) * 0.10
    total += int(input("Quantas moedas de 5 centavos?: ")) * 0.05
    total += int(input("Quantas moedas de 1 centavo?: ")) * 0.01
    return total

def transacao_bem_sucedida(dinheiro_recebido, custo_bebida):
    """Retorna True quando o pagamento é aceito, ou False se o dinheiro for insuficiente."""
    if dinheiro_recebido >= custo_bebida:
        troco = round(dinheiro_recebido - custo_bebida, 2)
        print(f"Aqui está ${troco:.2f} de troco.")
        global money
        money += custo_bebida
        return True
    else:
        print("Desculpe, dinheiro insuficiente. Dinheiro devolvido.")
        return False

def fazer_cafe(nome_bebida, ingredientes_pedido):
    """Deduz os ingredientes necessários dos recursos."""
    for item in ingredientes_pedido:
        resources[item] -= ingredientes_pedido[item]
    print(f"Aqui está o seu {nome_bebida} ☕. Aproveite!")


is_on = True

while is_on:
    # TODO: 1. Perguntar ao usuário qual café ele quer
    choice = input("Qual café você quer? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        imprimir_relatorio()
    elif choice in MENU:
        drink = MENU[choice]
        # TODO: 2. Checar se os recursos são suficientes
        if recursos_sao_suficientes(drink["ingredientes"]):
            # TODO: 3. Processar moedas
            pagamento = processar_moedas()
            # TODO: 4. Checar se a transação foi bem sucedida
            if transacao_bem_sucedida(pagamento, drink["cost"]):
                # TODO: 5. Fazer café
                fazer_cafe(choice, drink["ingredientes"])
    else:
        print("Escolha inválida. Tente novamente.")
