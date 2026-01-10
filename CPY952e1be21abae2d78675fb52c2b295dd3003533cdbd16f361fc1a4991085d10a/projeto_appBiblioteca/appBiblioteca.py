import streamlit as st

if 'dados' not in st.session_state:
    st.session_state.dados = [
        {"id": 1, "titulo": "Neuromancer", "autor": "William Gibson", "ano": 1985},
        {"id": 2, "titulo": "Fundação", "autor": "Isaac Asimov", "ano": 1957},  
        {"id": 3, "titulo": "O Conde de Monte Cristo", "autor": "Alexandre Dumas", "ano": 1844},
        {"id": 4, "titulo": "O Senhor dos Aneis", "autor": "J. R. R. Tolkien", "ano": 1954},
        {"id": 5, "titulo": "O Hobbit", "autor": "J. R. R. Tolkien", "ano": 1937}
    ]

st.sidebar.title("Navegação")
pagina = st.sidebar.radio(
    "Escolha a operação:",
    ["Incluir Livro", "Excluir Livro", "Relatórios", 
     "Exportar Dados", "Importar Dados"]
)


# Conteúdo das páginas
if pagina == "Incluir Livro":
    st.subheader("Incluir Livro")
    idLivro = len(st.session_state.dados)+1
    titulo = st.text_input("Título")
    autor = st.text_input("Autor")
    ano = st.number_input("Ano", 0, 2100)
    if st.button("Incluir"):
        if titulo == "" or autor == "":
            st.error("Por favor, preencha todos os campos.")
        else:
            livro = {
                "id": idLivro,
                "titulo": titulo,
                "autor": autor,
                "ano": ano
            }
            st.session_state.dados.append(livro)
            st.success("Livro incluído com sucesso!")
            
elif pagina == "Excluir Livro":
    st.subheader("Excluir Livro")
    idLivro = st.number_input("Id do Livro",1,300,None)
    if idLivro:
        livro = st.session_state.dados[int(idLivro)-1]
        if livro:
            st.write(f"ID: {livro['id']} " +
                    f"{livro['titulo']} " +
                    f"({livro['autor']} / {livro['ano']})")
        else:
            st.error("Livro não encontrado.")
    if st.button("Excluir"):
        for livro in st.session_state.dados:
            if livro["id"] == int(idLivro):
                st.session_state.dados.remove(livro)
                st.success("Livro excluído com sucesso!")
                break

elif pagina == "Relatórios":
    st.subheader("Relatórios")

    col1, col2 = st.columns(2)
    with col1:
        anoRelatorio = st.number_input("Ano", 0, 2100, None)
    with col2:
        autorRelatorio = st.text_input("Autor")

    relat = st.container(border=True)
    for livro in st.session_state.dados:
        if anoRelatorio and anoRelatorio != livro["ano"] :
            continue
        if autorRelatorio and autorRelatorio not in livro["autor"]:
            continue
        relat.write(f"ID: {livro['id']} " +
                    f"{livro['titulo']} " +
                    f"({livro['autor']} / {livro['ano']})")
    st.info("Fim do Relatório")

elif pagina == "Exportar Dados":
    st.subheader("Exportar Dados")
    st.write("Exportando dados...")

elif pagina == "Importar Dados":
    st.subheader("Importar Dados")
    st.write("Importando dados...")
