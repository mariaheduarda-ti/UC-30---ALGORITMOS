frase = input("Digite uma frase: ")

contador = 0

for letra in frase:
    if letra in "aeiou":
        contador += 1

print("Tem", contador, "vogais")