distancia = 450
consumo = 8
preco_litro = 5.50

litros_gastos = distancia / consumo
custo_total = litros_gastos * preco_litro

print("Distância percorrida: ", distancia, "km")
print("Consumo do carro: ", consumo, "km por litro")
print("Litros usados: ", litros_gastos)
print("Gasto com combustível: R$", custo_total)