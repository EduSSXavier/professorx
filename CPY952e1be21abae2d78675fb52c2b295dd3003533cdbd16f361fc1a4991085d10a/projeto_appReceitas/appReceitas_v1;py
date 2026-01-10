class Ingrediente:
    def __init__(self, nome, unidade):
        self.nome = nome
        self.unidade = unidade

    def descricao(self):
        return f"{self.nome} ({self.unidade})"


class Receita:
    def __init__(self, titulo, tempo_preparo, porcoes):
        self.titulo = titulo
        self.ingredientes = []           # Lista de tuplas: [(Ingrediente, quantidade), ...]
        self.passos = []
        self.tempo_preparo = tempo_preparo
        self.porcoes = porcoes

    def adicionar_ingrediente(self, ingrediente, quantidade):
        """Adiciona um ingrediente com sua quantidade específica para esta receita"""
        self.ingredientes.append((ingrediente, quantidade))

    def adicionar_passo(self, passo):
        self.passos.append(passo)

    def descricao(self):
        desc = f"Receita: {self.titulo}\n"
        desc += f"Tempo de preparo: {self.tempo_preparo} minutos\n"
        desc += f"Porções: {self.porcoes}\n"
        desc += "Ingredientes:\n"
        for ingrediente, qtd in self.ingredientes:
            desc += f"- {qtd} {ingrediente.unidade} de {ingrediente.nome}\n"
        desc += "Passos:\n"
        for i, passo in enumerate(self.passos, 1):
            desc += f"{i}. {passo}\n"
        return desc


class GerenciadorCozinha:
    def __init__(self):
        self.receitas = {}
        self.ingredientes = {}
        self.proximo_id_receita = 1
        self.proximo_id_ingrediente = 1
        self.menu_principal()

    def criar_receita(self, titulo, tempo_preparo, porcoes):
        receita = Receita(titulo, tempo_preparo, porcoes)
        id_receita = self.proximo_id_receita
        self.receitas[id_receita] = receita
        self.proximo_id_receita += 1
        return id_receita

    def ler_receita(self, id_receita):
        return self.receitas.get(id_receita)

    def apagar_receita(self, id_receita):
        return self.receitas.pop(id_receita, None) is not None

    def criar_ingrediente(self, nome, unidade):
        ingrediente = Ingrediente(nome, unidade)
        id_ing = self.proximo_id_ingrediente
        self.ingredientes[id_ing] = ingrediente
        self.proximo_id_ingrediente += 1
        return id_ing

    def ler_ingrediente(self, id_ing):
        return self.ingredientes.get(id_ing)

    def apagar_ingrediente(self, id_ing):
        if id_ing not in self.ingredientes:
            return False
            
        ingrediente = self.ingredientes.pop(id_ing)
        
        # Remove referências desse ingrediente de todas as receitas
        for receita in self.receitas.values():
            receita.ingredientes = [
                (ing, qtd) for ing, qtd in receita.ingredientes
                if ing != ingrediente
            ]
        return True

    def buscar_receitas_por_nome(self, termo):
        termo = termo.lower()
        return [r for r in self.receitas.values() if termo in r.titulo.lower()]

    def buscar_receitas_por_ingrediente(self, termo):
        termo = termo.lower()
        return [
            receita for receita in self.receitas.values()
            if any(termo in ing.nome.lower() for ing, _ in receita.ingredientes)
        ]

    # ================== Interface do Usuário ==================

    def menu_principal(self):
        while True:
            print("\n=== Gerenciador de Receitas ===")
            print("1.  Cadastrar nova receita")
            print("2.  Visualizar receita")
            print("3.  Editar receita")
            print("4.  Excluir receita")
            print("5.  Cadastrar ingrediente")
            print("6.  Visualizar ingrediente")
            print("7.  Excluir ingrediente")
            print("8.  Listar receitas")
            print("9.  Buscar receitas por nome")
            print("10. Buscar receitas por ingrediente")
            print("0.  Sair")
            
            op = input("\nOpção → ").strip()
            
            if op == '1':
                self.cadastrar_receita()
            elif op == '2':
                self.visualizar_receita()
            elif op == '3':
                self.editar_receita()
            elif op == '4':
                self.excluir_receita()
            elif op == '5':
                self.cadastrar_ingrediente()
            elif op == '6':
                self.visualizar_ingrediente()
            elif op == '7':
                self.excluir_ingrediente()
            elif op == '8':
                self.listar_receitas()
            elif op == '9':
                self.buscar_por_nome()
            elif op == '10':
                self.buscar_por_ingrediente()
            elif op == '0':
                print("Até logo!\n")
                break
            else:
                print("Opção inválida.")

    def cadastrar_receita(self):
        titulo = input("Título da receita: ").strip()
        tempo = int(input("Tempo de preparo (min): "))
        porcoes = int(input("Rendimento (porções): "))
        
        id_rec = self.criar_receita(titulo, tempo, porcoes)
        receita = self.ler_receita(id_rec)

        print("\nAdicionando ingredientes...")
        while True:
            resp = input("Adicionar ingrediente? (s/n): ").lower()
            if resp != 's':
                break
                
            print("\nIngredientes cadastrados:")
            for iid, ing in self.ingredientes.items():
                print(f"{iid:3d} - {ing.descricao()}")
                
            escolha = input("\nDigite o ID do ingrediente (ou 0 para novo): ")
            if escolha == '0':
                nome = input("Nome do ingrediente: ").strip()
                unidade = input("Unidade de medida (ex: xícara, colher, g, ml): ").strip()
                iid = self.criar_ingrediente(nome, unidade)
            else:
                try:
                    iid = int(escolha)
                except ValueError:
                    print("ID inválido!")
                    continue
                    
            ingrediente = self.ler_ingrediente(iid)
            if not ingrediente:
                print("Ingrediente não encontrado!")
                continue
                
            qtd = float(input(f"Quantidade de {ingrediente.nome}: "))
            receita.adicionar_ingrediente(ingrediente, qtd)

        print("\nAdicionando passos...")
        i = 1
        while True:
            passo = input(f"Passo {i} (Enter vazio para terminar): ").strip()
            if not passo:
                break
            receita.adicionar_passo(passo)
            i += 1

        print(f"\nReceita cadastrada com sucesso! ID: {id_rec}")

    def visualizar_receita(self):
        try:
            iid = int(input("ID da receita: "))
            rec = self.ler_receita(iid)
            if rec:
                print("\n" + "="*60)
                print(rec.descricao())
                print("="*60)
            else:
                print("Receita não encontrada.")
        except ValueError:
            print("ID inválido.")

    def editar_receita(self):
        id_receita = int(input("ID da receita: "))
        receita = self.ler_receita(id_receita)
        if not receita:
            print("Receita não encontrada!")
            return

        while True:
            print("\nEditar Receita:")
            print("1. Alterar Título")
            print("2. Alterar Tempo de Preparo")
            print("3. Alterar Porções")
            print("4. Adicionar Ingrediente")
            print("5. Remover Ingrediente")
            print("6. Adicionar Passo")
            print("7. Remover Passo")
            print("8. Voltar")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                receita.titulo = input("Novo título: ")
            elif opcao == '2':
                receita.tempo_preparo = int(input("Novo tempo de preparo: "))
            elif opcao == '3':
                receita.porcoes = int(input("Novo número de porções: "))
            elif opcao == '4':
                print("Ingredientes disponíveis:")
                for id_ing, ing in self.ingredientes.items():
                    print(f"{id_ing}: {ing.descricao()}")
                id_ing = int(input("ID do ingrediente (ou 0 para novo): "))
                if id_ing == 0:
                    nome = input("Nome do ingrediente: ")
                    quantidade = float(input("Quantidade: "))
                    unidade = input("Unidade: ")
                    id_ing = self.criar_ingrediente(nome,unidade)
                ingrediente = self.ler_ingrediente(id_ing)
                if ingrediente:
                    receita.adicionar_ingrediente(ingrediente, quantidade)
            elif opcao == '5':
                print("Ingredientes atuais:")
                for i, ing in enumerate(receita.ingredientes, 1):
                    desc, unidade = ing[0]
                    quantidade = ing[1]
                    print(f"{i}: {desc} ({quantidade} {unidade})")
                idx = int(input("Número do ingrediente a remover: ")) - 1
                if 0 <= idx < len(receita.ingredientes):
                    del receita.ingredientes[idx]
            elif opcao == '6':
                passo = input("Novo passo: ")
                receita.adicionar_passo(passo)
            elif opcao == '7':
                print("Passos atuais:")
                for i, passo in enumerate(receita.passos, 1):
                    print(f"{i}: {passo}")
                idx = int(input("Número do passo a remover: ")) - 1
                if 0 <= idx < len(receita.passos):
                    del receita.passos[idx]
            elif opcao == '8':
                break
            else:
                print("Opção inválida!")
    
    def excluir_receita(self):
        try:
            iid = int(input("ID da receita a excluir: "))
            if self.apagar_receita(iid):
                print("Receita excluída com sucesso.")
            else:
                print("Receita não encontrada.")
        except ValueError:
            print("ID inválido.")
            
    def cadastrar_ingrediente(self):
        nome = input("Nome do ingrediente: ").strip()
        unidade = input("Unidade de medida (ex: xícara, colher, g, ml): ").strip()
        id_ing = self.criar_ingrediente(nome, unidade)
        print(f"Ingrediente cadastrado com sucesso! ID: {id_ing}")

    def visualizar_ingrediente(self):
        try:
            iid = int(input("ID do ingrediente: "))
            ing = self.ler_ingrediente(iid)
            if ing:
                print("\n" + "="*40)
                print(ing.descricao())
                print("="*40)
            else:
                print("Ingrediente não encontrado.")
        except ValueError:
            print("ID inválido.")

    def excluir_ingrediente(self):
        try:
            iid = int(input("ID do ingrediente a excluir: "))
            if self.apagar_ingrediente(iid):
                print("Ingrediente excluído com sucesso.")
            else:
                print("Ingrediente não encontrado.")
        except ValueError:
            print("ID inválido.")

    def buscar_por_nome(self):
        termo = input("Termo de busca: ").strip()
        resultados = self.buscar_receitas_por_nome(termo)
        if resultados:
            print(f"\nReceitas encontradas ({len(resultados)}):")
            for rec in resultados:
                print(f"- {rec.titulo}")
        else:
            print("Nenhuma receita encontrada.")

    def buscar_por_ingrediente(self):
        termo = input("Termo de busca: ").strip()
        resultados = self.buscar_receitas_por_ingrediente(termo)
        if resultados:
            print(f"\nReceitas encontradas ({len(resultados)}):")
            for rec in resultados:
                print(f"- {rec.titulo}")
        else:
            print("Nenhuma receita encontrada.")

    def listar_receitas(self):
        print("\nReceitas cadastradas:")
        for rec in self.receitas.values():
            print(f"- {rec.titulo}")



if __name__ == "__main__":
    GerenciadorCozinha()