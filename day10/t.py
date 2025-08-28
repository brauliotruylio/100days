def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))

# O resultado é None, porque a função retorna None quando a < 40, e o print dentro do if não é executado.
