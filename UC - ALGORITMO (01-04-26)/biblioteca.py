# SISTEMA DE GESTÃO DE BIBLIOTECA 

# Dicionário p/ armazenar os livros
catalogo = {}

# Dicionário p/ armazenar os empréstimos ativos 
emprestimosAtivos = {}

# Lista p/ armazenar o histórico de transição 
historico = []

# Função: Adicionar livro

def adicionarLivro(codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"Erro: Livro com código {codigo} já existe")
        return False
    
    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade
    }

    print(f"Livro '{titulo}' adicionado com sucesso")
    return True

adicionarLivro("L001", "Código Limpo", "Robert Martin", 2)

#FUNÇÃO: EMPRESTAR LIVRO

def empresta_livro(codigo, nome_aluno):

    #VALIDAÇÃO 1: Livro existe no catálogo?
    if codigo not in catalogo:
        print(f"Erro: Livro com código {codigo} não encontrado!")
        return False
    
    #VALIDAÇÃO 2: Há quantidade disponível?
    if catalogo[codigo]["quantidade"] <= 0:
        print(f"Erro: '{catalogo[codigo]['titulo']}' não está disponível!")
        return False
    
    #VALIDAÇÃO 3: Aluno já pegou 2 livros?
    livros_do_aluno = conta_livros_aluno(nome_aluno)
    if livros_do_aluno >= 2:
        print(f"Erro: {nome_aluno} já pegou 2 livros (limite máximo)!")
        return False 
    
    #VALIDAÇÃO 4: Aluno já pegou este livro?
    if codigo in emprestimosAtivos and nome_aluno in emprestimosAtivos[codigo]:
        print(f"Erro: {nome_aluno} já pegou este livro!")
        return False 
    

    if codigo not in emprestimosAtivos:
        emprestimosAtivos[codigo] = []

    # Adiciona o aluno à lista de quem pegou este livro
    emprestimosAtivos[codigo].append(nome_aluno)

    # Diminui a quantidade disponível
    catalogo[codigo]["quantidade"] -= 1

        # Registra no histórico
    historico.append({
        "tipo": "emprestimo",
        "codigo": codigo,
        "titulo": catalogo[codigo]["titulo"],
        "aluno": nome_aluno
        })
        
    print(f"{nome_aluno} pegou '{catalogo[codigo]['titulo']}' com sucesso!")
    return True

# FUNÇÃO DEVOLVER LIVRO
def devolve_livro(codigo, nome_aluno):

    # Verifica se o livro está emprestado para este aluno
    if codigo not in emprestimosAtivos or nome_aluno not in emprestimosAtivos[codigo]:
        print(f"Erro: {nome_aluno} não pegou este livro!")
        return False

    # Remove o aluno da lista de quem pegou este livro
    emprestimosAtivos[codigo]["quantidade"] += 1

    # Registra no histórico
    historico.append ({
        "tipo": "devolucao",
        "codigo": codigo,
        "titulo": catalogo[codigo]["titulo"],
        "aluno": nome_aluno
    })

    print(f"{nome_aluno} devolveu '{catalogo[codigo]['titulo']}' com sucesso!")
    return True

#FUNÇÃO CONTAR LIVRO
def conta_livros_aluno(nome_aluno):

    # Começa com contador em 0
    contador = 0

    # Percorre todos os livros que estão emprestados
    for codigo, alunos in emprestimosAtivos.items():
        # Se o aluno está na lista de quem pegou este livro, incrementa
        if nome_aluno in alunos:
            contador += 1

    return contador

def lista_emprestimos():

    print("\n" + "="*60)
    print("LIVROS EMPRESTADOS NO MOMENTO")
    print("="*60)

    # Se não há empréstimos, avisa
    if not emprestimosAtivos:
        print("Nenhum livro emprestado.")
        return
    
    # Percorre cada livro que está emprestado 
    for codigo, alunos in emprestimosAtivos.items():
        titulo = catalogo[codigo]["título"]
        print(f"\n📖 {titulo} ({codigo})")

        # Mostra quem pegou cada livro
        for aluno in alunos:
            print(f"  → Emprestado para: {aluno}")


# PASSO 1: Adiciona alguns livros ao catálogo
print("\n--- Adicionado livros ao catálogo ---")
adicionarLivro("L001", "Clean Code", "Robert Martin", 2)
adicionarLivro("L002", "Python Fluente", "Luciano Ramalho", 1)
adicionarLivro("L003", "Algoritmos", "Thomas")