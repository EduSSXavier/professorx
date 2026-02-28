import streamlit as st
import pandas as pd
import database

# ==================== CONFIGURAÇÃO DA PÁGINA ====================
st.set_page_config(
    page_title="Sistema Escolar",
    page_icon="🏫",
    layout="wide"
)

# Estilo CSS customizado
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
    }
    .success-msg {
        padding: 10px;
        background-color: #d4edda;
        color: #155724;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    .error-msg {
        padding: 10px;
        background-color: #f8d7da;
        color: #721c24;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ==================== FUNÇÕES AUXILIARES ====================

def mostrar_mensagem(tipo, mensagem):
    """Exibe mensagem de sucesso ou erro."""
    if tipo == "sucesso":
        st.markdown(f'<div class="success-msg">✅ {mensagem}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="error-msg">❌ {mensagem}</div>', unsafe_allow_html=True)

def carregar_turmas():
    """Carrega turmas para um SelectBox."""
    turmas = database.listar_turmas()
    options = {"Nenhuma": None}
    for t in turmas:
        options[f"{t['nome']} ({t['ano_letivo']})"] = t['id']
    return options

# ==================== ABA: CADASTRO ====================

def aba_cadastro():
    st.header("📝 Cadastro de Alunos")
    
    with st.form("form_cadastro"):
        col1, col2 = st.columns(2)
        
        with col1:
            nome = st.text_input("Nome Completo", placeholder="João da Silva")
            data_nasc = st.date_input("Data de Nascimento")
            cpf = st.text_input("CPF", placeholder="123.456.789-00")
        
        with col2:
            email = st.text_input("Email", placeholder="joao@email.com")
            turmas = carregar_turmas()
            turma_selecionada = st.selectbox("Turma (Opcional)", 
                                              options=list(turmas.keys()))
        
        submit = st.form_submit_button("💾 Cadastrar Aluno")
        
        if submit:
            if nome and cpf:
                sucesso, msg = database.adicionar_aluno(
                    nome, 
                    str(data_nasc), 
                    cpf, 
                    email,
                    turmas[turma_selecionada]
                )
                if sucesso:
                    mostrar_mensagem("sucesso", msg)
                    st.rerun()
                else:
                    mostrar_mensagem("erro", msg)
            else:
                mostrar_mensagem("erro", "Preencha os campos obrigatórios!")

# ==================== ABA: CONSULTA ====================

def aba_consulta():
    st.header("🔍 Consulta de Alunos")
    
    # Filtros
    col1, col2 = st.columns(2)
    with col1:
        filtro_nome = st.text_input("Buscar por nome")
    with col2:
        turmas = carregar_turmas()
        filtro_turma = st.selectbox("Filtrar por turma", 
                                     options=["Todas"] + list(turmas.keys()))
    
    # Busca dados
    id_turma_filtro = turmas.get(filtro_turma) if filtro_turma != "Todas" else None
    alunos = database.buscar_alunos(filtro_nome, id_turma_filtro)
    
    if alunos:
        # Converte para DataFrame para melhor visualização
        df = pd.DataFrame(alunos, columns=[
            'ID', 'Nome', 'Data Nasc', 'CPF', 'Email', 'Turma', 'Ano Letivo'
        ])
        
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )
        
        st.write(f"**Total de registros encontrados: {len(alunos)}**")
    else:
        st.info("Nenhum aluno encontrado com os filtros selecionados.")

# ==================== ABA: EDIÇÃO ====================

def aba_edicao():
    st.header("✏️ Editar Dados do Aluno")
    
    # Seleção do aluno
    alunos = database.buscar_alunos()
    if not alunos:
        st.info("Nenhum aluno cadastrado.")
        return
    
    # Cria dicionário para seleção
    opcoes = {f"{a['nome']} (CPF: {a['cpf']})": a['id'] for a in alunos}
    aluno_selecionado = st.selectbox("Selecione o aluno para editar", 
                                      options=list(opcoes.keys()))
    
    if aluno_selecionado:
        aluno_id = opcoes[aluno_selecionado]
        dados_aluno = database.buscar_aluno_por_id(aluno_id)
        
        st.divider()
        
        with st.form("form_edicao"):
            col1, col2 = st.columns(2)
            
            with col1:
                novo_nome = st.text_input("Nome", value=dados_aluno['nome'])
                nova_data = st.date_input("Data Nasc", 
                                          value=pd.to_datetime(dados_aluno['data_nascimento']))
                novo_cpf = st.text_input("CPF", value=dados_aluno['cpf'])
            
            with col2:
                novo_email = st.text_input("Email", value=dados_aluno['email'] or "")
                turmas = carregar_turmas()
                
                # Encontra a chave da turma atual
                turma_atual_key = None
                for key, val in turmas.items():
                    if val == dados_aluno['id_turma']:
                        turma_atual_key = key
                        break
                
                nova_turma = st.selectbox("Turma", 
                                           options=list(turmas.keys()),
                                           index=list(turmas.keys()).index(turma_atual_key) if turma_atual_key else 0)
            
            salvar = st.form_submit_button("💾 Salvar Alterações")
            
            if salvar:
                if novo_nome and novo_cpf:
                    sucesso, msg = database.atualizar_aluno(
                        aluno_id, novo_nome, str(nova_data), novo_cpf, 
                        novo_email, turmas[nova_turma]
                    )
                    if sucesso:
                        mostrar_mensagem("sucesso", msg)
                        st.rerun()
                    else:
                        mostrar_mensagem("erro", msg)
                else:
                    mostrar_mensagem("erro", "Preencha os campos obrigatórios!")

# ==================== ABA: EXCLUSÃO ====================

def aba_exclusao():
    st.header("🗑️ Excluir Aluno")
    
    alunos = database.buscar_alunos()
    if not alunos:
        st.info("Nenhum aluno cadastrado.")
        return
    
    opcoes = {f"{a['nome']} (CPF: {a['cpf']})": a['id'] for a in alunos}
    aluno_selecionado = st.selectbox("Selecione o aluno para excluir", 
                                      options=list(opcoes.keys()))
    
    if st.button("❌ Excluir Aluno", type="primary"):
        aluno_id = opcoes[aluno_selecionado]
        
        # Confirmação
        confirm = st.checkbox("Confirmar exclusão")
        
        if confirm:
            sucesso, msg = database.excluir_aluno(aluno_id)
            if sucesso:
                mostrar_mensagem("sucesso", msg)
                st.rerun()
            else:
                mostrar_mensagem("erro", msg)
        else:
            st.warning("Marque a caixa de confirmação para excluir.")

# ==================== ABA: GERENCIAR TURMAS (BÔNUS) ====================

def aba_turmas():
    st.header("🏫 Gerenciar Turmas")
    
    # Adicionar nova turma
    with st.expander("➕ Adicionar Nova Turma", expanded=False):
        with st.form("form_turma"):
            nome_turma = st.text_input("Nome da Turma", placeholder="3º Ano A")
            ano = st.number_input("Ano Letivo", min_value=2020, max_value=2030, 
                                  value=pd.Timestamp.now().year)
            
            if st.form_submit_button("Adicionar"):
                if nome_turma:
                    database.adicionar_turma(nome_turma, ano)
                    mostrar_mensagem("sucesso", "Turma adicionada!")
                    st.rerun()
                else:
                    mostrar_mensagem("erro", "Digite o nome da turma!")
    
    # Listar turmas
    turmas = database.listar_turmas()
    if turmas:
        st.subheader("Turmas Cadastradas")
        df_turmas = pd.DataFrame(turmas, columns=['ID', 'Nome', 'Ano Letivo'])
        st.table(df_turmas)
        
        # Estatísticas
        st.subheader("📊 Alunos por Turma")
        estatisticas = database.estatisticas_turmas()
        if estatisticas:
            df_estat = pd.DataFrame(estatisticas, columns=['Turma', 'Ano', 'Total Alunos'])
            st.bar_chart(data=df_estat.set_index('Turma')['Total Alunos'])
    else:
        st.info("Nenhuma turma cadastrada.")

# ==================== MENU PRINCIPAL ====================

def main():
    st.title("🏫 Sistema de Gestão Escolar")
    
    # Sidebar com menu
    st.sidebar.title("Menu de Navegação")
    pagina = st.sidebar.radio(
        "Ir para:",
        ["Cadastro", "Consulta", "Edição", "Exclusão", "Turmas (Bônus)"]
    )
    
    # Renderiza a página selecionada
    if pagina == "Cadastro":
        aba_cadastro()
    elif pagina == "Consulta":
        aba_consulta()
    elif pagina == "Edição":
        aba_edicao()
    elif pagina == "Exclusão":
        aba_exclusao()
    elif pagina == "Turmas (Bônus)":
        aba_turmas()

if __name__ == "__main__":
    main()