'''Tratamento de IndexError

Problema

Temos um código com bugs. Tente executá-lo. O código travará e retornará um IndexError.

Isso ocorre porque estamos procurando na lista de frutas por um índice fora do intervalo.

Objetivo

Use o que você aprendeu sobre tratamento de exceções para evitar que o programa trave.
Se o usuário digitar algo fora do intervalo, basta imprimir a saída padrão "Torta de Frutas".

IMPORTANTE: O tratamento de exceções NÃO deve permitir que cada fruta seja impressa
quando houver uma exceção. Por exemplo, não deve imprimir Torta de Maçã, Torta de Pera e Torta de Laranja;
quando houver uma exceção, deve imprimir apenas "Torta de Frutas".

fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit pie")

make_pie(4)'''

'''KeyError Handling
We've got some buggy code, try running the code. The code will crash and give you a KeyError.
This is because some of the posts in the facebook_posts don't have any "Likes".

Objective

Use what you've learnt about exception handling to prevent the program from crashing.
'''
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes += post['Likes']
        except KeyError:
            # Se o post não tiver a chave 'Likes', simplesmente o ignoramos.
            pass
    return total_likes


total_likes = count_likes(facebook_posts)
print(f"Total de curtidas: {total_likes}")
