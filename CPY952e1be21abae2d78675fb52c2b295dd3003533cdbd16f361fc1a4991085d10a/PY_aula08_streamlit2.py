import streamlit as st

# 1. Configuração da página (opcional)
st.set_page_config(page_title="Meu App", 
                   page_icon=":smiley:", 
                   layout="centered")

# 2. Título e descrição
st.title("Meu Aplicativo")
st.write("Descrição do app")

# 3. Inputs do usuário
nome = st.text_input("Digite seu nome:")

# 4. Processamento e lógica
if nome:
    mensagem = f"Olá, {nome}!"
    # Exibição de resultados
    st.success(mensagem)