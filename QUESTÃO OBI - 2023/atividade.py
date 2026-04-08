pão = int(input("Digite a quantidade de pãos vendidos: "))
doce = int(input("Digite a quantidade de doces vendidos: "))
bolo = int(input("Digite a quantidade de bolos vendidos: "))

total = pão + 2*doce + 3*bolo

if total >= 150:
    print("Quantidade de bolos vendidos: ")
elif total >= 120:
    print("Quantidades de doces vendidos: ")
elif total >= 100:
    print("Quantidades de pães vendidos: ")
else:
    print("Não merecem o prêmio =( ")
