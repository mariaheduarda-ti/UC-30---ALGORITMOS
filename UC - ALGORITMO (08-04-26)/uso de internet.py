def usoInternet(consumo):

    total = sum(consumo)
    limite = 30

    if total <= limite:
        print("Ainda tem internet disponível.")
        print("Restam:", limite - total, "GB")

    else:
        print("Limite de internet ultrapassado.")
        print("Excedeu:", total - limite, "GB")