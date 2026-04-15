def calcular_total():
    try:
        preco1 = float(input("Digite o preço do  produto: "))
        preco2 = float(input("Digite o preço do segundoproduto: "))
    except ValueError:
        print("Erro: os preços devem ser numéricos.")
        return  

    total = preco1 + preco2
    print(f"Valor total da compra: R$ {total:.2f}")