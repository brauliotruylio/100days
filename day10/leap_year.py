'''
Ano Bissexto

💪 Este é um desafio difícil! 💪

Escreva um programa que retorne Verdadeiro ou Falso se um determinado ano for bissexto.
Um ano normal tem 365 dias, os anos bissextos têm 366, com um dia extra em fevereiro.
A razão pela qual temos anos bissextos é realmente fascinante, e este vídeo faz mais justiça a isso.
É assim que você descobre se um determinado ano é bissexto.

- em todos os anos divisíveis por 4 sem resto
- exceto todos os anos divisíveis por 100 sem resto
- a menos que o ano também seja divisível por 400 sem resto

Se o inglês não for sua primeira língua ou se a lógica acima for confusa, tente usar este fluxograma.

por exemplo: O ano 2000:

2000 ÷ 4 = 500 (ano bissexto)
2000 ÷ 100 = 20 (não bissexto)
2000 ÷ 400 = 5 (ano bissexto!)

Portanto, o ano 2000 é um ano bissexto.

Mas o ano 2100 não é um ano bissexto porque:

2100 ÷ 4 = 525 (ano bissexto)
2100 ÷ 100 = 21 (não bissexto)
2100 ÷ 400 = 5,25 (não bissexto)

Aviso

Seu retorno deve ser um booleano e corresponder exatamente ao formato de saída do exemplo, incluindo ortografia e pontuação.

Exemplo de Entrada 1

2400

Exemplo de Retorno 1

Verdadeiro

Exemplo de Entrada 2

1989

Exemplo de Retorno 2

Falso

Como testar seu código e ver sua saída?

Os exercícios de codificação da Udemy não têm um console, portanto, você não pode usar a função input(). Você precisará chamar sua função com valores fixos no código, como:

def is_leap_year(year):
# seu código aqui

# Chame sua função com valores fixos no código
is_leap_year(2024)

'''
def is_leap_year(year):
    '''Retorna True se o ano for bissexto, caso contrário False.'''
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
# Chame sua função com valores fixos no código
print(is_leap_year(2024))  # Exemplo de teste
print(is_leap_year(1900))  # Exemplo de teste
print(is_leap_year(2000))  # Exemplo de teste
print(is_leap_year(2021))  # Exemplo de teste
print(is_leap_year(2400))  # Exemplo de teste
print(is_leap_year(1989))  # Exemplo de teste
