senha_correta = "123456"

for tentativa in range(1, 4):
    senha = input("Digite sua senha: ")
    
    if senha == senha_correta:
        print("Olá, Mariah. Seja bem-vindo ao nosso banco!")
        break
    else:
        if tentativa == 1:
            print("Senha incorreta! Você ainda tem 2 tentativas.")
        elif tentativa == 2:
            print("Senha incorreta! Você ainda tem 1 tentativa.")
        else:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")