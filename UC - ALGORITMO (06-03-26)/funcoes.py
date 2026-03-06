notas = [7.5, 8.0, 9.5, 6.0, 8.5]
print("Notas: ", notas)

print("Menor nota: ", min(notas))
print("Maior nota: ", max(notas))
print("Soma: ", sum(notas))
print("Média: ", sum(notas) / len(notas))


nomes = ["Adriana", "Bárbara", "Carla", "Daniel"]

print("Usando FOR simples:") # apenas elementos

for nome in nomes:
    print(f"Olá, {nome}")

print("Usando enumerate: ") # indice e elementos

for indice, nome in enumerate(nomes):
    print(f"Posição {indice}: {nome}")


original = ["A", "B", "C"]
copia = list(original)

print("Original: ", original)
print("Cópia: ", copia)
print("São iguais: ", original == copia)

copia.append("D")
print("Original: ", original)
print("Cópia: ", copia)
print("São iguais: ", original == copia)



