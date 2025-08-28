# Blind Auction Project

import day10.art as art

print(art.logo)
print("Welcome to the secret auction program.")

nome = input("What is your name? ")
lance = float(input("What's your bid? $"))
mais_lance = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

leiloadores = {}
leiloadores[nome] = lance
while mais_lance == "yes":
    nome = input("What is your name? ")
    lance = float(input("What's your bid? $"))
    leiloadores[nome] = lance
    mais_lance = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
else:
    maior_lance = 0
    for leiloador in leiloadores:
        if leiloadores[leiloador] > maior_lance:
            maior_lance = leiloadores[leiloador]
            vencedor = leiloador
    print(f"The winner is {vencedor} with a bid of ${maior_lance}")
    print("Thanks for participating in the auction!")


