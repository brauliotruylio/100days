Classe MenuItem

Atributos:
    - name
    (str) O nome da bebida.
    Ex.: "latte"
    - cost
    (float) O preço da bebida.
    Ex.: 1,5
    - ingredients
    (dictionary) Os ingredientes e as quantidades necessárias para preparar a bebida.
    Ex.: {"water": 100, "coffee": 16}

Classe Menu

Métodos:
    - get_items()
    Retorna todos os nomes dos itens disponíveis do menu como uma string concatenada.
    Ex.: "latte/espresso/cappuccino"
    - find_drink(order_name)
    Parâmetro order_name: (str) O nome do pedido de bebidas.
    Busca no menu por uma bebida específica pelo nome. Retorna um objeto MenuItem se existir,
    caso contrário, retorna None.

Classe CoffeeMaker

Métodos:
    - report()
    Exibe um relatório de todos os recursos.
    Ex.:
    Água: 300ml
    Leite: 200ml
    Café: 100g
    - is_resource_sufficient(bebida)
    Parâmetro bebida: (ItemDoMenu) O objeto ItemDoMenu a ser preparado.
    Exibe uma mensagem se os ingredientes forem insuficientes.
    Retorna True quando o pedido de bebida pode ser feito, False se os ingredientes forem insuficientes.
    Ex.:
    True
    - make_coffee(pedido)
    Parâmetro pedido: (ItemDoMenu) O objeto ItemDoMenu a ser preparado.
    Deduz os ingredientes necessários dos recursos.

Classe MoneyMachine

Métodos:
    - report()
    Exibe o lucro atual
    Ex.:
    Dinheiro: $0
    - make_payment(custo)
    Parâmetro custo: (flutuante) O custo da bebida.
    Retorna True quando o pagamento é aceito, ou False se insuficiente.
    Ex.: False
