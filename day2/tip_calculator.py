
print("Bem vindo ao Calculador de Gorjetas!")
print("Vamos calcular a gorjeta com base no valor da conta, a porcentagem de gorjeta e o número de pessoas.")

total = float(input("Qual é o valor total da conta? R$ "))
gorjeta_percentagem = float(input("Qual é a porcentagem de gorjeta? (ex: 10, 12, 15) "))
pessoas = int(input("Quantas pessoas vão dividir a conta? "))
gorjeta = (total * gorjeta_percentagem) / 100
total_com_gorjeta = total + gorjeta
valor_por_pessoa = total_com_gorjeta / pessoas

print(f"\nTotal da conta: R$ {total:.2f}")
print(f"Gorjeta: R$ {gorjeta:.2f} ({gorjeta_percentagem}%)")
print(f"Total com gorjeta: R$ {total_com_gorjeta:.2f}")
print(f"Valor por pessoa: R$ {valor_por_pessoa:.2f}")
print("Obrigado por usar o Calculador de Gorjetas!")
