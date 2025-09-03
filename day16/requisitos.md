# Requisitos do Programa da Máquina de Café

## 1. Avise o usuário perguntando "O que você gostaria? (expresso/latte/cappuccino/):"
a. Verifique a entrada do usuário para decidir o que fazer em seguida.
b. O prompt deve mostrar sempre que a ação for concluída, por exemplo, assim que a bebida for
dispensada. O prompt deve aparecer novamente para servir o próximo cliente.

## 2. Desligue a Máquina de Café digitando "off" no prompt.
a. Os responsáveis ​​pela manutenção da máquina de café podem usar "off" como a palavra secreta para desligar a
máquina. Seu código deve encerrar a execução quando isso acontecer.
## 3. Imprima o relatório.

a. Quando o usuário digitar "report" no prompt, um relatório deve ser gerado mostrando os
valores atuais dos recursos. Por exemplo:
Água: 100ml
Leite: 50ml
Café: 76g
Dinheiro: R$ 2,50

## 4. Verifique se os recursos são suficientes?
a. Quando o usuário escolhe uma bebida, o programa deve verificar se há recursos suficientes
para prepará-la.
b. Por exemplo, se o Latte requer 200 ml de água, mas há apenas 100 ml restantes na máquina. Ele não deve
continuar a preparar a bebida, mas imprimir: "Desculpe, não há água suficiente".
c. O mesmo deve acontecer se outro recurso estiver esgotado, por exemplo, leite ou café.

## 5. Processar moedas.
a. Se houver recursos suficientes para preparar a bebida selecionada, o programa deve
solicitar ao usuário que insira moedas.
b. Lembre-se de que moedas de 25 centavos = $ 0,25, moedas de 10 centavos = $ 0,10, moedas de 5 centavos = $ 0,05, moedas de um centavo = $ 0,01
c. Calcule o valor monetário das moedas inseridas. Por exemplo, 1 moeda de 25 centavos, 2 moedas de 10 centavos, 1 moeda de 5 centavos, 2
centavos = 0,25 + 0,1 x 2 + 0,05 + 0,01 x 2 = R$ 0,52

## 6. Verificar se a transação foi bem-sucedida?
a. Verificar se o usuário inseriu dinheiro suficiente para comprar a bebida selecionada. Ex.:
O café com leite custou R$ 2,50, mas ele inseriu apenas R$ 0,52. Após a contagem das moedas, o programa
deveria dizer "Desculpe, não é dinheiro suficiente. Dinheiro devolvido".
b. Mas se o usuário inseriu dinheiro suficiente, o custo da bebida será adicionado à
máquina como lucro e isso será refletido na próxima vez que o "relatório" for acionado. Ex.:
Água: 100ml
Leite: 50ml
Café: 76g
Dinheiro: R$ 2,50
c. Se o usuário inseriu muito dinheiro, a máquina deve oferecer troco.
Ex.: “Aqui estão $ 2,45 de troco.” O troco deve ser arredondado para 2 casas decimais.

## 7. Prepare um café.
a. Se a transação for bem-sucedida e houver recursos suficientes para preparar a bebida
selecionada pelo usuário, os ingredientes para preparar a bebida devem ser deduzidos dos recursos da máquina de café.
Ex.: informe antes de comprar latte:
Água: 300ml
Leite: 200ml
Café: 100g
Dinheiro: $ 0
Relatório após comprar latte:
Água: 100ml
Leite: 50ml
Café: 76g
Dinheiro: $ 2,5
b. Após deduzir todos os recursos, diga ao usuário: “Aqui está seu latte. Aproveite!”. Se latte
foi a bebida escolhida.
