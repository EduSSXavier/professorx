# ------------------------------------------
# Projeto: Cadastro de Alunos (versão 1)
# 
# Este projeto é uma aplicação simples para 
# cadastrar alunos, Utiliza apenas estruturas 
# básicas de Python e armazena os dados em 
# uma lista onde cada elemento é um dicionário 
# contedo informações sobre um aluno.
# ------------------------------------------

# Lista para armazenar os dados dos alunos
listaAlunos = []

# menu principal com opções
while True:
    print("\n\n")
    print("===============================")
    print("Cadastro de Alunos")
    print("===============================")
    print("1. Cadastrar novo aluno")
    print("2. Consultar alunos cadastrados")
    print("3. Excluir aluno")
    print("4. Atualizar notas")
    print("5. Gerar relatório de aprovação")
    print("6. Sair")
    print("===============================")
    opcao = input("Escolha uma opção (1-6): ")
    print("===============================")

    if opcao == "1":
        # Cadastrar novo aluno
        print("\n=== INCLUSÃO DE ALUNO ===")
        matriculaAluno = input("Matricula: ")
        nomeAluno      = input("Nome     : ")
        idadeAluno     = input("Idade    : ")
        notasAuno = {'matematica': 0, 'portugues' : 0,  'ciencias'  : 0}
        # montagem do dicionario do aluno
        aluno = {
            'matricula': matriculaAluno,
            'nome'     : nomeAluno,
            'idade'    : idadeAluno,
            'notas'    : notasAuno
        }
        # inclusão do aluno na lista
        listaAlunos.append(aluno)
        print("[MENSAGEM] Aluno cadastrado com sucesso!")

    elif opcao == "2":
        # Consultar alunos cadastrados
        print("\n=== CONSULTA DE ALUNO ===")
        matriculaAluno = input("Matricula: ")
        # pesquisar aluno na lista pela matricula
        encontrado = False
        for aluno in listaAlunos:
            if aluno['matricula'] == matriculaAluno:
                encontrado = True
                print(f"Matricula: {aluno['matricula']}")
                print(f"Nome     : {aluno['nome']}")
                print(f"Idade    : {aluno['idade']}")
                print(f"Notas    : {aluno['notas']}")
                break
        if not encontrado: # nao encontrou o aluno
            print("[MENSAGEM] Aluno não encontrado!")
        print("----------------------------")
    
    elif opcao == "3":
        # Excluir aluno
        print("\n=== EXCLUSÃO DE ALUNO ===")
        matriculaAluno = input("Matricula: ")
        # pesquisar aluno na lista pela matricula
        encontrado = False
        for aluno in listaAlunos: 
            if aluno['matricula'] == matriculaAluno:
                encontrado = True
                posicao = listaAlunos.index(aluno)
                listaAlunos.pop(posicao) # remove o aluno da lista
                print("[MENSAGEM] Aluno excluído com sucesso!")
                break
        if not encontrado: # nao encontrou o aluno
            print("[MENSAGEM] Aluno não encontrado!")
        print("----------------------------")

    elif opcao == "4":
        # Atualizar notas
        print("\n=== ATUALIZAÇÃO DE NOTAS ===")
        matriculaAluno = input("Matricula: ")
        # pesquisar aluno na lista pela matricula
        encontrado = False
        for aluno in listaAlunos:
            if aluno['matricula'] == matriculaAluno:
                encontrado = True
                # solicitar novas notas
                notaMatematica = float(input("Nota Matemática: "))
                notaPortugues  = float(input("Nota Português : "))
                notaCiencias   = float(input("Nota Ciências  : "))
                # atualizar as notas do aluno
                aluno['notas']['matematica'] = notaMatematica
                aluno['notas']['portugues']  = notaPortugues
                aluno['notas']['ciencias']   = notaCiencias
                print("[MENSAGEM] Notas atualizadas com sucesso!")
                break
        if not encontrado: # nao encontrou o aluno
            print("[MENSAGEM] Aluno não encontrado!")
        print("----------------------------")

    elif opcao == "5":
        # Gerar relatório de aprovação
        print("\n=== RELATÓRIO DE APROVAÇÃO ===")
        for aluno in listaAlunos:
            notas = aluno['notas']
            media = (notas['matematica'] + notas['portugues'] + notas['ciencias']) / 3
            if media >= 7:
                status = "Aprovado"
            else:
                status = "Reprovado"
            print(f"Matricula: {aluno['matricula']} | Nome: {aluno['nome']} | Média: {media:.2f} | Status: {status}")
        print("----------------------------")
    elif opcao == "6":
        # Sair do programa
        print("[MENSAGEM] Saindo do programa...")
        break

print("[MENSAGEM] Programa encerrado.")