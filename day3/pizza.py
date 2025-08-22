# Calcule quanto eles precisam pagar com base no tamanho escolhido.

# Calcule quanto adicionar à conta com base na escolha de pepperoni.

# Calcule o valor final com base na preferência de queijo extra.

print("Bem-vindo à Pizzaria Python!")
tamanho = input("Escolha o tamanho da pizza (P, M, G): ").strip().upper()
pepperoni = input("Deseja adicionar pepperoni? (S/N): ").strip().upper()
queijo_extra = input("Deseja adicionar queijo extra? (S/N): ").strip().upper()

conta = 0
if tamanho == 'P':
    conta += 15
elif tamanho == 'M':
    conta += 20
elif tamanho == 'G':
    conta += 25
else:
    print("Tamanho inválido. Por favor, escolha P, M ou G.")


if pepperoni == 'S':
    if tamanho == 'P':
        conta += 2
    elif tamanho == 'M':
        conta += 3
    elif tamanho == 'G':
        conta += 4

if queijo_extra == 'S':
    conta += 1

print(f"O valor total da sua pizza é: R$ {conta:.2f}")
# day3/pizza.py
