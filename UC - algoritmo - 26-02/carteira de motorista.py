# Programa 3

resposta = input("Você tem carteira de motorista? (S/N): ")

if resposta == "S" or resposta == "s":
    carteira = True
else:
    carteira = False

print("Valor booleano:", carteira)
print("Tipo:", type(carteira))