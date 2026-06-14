# parcial.py
import streamlit as st
from styles import page_header, section_label, metric_cards

def parcial():
    st.markdown("""
    <style>
    .photo-placeholder {
        background: #161b22;
        border: 2px dashed #30363d;
        border-radius: 12px;
        height: 240px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #484f58;
        font-size: 0.85rem;
        text-align: center;
        flex-direction: column;
        gap: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

    # ──────────────────────────────────────────────────────
    col_foto, col_info = st.columns([1, 2.4], gap="large")

    with col_foto:
        try:
            from PIL import Image
            foto = Image.open("fotoportafolio.jpeg") 
            st.image(foto, use_container_width=True)
        except FileNotFoundError:
            st.markdown("""
            <div class="photo-placeholder">
                <span style="font-size:2rem">📷</span>
                <span><br>como <b>mi_foto.jpg</b></span>
            </div>
            """, unsafe_allow_html=True)

    with col_info:
        st.markdown("""
        <div class="hero-wrap">
            <p class="hero-name">Anderson Jose Berrios Diaz</p>
            <p class="hero-sub">Ingeniería en Sistemas y Redes Informáticas &nbsp;·&nbsp;</p>
            <div>
                <span class="badge">Python</span>
                <span class="badge">Streamlit</span>
                <span class="badge badge-green">Machine Learning</span>
                <span class="badge badge-purple">NLP</span>
                <span class="badge badge-orange">Data Analysis</span>
            </div>
            <p class="hero-bio">
                Soy estudiante de Ingeniería en Sistemas y Redes Informáticas 
                en la Universidad Gerardo Barrios. 
                Me apasiona el mundo de la tecnología y el desarrollo, 
                especialmente la programación, el diseño de bases de 
                datos en SQL, la electrónica y, sobre todo, la ciencia y 
                el análisis de datos.
            </p>
        </div>
        """, unsafe_allow_html=True)

    # ── MÉTRICAS ────────────────────────────────────────────────
    section_label("El proyecto en números")
    metric_cards([
        ("10K+", "Apps analizadas"),
        ("7", "Secciones del portafolio"),
        ("2", "Modelos de ML"),
        ("2", "Hipótesis validadas"),
    ])

    # ── VIDEO ────────────────────────────────────────────────────
    section_label("Demo · Data Storytelling")
    st.markdown("""
    <div class="content-card">
        <h4>🎥 Google Play Store — Análisis narrativo</h4>
        <p>Exploración de tendencias en descargas, calificaciones y monetización de más de 10,000 aplicaciones móviles.</p>
    </div>
    """, unsafe_allow_html=True)

    VIDEO_URL = "https://www.youtube.com/watch?v=XXXXXXXXXX"  # 👈 Tu link de YouTube
    st.video(VIDEO_URL)

    # ── NAVEGACIÓN ───────────────────────────────────────────────
    section_label("Contenido del portafolio")

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="nav-card">
            <div class="nc-icon">📊</div>
            <div class="nc-title">Análisis Exploratorio (EDA)</div>
            <div class="nc-desc">Descripción del dataset, estadísticas por campo, graficador automático y validación de hipótesis.</div>
        </div>
        <div class="nav-card">
            <div class="nc-icon">🤖</div>
            <div class="nc-title">Aprendizaje Automático</div>
            <div class="nc-desc">Regresión Lineal y Árbol de Decisión interactivos con métricas en tiempo real.</div>
        </div>
        <div class="nav-card">
            <div class="nc-icon">🎮</div>
            <div class="nc-title">Sistema de Recomendación</div>
            <div class="nc-desc">Motor de recomendaciones personalizado basado en preferencias del usuario.</div>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.markdown("""
        <div class="nav-card">
            <div class="nc-icon">📁</div>
            <div class="nc-title">Carga de Archivos</div>
            <div class="nc-desc">Sube tu propio CSV o Excel y obtén visualizaciones automáticas al instante.</div>
        </div>
        <div class="nav-card">
            <div class="nc-icon">🕵️</div>
            <div class="nc-title">Análisis de Sentimientos</div>
            <div class="nc-desc">Scraping de opiniones en español con clasificación positivo / negativo / neutro.</div>
        </div>
        <div class="nav-card">
            <div class="nc-icon">💡</div>
            <div class="nc-title">Interfaz IA (Opcional)</div>
            <div class="nc-desc">Consulta el dataset con lenguaje natural y obtén respuestas directas sobre los datos.</div>
        </div>
        """, unsafe_allow_html=True)

