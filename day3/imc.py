print("bem vindo a Calculadora de IMC!")

peso = int(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print("Você é um pau de virar tripa.")

elif imc < 25 and imc >= 18.5:
    print("Você está no peso ideal.")

elif imc < 30 and imc >= 25:
    print("Você está acima do peso ideal.")
else:
    print("Você é enorme!")
