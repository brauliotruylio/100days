


def calculate_love_score(name1, name2):
    nomes_combinados = (name1 + name2).lower()
    contador_true = sum(nomes_combinados.count(char) for char in "true")
    contador_love = sum(nomes_combinados.count(char) for char in "love")
    print(f"{contador_true}{contador_love}")


calculate_love_score("Braulio", "Juliana")
