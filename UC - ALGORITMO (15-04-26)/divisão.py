def divisao (x, y):
    try:
        quociente = x / y
        return quociente
    except ZeroDivisionError:
        return ("Não da pra dividir por zero!")