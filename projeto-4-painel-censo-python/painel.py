#carregar o pandas e o streamlit
import pandas as pd
import streamlit as st

#função para classificar o porte
def classifica_porte(total):
    if total <= 50:
        return "micro"
    elif total <= 200:
        return "pequena"
    elif total <= 400:
        return "média"
    else:
        return "grande"

#dados
censo = pd.read_csv("escolas_sp_regioes_2024_geo.csv")
censo["porte"] = censo["matriculas"].apply(classifica_porte)

st.title("Painel de Escolas de Regiões de São Paulo")
st.caption("Adaptado do Censo Escolar 2024 (INEP)")

#filtros (na barra lateral)
st.sidebar.header("Filtros")

#filtro 1: região
regiao = st.sidebar.selectbox("Região", ["Todas", "Região Metropolitana de SP", "Baixada Santista", "Litoral Norte", "Vale do Ribeira"])
if regiao != "Todas":
    censo = censo[censo["regiao"] == regiao]

#filtro 2: localização
localizacao = st.sidebar.selectbox("Localização", ["Todas", "Urbana", "Rural"])
if localizacao != "Todas":
    censo = censo[censo["localizacao"] == localizacao]

#filtro 3: porte
porte = st.sidebar.selectbox("Porte", ["Todos", "micro", "pequena", "média", "grande"])
if porte != "Todos":
    censo = censo[censo["porte"] == porte]

#se não sobrou nenhuma escola, avisa e para
if len(censo) == 0:
    st.warning("Nenhuma escola atende a essa combinação de filtros.")
    st.stop()

#contagens e soma
col1, col2 = st.columns(2)
col1.metric("Quantidade de Escolas", len(censo))
col2.metric("Total de Matrículas", censo["matriculas"].sum())

#gráficos de características
st.subheader("Escolas por Porte")
st.bar_chart(censo["porte"].value_counts())

st.subheader("Escolas por Dependência Administrativa")
st.bar_chart(censo["dependencia"].value_counts())

#gráficos de infraestrutura
st.subheader("Escolas por Abastecimento de Água")
st.bar_chart(censo["agua"].value_counts())

st.subheader("Escolas por Destino do Lixo")
st.bar_chart(censo["lixo"].value_counts())

#mapa das escolas
st.subheader("Mapa das Escolas")
st.map(censo[["latitude", "longitude"]])

#lista de escolas
st.subheader("Lista das Escolas")
st.dataframe(censo[["municipio", "escola", "dependencia", "matriculas", "porte"]])