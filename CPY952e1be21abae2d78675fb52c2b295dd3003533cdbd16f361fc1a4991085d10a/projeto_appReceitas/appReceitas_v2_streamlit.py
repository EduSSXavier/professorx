import streamlit as st

class Ingrediente:
    def __init__(self, nome, unidade):
        self.nome = nome
        self.unidade = unidade

    def descricao(self):
        return f"{self.nome} ({self.unidade})"

class Receita:
    def __init__(self, titulo, tempo_preparo, porcoes):
        self.titulo = titulo
        self.ingredientes = []  # Lista de tuplas: [(Ingrediente, quantidade), ...]
        self.passos = []
        self.tempo_preparo = tempo_preparo
        self.porcoes = porcoes

    def adicionar_ingrediente(self, ingrediente, quantidade):
        self.ingredientes.append((ingrediente, quantidade))

    def remover_ingrediente(self, index):
        if 0 <= index < len(self.ingredientes):
            del self.ingredientes[index]

    def atualizar_quantidade_ingrediente(self, index, nova_quantidade):
        if 0 <= index < len(self.ingredientes):
            ing, _ = self.ingredientes[index]
            self.ingredientes[index] = (ing, nova_quantidade)

    def adicionar_passo(self, passo):
        self.passos.append(passo)

    def remover_passo(self, index):
        if 0 <= index < len(self.passos):
            del self.passos[index]

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

    def criar_receita(self, titulo, tempo_preparo, porcoes):
        receita = Receita(titulo, tempo_preparo, porcoes)
        id_receita = self.proximo_id_receita
        self.receitas[id_receita] = receita
        self.proximo_id_receita += 1
        return id_receita

    def ler_receita(self, id):
        return self.receitas.get(id, None)

    def apagar_receita(self, id):
        if id in self.receitas:
            del self.receitas[id]
            return True
        return False

    def criar_ingrediente(self, nome, unidade):
        ingrediente = Ingrediente(nome, unidade)
        id_ingrediente = self.proximo_id_ingrediente
        self.ingredientes[id_ingrediente] = ingrediente
        self.proximo_id_ingrediente += 1
        return id_ingrediente

    def ler_ingrediente(self, id):
        return self.ingredientes.get(id, None)

    def apagar_ingrediente(self, id):
        if id in self.ingredientes:
            ingrediente = self.ingredientes.pop(id)
            for receita in self.receitas.values():
                receita.ingredientes = [(ing, qtd) for ing, qtd in receita.ingredientes if ing != ingrediente]
            return True
        return False

    def buscar_receitas_por_nome(self, nome_receita):
        return [receita for receita in self.receitas.values() if nome_receita.lower() in receita.titulo.lower()]

    def buscar_receitas_por_ingrediente(self, nome_ingrediente):
        return [receita for receita in self.receitas.values() if any(nome_ingrediente.lower() in ing.nome.lower() for ing, _ in receita.ingredientes)]

# Interface com Streamlit
st.title("Gerenciador de Receitas Culinárias")

if 'gerenciador' not in st.session_state:
    st.session_state.gerenciador = GerenciadorCozinha()

gerenciador = st.session_state.gerenciador

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Cadastrar Receita",
        "Visualizar Receita",
        "Editar Receita",
        "Excluir Receita",
        "Cadastrar Ingrediente",
        "Visualizar Ingrediente",
        "Editar Ingrediente",
        "Excluir Ingrediente",
        "Buscar Receitas por Nome",
        "Buscar Receitas por Ingrediente"
    ]
)

if menu == "Cadastrar Receita":
    st.header("Cadastrar Nova Receita")
    titulo = st.text_input("Título da Receita")
    tempo_preparo = st.number_input("Tempo de Preparo (minutos)", min_value=0)
    porcoes = st.number_input("Número de Porções", min_value=1)
    if st.button("Cadastrar Receita"):
        if titulo:
            id_receita = gerenciador.criar_receita(titulo, tempo_preparo, porcoes)
            st.success(f"Receita cadastrada com ID: {id_receita}. Agora você pode editá-la para adicionar ingredientes e passos.")
        else:
            st.error("O título é obrigatório.")

elif menu == "Visualizar Receita":
    st.header("Visualizar Receita")
    receitas_options = {id: rec.titulo for id, rec in gerenciador.receitas.items()}
    if receitas_options:
        selected_id = st.selectbox("Selecione a Receita", options=list(receitas_options.keys()), format_func=lambda x: receitas_options[x])
        receita = gerenciador.ler_receita(selected_id)
        if receita:
            st.text_area("Detalhes da Receita", receita.descricao(), height=400)
    else:
        st.info("Nenhuma receita cadastrada.")

elif menu == "Editar Receita":
    st.header("Editar Receita")
    receitas_options = {id: rec.titulo for id, rec in gerenciador.receitas.items()}
    if receitas_options:
        selected_id = st.selectbox("Selecione a Receita para Editar", options=list(receitas_options.keys()), format_func=lambda x: receitas_options[x])
        receita = gerenciador.ler_receita(selected_id)
        if receita:
            novo_titulo = st.text_input("Título", value=receita.titulo)
            novo_tempo = st.number_input("Tempo de Preparo (minutos)", min_value=0, value=receita.tempo_preparo)
            novo_porcoes = st.number_input("Número de Porções", min_value=1, value=receita.porcoes)
            if st.button("Atualizar Informações Básicas"):
                receita.titulo = novo_titulo
                receita.tempo_preparo = novo_tempo
                receita.porcoes = novo_porcoes
                st.success("Informações atualizadas.")

            st.subheader("Ingredientes")
            for i, (ing, qtd) in enumerate(receita.ingredientes):
                col1, col2, col3 = st.columns([3, 1, 1])
                col1.write(ing.descricao())
                nova_qtd = col2.number_input(f"Qtd {i}", min_value=0.0, value=qtd, key=f"qtd_{selected_id}_{i}")
                if col3.button("Remover", key=f"rem_ing_{selected_id}_{i}"):
                    receita.remover_ingrediente(i)
                    st.experimental_rerun()
                if nova_qtd != qtd:
                    receita.atualizar_quantidade_ingrediente(i, nova_qtd)

            st.subheader("Adicionar Ingrediente")
            ingredientes_options = {id: ing.descricao() for id, ing in gerenciador.ingredientes.items()}
            novo_ing_op = st.radio("Ingrediente", options=["Existente", "Novo"])
            if novo_ing_op == "Novo":
                novo_nome = st.text_input("Nome do Novo Ingrediente")
                nova_unidade = st.text_input("Unidade de Medida")
                nova_qtd = st.number_input("Quantidade", min_value=0.0)
                if st.button("Adicionar Novo Ingrediente"):
                    if novo_nome and nova_unidade:
                        id_ing = gerenciador.criar_ingrediente(novo_nome, nova_unidade)
                        ing = gerenciador.ler_ingrediente(id_ing)
                        receita.adicionar_ingrediente(ing, nova_qtd)
                        st.success("Ingrediente adicionado.")
                        st.experimental_rerun()
            else:
                if ingredientes_options:
                    selected_ing_id = st.selectbox("Selecione o Ingrediente", options=list(ingredientes_options.keys()), format_func=lambda x: ingredientes_options[x])
                    nova_qtd = st.number_input("Quantidade", min_value=0.0)
                    if st.button("Adicionar Ingrediente Existente"):
                        ing = gerenciador.ler_ingrediente(selected_ing_id)
                        if ing:
                            receita.adicionar_ingrediente(ing, nova_qtd)
                            st.success("Ingrediente adicionado.")
                            st.experimental_rerun()
                else:
                    st.info("Nenhum ingrediente cadastrado. Crie um novo.")

            st.subheader("Passos")
            for i, passo in enumerate(receita.passos):
                col1, col2 = st.columns([4, 1])
                novo_passo = col1.text_input(f"Passo {i+1}", value=passo, key=f"passo_{selected_id}_{i}")
                if col2.button("Remover", key=f"rem_passo_{selected_id}_{i}"):
                    receita.remover_passo(i)
                    st.experimental_rerun()
                if novo_passo != passo:
                    receita.passos[i] = novo_passo

            st.subheader("Adicionar Passo")
            novo_passo = st.text_input("Novo Passo")
            if st.button("Adicionar Passo"):
                if novo_passo:
                    receita.adicionar_passo(novo_passo)
                    st.success("Passo adicionado.")
                    st.experimental_rerun()
    else:
        st.info("Nenhuma receita cadastrada.")

elif menu == "Excluir Receita":
    st.header("Excluir Receita")
    receitas_options = {id: rec.titulo for id, rec in gerenciador.receitas.items()}
    if receitas_options:
        selected_id = st.selectbox("Selecione a Receita para Excluir", options=list(receitas_options.keys()), format_func=lambda x: receitas_options[x])
        if st.button("Excluir"):
            if gerenciador.apagar_receita(selected_id):
                st.success("Receita excluída com sucesso.")
                st.experimental_rerun()
            else:
                st.error("Erro ao excluir.")
    else:
        st.info("Nenhuma receita cadastrada.")

elif menu == "Cadastrar Ingrediente":
    st.header("Cadastrar Novo Ingrediente")
    nome = st.text_input("Nome do Ingrediente")
    unidade = st.text_input("Unidade de Medida")
    if st.button("Cadastrar Ingrediente"):
        if nome and unidade:
            id_ing = gerenciador.criar_ingrediente(nome, unidade)
            st.success(f"Ingrediente cadastrado com ID: {id_ing}")
        else:
            st.error("Nome e unidade são obrigatórios.")

elif menu == "Visualizar Ingrediente":
    st.header("Visualizar Ingrediente")
    ingredientes_options = {id: ing.descricao() for id, ing in gerenciador.ingredientes.items()}
    if ingredientes_options:
        selected_id = st.selectbox("Selecione o Ingrediente", options=list(ingredientes_options.keys()), format_func=lambda x: ingredientes_options[x])
        ing = gerenciador.ler_ingrediente(selected_id)
        if ing:
            st.write(ing.descricao())
    else:
        st.info("Nenhum ingrediente cadastrado.")

elif menu == "Editar Ingrediente":
    st.header("Editar Ingrediente")
    ingredientes_options = {id: ing.descricao() for id, ing in gerenciador.ingredientes.items()}
    if ingredientes_options:
        selected_id = st.selectbox("Selecione o Ingrediente para Editar", options=list(ingredientes_options.keys()), format_func=lambda x: ingredientes_options[x])
        ing = gerenciador.ler_ingrediente(selected_id)
        if ing:
            novo_nome = st.text_input("Nome", value=ing.nome)
            nova_unidade = st.text_input("Unidade", value=ing.unidade)
            if st.button("Atualizar Ingrediente"):
                ing.nome = novo_nome
                ing.unidade = nova_unidade
                st.success("Ingrediente atualizado.")
    else:
        st.info("Nenhum ingrediente cadastrado.")

elif menu == "Excluir Ingrediente":
    st.header("Excluir Ingrediente")
    ingredientes_options = {id: ing.descricao() for id, ing in gerenciador.ingredientes.items()}
    if ingredientes_options:
        selected_id = st.selectbox("Selecione o Ingrediente para Excluir", options=list(ingredientes_options.keys()), format_func=lambda x: ingredientes_options[x])
        if st.button("Excluir"):
            if gerenciador.apagar_ingrediente(selected_id):
                st.success("Ingrediente excluído com sucesso. Removido de todas as receitas.")
                st.experimental_rerun()
            else:
                st.error("Erro ao excluir.")
    else:
        st.info("Nenhum ingrediente cadastrado.")

elif menu == "Buscar Receitas por Nome":
    st.header("Buscar Receitas por Nome")
    termo = st.text_input("Termo de Busca")
    if termo:
        resultados = gerenciador.buscar_receitas_por_nome(termo)
        if resultados:
            for rec in resultados:
                st.text_area(rec.titulo, rec.descricao(), height=200)
        else:
            st.info("Nenhuma receita encontrada.")

elif menu == "Buscar Receitas por Ingrediente":
    st.header("Buscar Receitas por Ingrediente")
    termo = st.text_input("Nome do Ingrediente")
    if termo:
        resultados = gerenciador.buscar_receitas_por_ingrediente(termo)
        if resultados:
            for rec in resultados:
                st.text_area(rec.titulo, rec.descricao(), height=200)
        else:
            st.info("Nenhuma receita encontrada.")