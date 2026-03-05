import random

numeros = [100, 200, 400, 500, 300, 600]
print("Lista oficial: ", numeros)

# sort crescente
numeros.sort()
print("Após sort(): ", numeros)

# sort decrescente
numeros.sort(reverse=True)
print("Após sort(): ", numeros)

# embaralhar
dados = [100, 200, 300, 400, 500, 600]
random.shuffle(dados)
print("Embaralhar: ", dados)

