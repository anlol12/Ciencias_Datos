# carga_archivos.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from styles import page_header, section_label

def _set_dark_style():
    plt.rcParams.update({
        "figure.facecolor": "#161b22",
        "axes.facecolor":   "#161b22",
        "axes.edgecolor":   "#30363d",
        "axes.labelcolor":  "#c9d1d9",
        "xtick.color":      "#7d8590",
        "ytick.color":      "#7d8590",
        "text.color":       "#c9d1d9",
        "grid.color":       "#21262d",
        "grid.linestyle":   "--",
        "grid.alpha":       0.5,
    })

def carga_archivos():
    page_header("📁", "Carga de Archivos", "Sube un CSV o Excel y obtén visualizaciones automáticas")

    st.markdown("""
    <div class="content-card">
        <h4>¿Cómo funciona?</h4>
        <p>Selecciona un archivo desde tu equipo. El sistema detectará automáticamente
        las columnas numéricas y te mostrará estadísticas y gráficos al instante.
        Compatible con archivos <b style="color:#4fc3f7">.csv</b> y <b style="color:#4fc3f7">.xlsx</b>.</p>
    </div>
    """, unsafe_allow_html=True)

    archivo = st.file_uploader("Selecciona tu archivo:", type=["csv", "xlsx"])

    if archivo is None:
        st.markdown("""
        <div style="text-align:center; padding:48px 0; color:#484f58; font-size:0.88rem">
            <span style="font-size:2.5rem">📂</span><br><br>
            Ningún archivo seleccionado aún
        </div>
        """, unsafe_allow_html=True)
        return

    try:
        if archivo.name.endswith('.csv'):
            df_sub = pd.read_csv(archivo)
        else:
            df_sub = pd.read_excel(archivo)

        st.markdown('<span class="badge badge-green">✓ Archivo cargado correctamente</span>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        # ── Métricas ─────────────────────────────────────────────
        section_label("Resumen del archivo")
        cols = st.columns(3)
        datos = [
            (f"{df_sub.shape[0]:,}", "Filas"),
            (str(df_sub.shape[1]), "Columnas"),
            (str(df_sub.isna().sum().sum()), "Valores faltantes"),
        ]
        for col, (num, label) in zip(cols, datos):
            with col:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="m-num">{num}</div>
                    <div class="m-label">{label}</div>
                </div>""", unsafe_allow_html=True)

        # ── Vista previa ─────────────────────────────────────────
        section_label("Vista previa — primeros 10 registros")
        st.dataframe(df_sub.head(10), use_container_width=True)

        # ── Gráfico ──────────────────────────────────────────────
        columnas_num = df_sub.select_dtypes(include=['float64', 'int64']).columns.tolist()

        if columnas_num:
            section_label("Gráfico de distribución")
            var_graf = st.selectbox("Selecciona una columna numérica:", columnas_num)

            _set_dark_style()
            fig, ax = plt.subplots(figsize=(9, 4))
            sns.histplot(df_sub[var_graf].dropna(), kde=True, color="#4fc3f7", alpha=0.7, ax=ax)
            ax.set_title(f"Distribución de {var_graf}", color="#e6edf3", fontsize=13, pad=10)
            ax.set_xlabel(var_graf, color="#7d8590")
            ax.set_ylabel("Frecuencia", color="#7d8590")
            fig.tight_layout()
            st.pyplot(fig)

            # Estadísticas rápidas
            section_label("Estadísticas descriptivas")
            st.dataframe(df_sub[columnas_num].describe(), use_container_width=True)
        else:
            st.markdown("""
            <div class="content-card">
                <h4>Sin columnas numéricas</h4>
                <p>El archivo cargado no contiene columnas numéricas compatibles para generar gráficos.</p>
            </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.markdown(f"""
        <div class="content-card" style="border-color:#f85149">
            <h4 style="color:#f85149">Error al procesar el archivo</h4>
            <p>{e}</p>
        </div>
        """, unsafe_allow_html=True)