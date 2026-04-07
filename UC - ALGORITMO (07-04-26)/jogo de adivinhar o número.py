import random

numero = random.randint(1, 100)
tentativas = 0
palpite = 0

while palpite != numero:
    palpite = int(input("Tente adivinhar o número (1 a 100): "))
    tentativas += 1

    if palpite < numero:
        print("Maior")
    elif palpite > numero:
        print("Menor")

print("Parabéns! Você acertou.")
print("Tentativas:", tentativas)