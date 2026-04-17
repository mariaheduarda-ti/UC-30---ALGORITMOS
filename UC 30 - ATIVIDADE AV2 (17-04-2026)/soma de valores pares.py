numeros = [10, 15, 20, 25, 30]

soma = 0

for n in numeros:
    if n % 2 == 0:
        soma = soma + n

print("Soma dos pares:", soma)