import streamlit as st
from datetime import datetime

# === Classes da aplicção ===
import Hospede
import Quarto
import Hotel

# === Inicialização do Hotel (estado da sessão) ===
if 'hotel' not in st.session_state:
    st.session_state.hotel = Hotel("Hotel Paraíso", "Av. Principal, 1000 - Centro")

    # Quartos pré-cadastrados
    for num, tipo, cap in [(101, "Standard", 2), (102, "Standard", 2),
                           (201, "Suíte", 4), (202, "Suíte", 4),
                           (301, "Luxo", 3)]:
        st.session_state.hotel.adicionar_quarto(Quarto(num, tipo, cap))

hotel = st.session_state.hotel


# === Interface Streamlit ===
st.set_page_config(page_title="Sistema de Hotel - Paraíso", layout="wide")
st.title("🏨 Sistema de Gerenciamento - Hotel Paraíso")

menu = st.sidebar.selectbox(
    "Menu",
    ["Início", "Registrar Hóspede", "Check-in", "Check-out", "Consultar Quartos", "Hóspedes Alocados"]
)

if menu == "Início":
    st.header("Bem-vindo ao Hotel Paraíso")
    st.write(f"**Endereço:** {hotel.endereco}")
    st.write(f"**Total de quartos:** {len(hotel.quartos)}")
    st.write(f"**Hóspedes registrados:** {len(hotel.hospedes)}")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Quartos Disponíveis", len(hotel.listar_quartos_disponiveis()))
    with col2:
        st.metric("Quartos Ocupados", len(hotel.listar_quartos_ocupados()))

elif menu == "Registrar Hóspede":
    st.header("Registrar Novo Hóspede")
    with st.form("form_hospede"):
        nome = st.text_input("Nome completo")
        cpf = st.text_input("CPF (somente números)", max_chars=11)
        email = st.text_input("E-mail (opcional)")
        telefone = st.text_input("Telefone (opcional)")
        submetido = st.form_submit_button("Registrar")

        if submetido:
            if not nome or not cpf:
                st.error("Nome e CPF são obrigatórios.")
            elif len(cpf) != 11 or not cpf.isdigit():
                st.error("CPF deve ter 11 dígitos numéricos.")
            else:
                hospede = Hospede(nome, cpf, email or None, telefone or None)
                if hotel.registrar_hospede(hospede):
                    st.success(f"Hóspede {nome} registrado com sucesso!")
                else:
                    st.warning("Hóspede com este CPF já está registrado.")

elif menu == "Check-in":
    st.header("Realizar Check-in")
    with st.form("form_checkin"):
        cpf = st.text_input("CPF do hóspede")
        quarto_num = st.selectbox(
            "Selecione o quarto",
            options=[q.numero for q in hotel.listar_quartos_disponiveis()],
            format_func=lambda n: f"Quarto {n} ({hotel.quartos[n].tipo})"
        )
        submetido = st.form_submit_button("Fazer Check-in")

        if submetido:
            if not cpf:
                st.error("Informe o CPF do hóspede.")
            else:
                resultado = hotel.check_in(cpf, quarto_num)
                if "realizado" in resultado:
                    st.success(resultado)
                else:
                    st.error(resultado)

elif menu == "Check-out":
    st.header("Realizar Check-out")
    with st.form("form_checkout"):
        quarto_num = st.selectbox(
            "Selecione o quarto ocupado",
            options=[q.numero for q in hotel.listar_quartos_ocupados()],
            format_func=lambda n: str(hotel.quartos[n])
        )
        submetido = st.form_submit_button("Fazer Check-out")

        if submetido:
            resultado = hotel.check_out(quarto_num)
            if "realizado" in resultado:
                st.success(resultado)
            else:
                st.error(resultado)

elif menu == "Consultar Quartos":
    st.header("Status dos Quartos")
    disponiveis = hotel.listar_quartos_disponiveis()
    ocupados = hotel.listar_quartos_ocupados()

    tab1, tab2 = st.tabs(["Disponíveis", "Ocupados"])

    with tab1:
        if disponiveis:
            for q in disponiveis:
                st.write(f"🟢 **{q}**")
        else:
            st.info("Não há quartos disponíveis no momento.")

    with tab2:
        if ocupados:
            for q in ocupados:
                st.write(f"🔴 **{q}**")
        else:
            st.info("Não há quartos ocupados.")

elif menu == "Hóspedes Alocados":
    st.header("Hóspedes Atualmente no Hotel")
    alocados = [h for h in hotel.hospedes if h.quarto_alocado]
    if alocados:
        for h in alocados:
            st.write(f"👤 **{h}**")
    else:
        st.info("Não há hóspedes alocados no momento.")

# Rodapé
st.sidebar.markdown("---")
st.sidebar.caption(f"Data atual: {datetime.now().strftime('%d/%m/%Y %H:%M')}")