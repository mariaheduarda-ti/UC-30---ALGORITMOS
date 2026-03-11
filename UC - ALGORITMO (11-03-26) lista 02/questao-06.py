idade = int(input("Idade: "))

if idade < 12:
    print("Categoria: Infantil")
elif idade < 18:
    print("Categoria: Juvenil")
elif idade < 60:
    print("Categoria: Adulto")
else:
    print("Categoria: Senior")

print("Bem-vindo à competição!")