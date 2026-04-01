# estruturas do sistema
catalogo = {}
emprestimosAtivos = {}
historico = []

# Função de empréstimo
def emprestarLivro(codigo, usuario):

    if codigo not in catalogo:
        print("Erro: livro não encontrado.")
        return

    if catalogo[codigo]["quantidade"] <= 0:
        print("Erro: não há exemplares disponíveis.")
        return

    emprestimosAtivos[codigo] = usuario
    catalogo[codigo]["quantidade"] -= 1
    historico.append(usuario + " pegou o livro " + catalogo[codigo]["titulo"])

    print("Empréstimo realizado com sucesso.")