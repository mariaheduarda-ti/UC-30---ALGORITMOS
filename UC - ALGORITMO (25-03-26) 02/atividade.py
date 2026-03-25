def calcular_estatisticas(*notas):
    if len(notas) == 0:
        print("Nenhuma nota informada.")
        return

    soma = sum(notas)
    media = soma / len(notas)
    maior = max(notas)
    menor = min(notas)

    return soma, media, maior, menor


soma, media, maior, menor = calcular_estatisticas(7, 8, 9)

print(f"Soma das notas: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior nota: {maior}")
print(f"Menor nota: {menor}")
