# ---------------------------------------
# Projeto: Gerenciador de Tarefas
# Autor: Professor Xavier
# ---------------------------------------

# Dados --------------------------------
listaTarefas = []

# Cada tarefa será armazenada em uma lista
# contendo [descrição, situação], ou seja,
# uma lista de listas.
#    listaTarefas = [
#        ["Comprar leite", "pendente"],
#        ["Estudar para a prova", "concluída"]
#    ]
# ---------------------------------------


# Menu Principal ------------------------
while True:
    print("""\n\n
          --- Gerenciador de Tarefas ---
          1. Adicionar Nova Tarefa
          2. Excluir Tarefa
          3. Alterar situação da Tarefa
          4. Listar Tarefas
          5. Sair
          -------------------------------
          """)
    
    opcao = input("Escolha uma opção: ")

    if opcao == "5":
        print("[MSG] Saindo do gerenciador de tarefas...")
        break
    elif opcao == "1":
        # Adicionar Tarefa
        descricaoTarefa = input("Descrição da tarefa: ")
        # Toda tarefa criada inicia com a situação "pendente"
        listaTarefas.append([descricaoTarefa, "pendente"])
        print(f"[MSG] Tarefa '{len(listaTarefas)}' adicionada com sucesso!")
    elif opcao == "2":
        # Excluir Tarefa
        if not listaTarefas:
            print("[MSG] Nenhuma tarefa cadastrada.")
        else:
            # Exibir tarefas cadastradas
            print("\nTarefas Cadastradas:")
            for i in range(len(listaTarefas)):
                desc     = listaTarefas[i][0] #Extrai descrição da tarefa
                situacao = listaTarefas[i][1] #Extrai situação da tarefa
                print(f"{i + 1}. {desc} - {situacao}")
            # solicitar tarefa que será excluída
            numero = int(input("Número da tarefa a ser excluída: ")) - 1
            if 0 <= numero < len(listaTarefas):
                listaTarefas.pop(numero)
                print(f"[MSG] Tarefa {numero + 1} excluída com sucesso!")
            else:
                print("[MSG] Número de tarefa inválido.")
    elif opcao == "3":
        # Alterar Situação da Tarefa        
        if not listaTarefas:
            print("[MSG] Nenhuma tarefa cadastrada.")
        else:
            # Exibir tarefas cadastradas
            print("\nTarefas Cadastradas:")
            for i in range(len(listaTarefas)):
                desc     = listaTarefas[i][0] #Extrai descrição da tarefa
                situacao = listaTarefas[i][1] #Extrai situação da tarefa
                print(f"{i + 1}. {desc} - {situacao}")
            # solicitar tarefa que terá a situação alterada
            numero = int(input("Número da tarefa a ter a situação alterada: ")) - 1
            if 0 <= numero < len(listaTarefas):
                nova_situacao = input("Nova situação (pendente/concluída): ")
                if nova_situacao in ["pendente", "concluída"]:
                    listaTarefas[numero][1] = nova_situacao
                    print(f"[MSG] Situação da tarefa {numero + 1} alterada para '{nova_situacao}' com sucesso!")
                else:
                    print("[MSG] Situação inválida. Use 'pendente' ou 'concluída'.")
            else:
                print("[MSG] Número de tarefa inválido.")
    elif opcao == "4":
        # Listar Tarefas
        if not listaTarefas:
            print("[MSG] Nenhuma tarefa cadastrada.")
        else:
            print("\nTarefas Cadastradas:")
            for i in range(len(listaTarefas)):
                desc     = listaTarefas[i][0] #Extrai descrição da tarefa
                situacao = listaTarefas[i][1] #Extrai situação da tarefa
                print(f"{i + 1}. {desc} - {situacao}")
    else:
        print("Opção inválida. Tente novamente.")
# ---------------------------------------