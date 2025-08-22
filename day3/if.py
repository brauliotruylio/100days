# Teste de if's aninhados
print('Bem vindo ao Rollercoaster!')
altura = int(input('Qual é a sua altura em cm? '))
if altura >= 120:
    print('Você pode entrar no brinquedo!')
    idade = int(input('Qual é a sua idade? '))
    if idade <= 12:
        print('O preço do ingresso é R$ 5,00.')
    elif idade <= 18:
        print('O preço do ingresso é R$ 7,00.')
    else:
        print('O preço do ingresso é R$ 10,00.')

    fotos = input('Você gostaria de tirar uma foto? (S/N) ')
    if fotos.upper() == 'S':
        print('O custo da foto é R$ 3,00.')

    else:
        print('Você escolheu não tirar uma foto.')
    

else:
    print('Desculpe, você não pode entrar no brinquedo.')

