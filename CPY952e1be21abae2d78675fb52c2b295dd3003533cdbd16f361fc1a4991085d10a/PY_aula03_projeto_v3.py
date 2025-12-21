# ------------------------------------------
# Projeto: Cadastro de Alunos (versão 2)
# 
# Este projeto é uma atualização da versão 3 
# da aplicação para cadastrar alunos, 
# Ele faz uso de funções mais avançadaso.
# ------------------------------------------
from functools import reduce

# Lista para armazenar os dados dos alunos
listaAlunos = []

# Função para incluir um novo aluno
def incluir_aluno(matriculaAluno,nomeAluno, idadeAluno):
    notasAluno = {'matematica': 0, 'portugues' : 0,  'ciencias'  : 0}
    # montagem do dicionario do aluno
    aluno = {
        'matricula': matriculaAluno,
        'nome'     : nomeAluno,
        'idade'    : idadeAluno,
        'notas'    : notasAluno
    }
    # inclusão do aluno na lista
    listaAlunos.append(aluno)

# Função para consultar alunos cadastrados
def consultar_alunos(matriculaAluno): 
    # pesquisar aluno na lista pela matricula
    resultadoPesquisa = filter(
        lambda aluno:aluno if aluno['matricula'] == matriculaAluno else False, 
        listaAlunos)
    return resultadoPesquisa

# Função para excluir um aluno
def excluir_aluno(matriculaAluno):
    # pesquisar aluno na lista 
    aluno = consultar_alunos(matriculaAluno)
    if aluno:
        posicao = listaAlunos.index(aluno)
        listaAlunos.pop(posicao) # remove o aluno da lista
        return True
    return False

# Função para atualizar notas
def atualizar_notas(matriculaAluno, notaMatematica, notaPortugues, notaCiencias):
    # pesquisar aluno na lista pela matricula
    aluno = consultar_alunos(matriculaAluno)
    if aluno:
        # atualizar as notas do aluno
        aluno['notas']['matematica'] = notaMatematica
        aluno['notas']['portugues']  = notaPortugues
        aluno['notas']['ciencias']   = notaCiencias
        return True
    return False

# Função para gerar relatório de aprovação
def gerar_relatorio():
    for aluno in listaAlunos:
        media = reduce(lambda soma, nota: soma+nota, aluno['notas'].values())/3
        status = "Aprovado" if media >= 7 else "Reprovado"
        print(f"Matricula: {aluno['matricula']:5} | Nome: {aluno['nome']:20} | Média: {media:2.2f} | Status: {status}")


# menu principal com opções
while True:
    print("""
          \n\n)
          ===============================
          Cadastro de Alunos
          ===============================
          1. Cadastrar novo aluno
          2. Consultar alunos cadastrados
          3. Excluir aluno
          4. Atualizar notas
          5. Gerar relatório de aprovação
          6. Sair
          ===============================
          """)
    opcao = input("Escolha uma opção (1-6): ")
    print("===============================")

    if opcao == "1":
        # Cadastrar novo aluno
        print("\n=== INCLUSÃO DE ALUNO ===")
        matriculaAluno = input("Matricula: ")
        nomeAluno      = input("Nome     : ")
        idadeAluno     = input("Idade    : ")
        # chamando função de inclusão
        incluir_aluno(matriculaAluno,nomeAluno, idadeAluno)
        print("[MENSAGEM] Aluno cadastrado com sucesso!")

    elif opcao == "2":
        # Consultar alunos cadastrados
        print("\n=== CONSULTA DE ALUNO ===")
        matriculaAluno = input("Matricula: ")
        # chamando a funcao de consulta
        aluno = consultar_alunos(matriculaAluno)
        if aluno:
            print(f"Nome     : {aluno['nome']}")
            print(f"Idade    : {aluno['idade']}")
            print(f"Notas    : {aluno['notas']}")
        else:
            print("[MENSAGEM] Aluno nao encontrado!")
        print("----------------------------")
    
    elif opcao == "3":
        # Excluir aluno
        print("\n=== EXCLUSÃO DE ALUNO ===")
        matriculaAluno = input("Matricula: ")
        # chamando a funcao de exclusao
        if excluir_aluno(matriculaAluno):
            print("[MENSAGEM] Aluno excluído com sucesso!")
        else:
            print("[MENSAGEM] Aluno nao encontrado!")
        print("----------------------------")

    elif opcao == "4":
        # Atualizar notas
        print("\n=== ATUALIZAÇÃO DE NOTAS ===")
        matriculaAluno = input("Matricula: ")
        # solicitar novas notas
        notaMatematica = float(input("Nota Matemática: "))
        notaPortugues  = float(input("Nota Português : "))
        notaCiencias   = float(input("Nota Ciências  : "))
        # altera as otas do aluno
        if atualizar_notas(matriculaAluno, notaMatematica, notaPortugues, notaCiencias):
            print("[MENSAGEM] Notas atualizadas com sucesso!")
        else:
            print("[MENSAGEM] Aluno não encontrado!")
        print("----------------------------")

    elif opcao == "5":
        # Gerar relatório de aprovação
        print("\n=== RELATÓRIO DE APROVAÇÃO ===")
        gerar_relatorio()
        print("----------------------------")
    elif opcao == "6":
        # Sair do programa
        print("[MENSAGEM] Saindo do programa...")
        break

print("[MENSAGEM] Programa encerrado.")