def soma_segura (a, b):
    try:
        soma = a + b
        return soma
    except TypeError:
        print ("Entrada inválida!")
        return 0