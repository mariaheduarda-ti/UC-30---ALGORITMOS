def calcular_media():
    notas = []

    for i in range(3):
        try:
            nota = float(input(f"Digite a {i+1}ª nota: "))
            notas.append(nota)
        except ValueError:
            print("Erro: as notas devem ser numéricas.")
            return  # encerra a função

    media = sum(notas) / 3
    print(f"Média final: {media:.2f}")