# Este é um exemplo de código Python que gera um nome de banda baseado na cidade natal e no nome do animal de estimação do usuário.
# Para comentar o código, uso o símbolo # no início da linha.
# Para comentar uma linha inteira de código basta usra o atalho Ctrl + /
# Posso usar input para receber dados do usuário e concatenar strings com o operador +.
# Quando seleciono uma palavra e aperto Ctrl + D, o Python seleciona todas as ocorrências da palavra no arquivo.

print('Bem vindo ao Gerador de nomes de Bandas!')
cidade = input('Qual o nome da sua cidade natal?\n ')
pet = input('Qual o nome do seu animal de estimação?\n ')

nome_banda = cidade + ' ' + pet
print('O nome da sua banda é: ' + nome_banda)
input('Pressione Enter para sair...')
