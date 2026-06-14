# prueba.py
import streamlit as st
import pandas as pd
from PIL import Image

from styles import aplicar_estilos
from eda import eda
from ml import ml
from carga_archivos import carga_archivos
from scrapping_sentimientos import scrapping_sentimientos
from parcial import parcial

st.set_page_config(
    page_title="Portafolio · Ciencia de Datos",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Aplicar estilos globales una sola vez
aplicar_estilos()

@st.cache_data
def cargar_datos():
    df = pd.read_csv('googleplaystore.csv')
    df = df.drop(10472, errors='ignore')

    df['Reviews_numeric']  = pd.to_numeric(df['Reviews'], errors='coerce')
    df['Installs_numeric'] = (
        df['Installs'].astype(str)
        .str.replace('+', '', regex=False)
        .str.replace(',', '', regex=False)
    )
    df['Installs_numeric'] = pd.to_numeric(df['Installs_numeric'], errors='coerce')
    df['Price_numeric']    = pd.to_numeric(
        df['Price'].astype(str).str.replace('$', '', regex=False), errors='coerce'
    )
    df['Rating_numeric']   = pd.to_numeric(df['Rating'], errors='coerce')

    def limpiar_tamano(val):
        if not isinstance(val, str): return None
        if 'M' in val: return float(val.replace('M', ''))
        if 'k' in val: return float(val.replace('k', '')) / 1024.0
        return None
    df['Size_MB'] = df['Size'].apply(limpiar_tamano)

    return df

# ── SIDEBAR ─────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="padding: 8px 0 20px 0">
        <p style="font-size:0.7rem; color:#484f58; text-transform:uppercase;
                  letter-spacing:1.2px; margin:0 0 8px 0">Portafolio</p>
    </div>
    """, unsafe_allow_html=True)

    menu_principal = st.selectbox(
        "Sección:",
        ("INICIO", "TAREA 1", "TAREA 2"),
        label_visibility="collapsed"
    )

    st.markdown("---")

    sub_t1 = sub_t2 = None

    if menu_principal == "TAREA 1":
        st.markdown('<p style="font-size:0.7rem; color:#484f58; text-transform:uppercase; letter-spacing:1px; margin:0 0 6px 0">Tarea 1</p>', unsafe_allow_html=True)
        sub_t1 = st.radio(
            "Opción:",
            ("Análisis Exploratorio (EDA)", "Aprendizaje Automático (ML)"),
            label_visibility="collapsed"
        )

    elif menu_principal == "TAREA 2":
        st.markdown('<p style="font-size:0.7rem; color:#484f58; text-transform:uppercase; letter-spacing:1px; margin:0 0 6px 0">Tarea 2</p>', unsafe_allow_html=True)
        sub_t2 = st.radio(
            "Opción:",
            ("Carga de Archivos", "Análisis de Sentimientos"),
            label_visibility="collapsed"
        )

    st.markdown("""
    <div style="position:fixed; bottom:16px; left:0; width:240px;
                text-align:center; color:#484f58; font-size:0.72rem">
        Técnica Electiva I · 2026
    </div>
    """, unsafe_allow_html=True)

# ── CONTENIDO PRINCIPAL ──────────────────────────────────────
df = cargar_datos()

if menu_principal == "INICIO":
    parcial()

elif menu_principal == "TAREA 1":
    if sub_t1 == "Análisis Exploratorio (EDA)":
        eda(df)
    elif sub_t1 == "Aprendizaje Automático (ML)":
        ml(df)

elif menu_principal == "TAREA 2":
    if sub_t2 == "Carga de Archivos":
        carga_archivos()
    elif sub_t2 == "Análisis de Sentimientos":
        scrapping_sentimientos()