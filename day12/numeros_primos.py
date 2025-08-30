# Verificador de números primos
num = 1

def is_prime(num):
    if num < 2:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

num = int(input("Digite um número: "))

if is_prime(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")

