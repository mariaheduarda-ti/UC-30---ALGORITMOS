numeros = []

for i in range(8):
    n = int(input("Digite um número: "))
    numeros.append(n)

for numero in numeros:
    quantidade = numeros.count(numero)

    if quantidade > 1:
        print(numero, "apareceu", quantidade, "vezes")