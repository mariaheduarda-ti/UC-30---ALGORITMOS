def controleFinanceiro(gastos, mesada):
    
    total = sum(gastos)

    if total < mesada:
        print("João economizou dinheiro.")
        print("Sobra:", mesada - total)

    elif total > mesada:
        print("João gastou mais do que tinha.")
        print("Faltou:", total - mesada)

    else:
        print("João gastou exatamente o valor da mesada.")