valor = float(input("Digite o valor da compra: "))

if valor > 500:
    valor = valor * 0.8
elif valor >= 200:
    valor = valor * 0.9

print("Valor final:", valor)