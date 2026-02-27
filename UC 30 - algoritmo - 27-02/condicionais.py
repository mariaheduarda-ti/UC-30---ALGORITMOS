nome = input("Digite seu nome: ")
if len(nome) > 20:
    print("Seu nome é grande, ele possui mais de 20 letras")
print(f"Ele possui {len/(nome)} caracteres.")


valor = int(input("Digite um número"))
if valor % 2 == 0:
    print("O número é par")
else:
    print("O valor é impar")

nota = float(input("Digite sua nota"))

if nota >= 10:
    print("Passou")
else:
    if nota == 7:
        print("Pode melhorar")
    else:
        print("Recuperação")