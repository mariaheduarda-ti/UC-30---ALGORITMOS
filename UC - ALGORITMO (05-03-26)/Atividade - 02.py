import random
numeros = [91, 34, 67, 15, 82]
print("Lista oficial: ", numeros)

# sort crescente
numeros.sort()
print("Após sort(): ", numeros)

# sort decrescente
numeros.sort(reverse=True)
print("Após sort(): ", numeros)

# embaralhar
dados = [80, 7, 10, 9, 19]
random.shuffle(dados)
print("Embaralhar: ", dados)