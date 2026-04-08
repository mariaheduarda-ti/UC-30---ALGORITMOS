p = int(input("Digite a pontuação P: "))
d = int(input("Digite a pontuação D: "))
b = int(input("Digite a pontuação B: "))

total = p + 2*d + 3*b

if total >= 150:
    print("Quantidade de bolos vendidos: ")
elif total >= 120:
    print("Quantidades de doces vendidos: ")
elif total >= 100:
    print("Quantidades de pães: ")
else:
    print("Não merecem o prêmio")
