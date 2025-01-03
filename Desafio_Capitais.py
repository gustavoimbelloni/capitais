import streamlit as st

# Dados dos estados e capitais
Estados_e_Capitais = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}

# Interface do jogo
st.title("Jogo: Qual é a capital do estado?")
st.write("Teste seus conhecimentos sobre as capitais do Brasil!")

# Inicialização
if "estado_atual" not in st.session_state:
    st.session_state.estado_atual = None
    st.session_state.rodadas = 0
    st.session_state.acertos = 0

# Selecionar um estado aleatório
import random
if st.session_state.estado_atual is None:
    st.session_state.estado_atual = random.choice(list(Estados_e_Capitais.keys()))

estado = st.session_state.estado_atual
capital_correta = Estados_e_Capitais[estado]

# Exibir o estado
st.write(f"Qual é a capital do estado **{estado}**?")

# Entrada do usuário
resposta = st.text_input("Sua resposta:")

# Verificar resposta
if st.button("Enviar resposta"):
    st.session_state.rodadas += 1
    if resposta.lower() == capital_correta.lower():
        st.session_state.acertos += 1
        st.success("Resposta correta!")
    else:
        st.error(f"Resposta errada! A capital correta é **{capital_correta}**.")
    
    # Escolher o próximo estado
    st.session_state.estado_atual = random.choice(list(Estados_e_Capitais.keys()))

# Exibir estatísticas
st.write(f"Rodadas jogadas: {st.session_state.rodadas}")
st.write(f"Acertos: {st.session_state.acertos}")
if st.session_state.rodadas > 0:
    st.write(f"Porcentagem de acertos: {st.session_state.acertos / st.session_state.rodadas * 100:.2f}%")
