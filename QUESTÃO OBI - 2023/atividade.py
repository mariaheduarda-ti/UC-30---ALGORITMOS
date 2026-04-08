P = int(input("Digite a pontuação P: "))
D = int(input("Digite a pontuação D: "))
B = int(input("Digite a pontuação B: "))

total = P + 2*D + 3*B

if total >= 150:
    print("Quantidade de bolos vendidos: ")
elif total >= 120:
    print("Quantidades de doces vendidos: ")
elif total >= 100:
    print("Quantidades de pães: ")
else:
    print("Não merecem o prêmio")