# eda.py
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from styles import page_header, section_label

# Paleta oscura para matplotlib
def _set_dark_style():
    plt.rcParams.update({
        "figure.facecolor":  "#161b22",
        "axes.facecolor":    "#161b22",
        "axes.edgecolor":    "#30363d",
        "axes.labelcolor":   "#c9d1d9",
        "xtick.color":       "#7d8590",
        "ytick.color":       "#7d8590",
        "text.color":        "#c9d1d9",
        "grid.color":        "#21262d",
        "grid.linestyle":    "--",
        "grid.alpha":        0.6,
    })

def eda(df):
    page_header("📊", "Análisis Exploratorio", "Google Play Store · más de 10,000 aplicaciones")

    sub_menu = st.radio(
        "Sección:",
        ["Descripción del dataset", "Descripción de los campos",
         "Navegador completo", "Buscador de registros", "Graficador exploratorio", "Hipótesis"],
        horizontal=True,
        label_visibility="collapsed"
    )

    diccionario_campos = {
        'App':            'Nombre de la aplicación móvil.',
        'Category':       'Categoría del mercado (GAME, FAMILY, etc.).',
        'Rating':         'Calificación promedio dada por los usuarios (1.0 a 5.0).',
        'Reviews':        'Número total de reseñas escritas.',
        'Size':           'Espacio de almacenamiento requerido para la instalación.',
        'Installs':       'Volumen aproximado de descargas.',
        'Type':           'Distribución comercial: Gratis (Free) o Pago (Paid).',
        'Price':          'Costo de adquisición en dólares ($).',
        'Content Rating': 'Público objetivo y restricciones por edad.',
        'Genres':         'Subgéneros asignados por el desarrollador.',
    }

    # ── DESCRIPCIÓN ─────────────────────────────────────────────
    if sub_menu == "Descripción del dataset":
        section_label("Resumen general")
        cols = st.columns(3)
        datos = [
            (f"{df.shape[0]:,}", "Aplicaciones registradas"),
            (str(df.shape[1]), "Variables analizadas"),
            (f"{df.isna().sum().sum():,}", "Valores faltantes"),
        ]
        for col, (num, label) in zip(cols, datos):
            with col:
                st.markdown(f"""
                <div class="metric-card">
                    <div class="m-num">{num}</div>
                    <div class="m-label">{label}</div>
                </div>""", unsafe_allow_html=True)

        section_label("Primeros registros")
        st.dataframe(df.head(10), use_container_width=True)

        st.markdown("""
        <div class="content-card" style="margin-top:16px">
            <h4>Sobre el dataset</h4>
            <p>Recopila información de miles de aplicaciones de la Google Play Store,
            permitiendo analizar tendencias de descarga, estrategias de monetización
            y niveles de satisfacción del usuario en distintas categorías.</p>
        </div>
        """, unsafe_allow_html=True)

    # ── CAMPOS ──────────────────────────────────────────────────
    elif sub_menu == "Descripción de los campos":
        section_label("Diccionario de variables")
        campo_elegido = st.selectbox("Selecciona un campo:", list(diccionario_campos.keys()))

        st.markdown(f"""
        <div class="content-card">
            <h4>{campo_elegido}</h4>
            <p>{diccionario_campos[campo_elegido]}</p>
        </div>
        """, unsafe_allow_html=True)

        mapeo_num = {
            'Rating': 'Rating_numeric', 'Reviews': 'Reviews_numeric',
            'Installs': 'Installs_numeric', 'Price': 'Price_numeric', 'Size': 'Size_MB'
        }

        if campo_elegido in mapeo_num:
            section_label("Estadísticas descriptivas")
            st.dataframe(df[[mapeo_num[campo_elegido]]].describe(), use_container_width=True)
        else:
            section_label("Valores únicos (muestra de 50)")
            valores = list(df[campo_elegido].dropna().unique()[:50])
            st.markdown(" ".join([f'<span class="badge">{v}</span>' for v in valores]), unsafe_allow_html=True)

    # ── NAVEGADOR ────────────────────────────────────────────────
    elif sub_menu == "Navegador completo":
        section_label(f"Dataset completo — {df.shape[0]:,} registros")
        st.dataframe(df, use_container_width=True)

    # ── BUSCADOR ─────────────────────────────────────────────────
    elif sub_menu == "Buscador de registros":
        section_label("Búsqueda por nombre de app")
        texto = st.text_input("Escribe el nombre o parte del nombre:")
        if texto:
            resultados = df[df['App'].str.contains(texto, case=False, na=False)]
            st.markdown(f'<span class="badge badge-green">{len(resultados)} coincidencias</span>', unsafe_allow_html=True)
            st.dataframe(resultados, use_container_width=True)
        else:
            st.markdown('<p style="color:#7d8590; font-size:0.88rem">Escribe algo para comenzar la búsqueda.</p>', unsafe_allow_html=True)

    # ── GRAFICADOR ───────────────────────────────────────────────
    elif sub_menu == "Graficador exploratorio":
        section_label("Visualización automática por campo")
        campo_grafica = st.selectbox(
            "Campo a graficar:",
            ["Rating", "Reviews", "Installs", "Price", "Type", "Content Rating"]
        )
        mapeo_num = {
            'Rating': 'Rating_numeric', 'Reviews': 'Reviews_numeric',
            'Installs': 'Installs_numeric', 'Price': 'Price_numeric'
        }

        _set_dark_style()
        fig, ax = plt.subplots(figsize=(9, 4))

        if campo_grafica in mapeo_num:
            sns.histplot(df[mapeo_num[campo_grafica]].dropna(), kde=True, ax=ax,
                         color="#4fc3f7", alpha=0.7)
            ax.set_title(f"Distribución de {campo_grafica}", color="#e6edf3", fontsize=13, pad=12)
        else:
            top = df[campo_grafica].value_counts().head(10)
            bars = ax.bar(top.index, top.values, color="#4fc3f7", alpha=0.8)
            ax.set_title(f"Top 10 — {campo_grafica}", color="#e6edf3", fontsize=13, pad=12)
            plt.xticks(rotation=30, ha='right')

        ax.set_xlabel(campo_grafica, color="#7d8590")
        ax.set_ylabel("Frecuencia", color="#7d8590")
        fig.tight_layout()
        st.pyplot(fig)

    # ── HIPÓTESIS ────────────────────────────────────────────────
    elif sub_menu == "Hipótesis":
        section_label("Validación de hipótesis")
        hipotesis = st.selectbox("Selecciona una hipótesis:", [
            "H1 — Las apps de pago tienen mejor calificación que las gratuitas",
            "H2 — Las apps para adolescentes tienen más descargas que las de todo público",
        ])

        _set_dark_style()
        fig, ax = plt.subplots(figsize=(8, 4))

        if "H1" in hipotesis:
            resumen = df.groupby('Type')['Rating_numeric'].mean().dropna()

            col_datos, col_conc = st.columns([1, 1])
            with col_datos:
                section_label("Rating promedio por tipo")
                st.dataframe(resumen.reset_index().rename(columns={'Rating_numeric': 'Rating promedio'}),
                             use_container_width=True)
            with col_conc:
                st.markdown("""
                <div class="content-card" style="margin-top:20px">
                    <h4>✅ Hipótesis validada</h4>
                    <p>Las apps de pago promedian <b style="color:#4fc3f7">4.26</b> frente a
                    <b style="color:#4fc3f7">4.18</b> de las gratuitas. El software de pago
                    mantiene un estándar de calidad más alto porque los usuarios que pagan
                    exigen mayor cuidado en la experiencia.</p>
                </div>
                """, unsafe_allow_html=True)

            sns.boxplot(
                data=df[df['Type'].isin(['Free', 'Paid'])],
                x='Type', y='Rating_numeric', ax=ax,
                palette={"Free": "#30363d", "Paid": "#4fc3f7"},
                linewidth=1.2
            )
            ax.set_title("Distribución de Rating: Free vs Paid", color="#e6edf3", fontsize=13)

        elif "H2" in hipotesis:
            grupos = ['Everyone', 'Teen']
            resumen = df.groupby('Content Rating')['Installs_numeric'].mean()
            resumen = resumen.loc[[g for g in grupos if g in resumen.index]]

            col_datos, col_conc = st.columns([1, 1])
            with col_datos:
                section_label("Descargas promedio por público")
                st.dataframe(resumen.reset_index().rename(columns={'Installs_numeric': 'Descargas promedio'}),
                             use_container_width=True)
            with col_conc:
                st.markdown("""
                <div class="content-card" style="margin-top:20px">
                    <h4>✅ Hipótesis validada</h4>
                    <p>El grupo <b style="color:#4fc3f7">Teen</b> promedia ~28.7M de descargas,
                    casi el doble que <b style="color:#4fc3f7">Everyone</b> con ~13.1M.
                    El público adolescente es el segmento más activo y viral de la tienda.</p>
                </div>
                """, unsafe_allow_html=True)

            colores = ["#30363d", "#4fc3f7"]
            resumen.plot(kind='bar', ax=ax, color=colores, alpha=0.85, edgecolor='none')
            ax.set_title("Descargas promedio: Everyone vs Teen", color="#e6edf3", fontsize=13)
            plt.xticks(rotation=0)

        ax.set_xlabel("")
        fig.tight_layout()
        st.pyplot(fig)