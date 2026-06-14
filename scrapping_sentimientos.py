# scrapping_sentimientos.py
import streamlit as st
import requests
from bs4 import BeautifulSoup
from sentiment_analysis_spanish import sentiment_analysis
from styles import page_header, section_label

@st.cache_resource
def iniciar_modelo():
    return sentiment_analysis.SentimentAnalysisSpanish()

def scrapping_sentimientos():
    page_header("🕵️", "Análisis de Sentimientos", "Extrae opiniones de la web y clasifícalas automáticamente")

    st.markdown("""
    <div class="content-card">
        <h4>¿Cómo funciona?</h4>
        <p>Ingresa la URL de cualquier página con texto en español. El sistema extraerá
        los párrafos disponibles y analizará si cada opinión es
        <b style="color:#3fb950">positiva</b>,
        <b style="color:#f85149">negativa</b> o
        <b style="color:#ffa726">neutra</b>
        usando un modelo de NLP entrenado en español.</p>
    </div>
    """, unsafe_allow_html=True)

    nlp = iniciar_modelo()

    section_label("Fuente de datos")
    url_target = st.text_input(
        "URL del sitio a analizar:",
        value="https://es.wikipedia.org/wiki/Videojuego",
        placeholder="https://..."
    )

    if not st.button("Extraer y analizar"):
        return

    opiniones = []

    with st.spinner("Conectando con el sitio web..."):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
            res = requests.get(url_target, headers=headers, timeout=6)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                for p in soup.find_all('p'):
                    texto = p.text.strip()
                    if len(texto) > 30:
                        opiniones.append(texto)
        except Exception:
            st.markdown('<span class="badge badge-orange">⚠ Scraping directo limitado — usando opiniones de demostración</span>', unsafe_allow_html=True)

    if len(opiniones) < 2:
        opiniones = [
            "Esta aplicación es excelente, funciona de maravilla, es muy rápida y amigable.",
            "Es un pésimo servicio, la última actualización es una basura y se cierra constantemente.",
            "La aplicación es regular, cumple su función básica pero le falta mucho desarrollo.",
            "Me encanta la app, el diseño visual es fantástico y no tiene anuncios molestos.",
        ]
        st.markdown('<span class="badge badge-orange">Mostrando opiniones de demostración</span>', unsafe_allow_html=True)
    else:
        st.markdown(f'<span class="badge badge-green">✓ {len(opiniones)} párrafos extraídos</span>', unsafe_allow_html=True)

    section_label("Resultados del análisis")

    positivos = negativos = neutros = 0

    for i, comentario in enumerate(opiniones[:6], 1):
        score = nlp.sentiment(comentario)

        if score > 0.55:
            cls   = "sent-pos"
            emoji = "😊"
            resultado = f"Positivo — confianza {score*100:.1f}%"
            positivos += 1
        elif score < 0.45:
            cls   = "sent-neg"
            emoji = "😡"
            resultado = f"Negativo — confianza {(1-score)*100:.1f}%"
            negativos += 1
        else:
            cls   = "sent-neu"
            emoji = "😐"
            resultado = f"Neutro / mixto — puntaje {score:.2f}"
            neutros += 1

        # Truncar texto largo
        texto_show = comentario if len(comentario) <= 180 else comentario[:180] + "…"

        st.markdown(f"""
        <div class="sent-card {cls}">
            <div class="sc-text">#{i} — {texto_show}</div>
            <div class="sc-result">{emoji} {resultado}</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Resumen numérico ─────────────────────────────────────────
    section_label("Resumen general")
    total = positivos + negativos + neutros
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""<div class="metric-card">
            <div class="m-num" style="color:#3fb950">{positivos}</div>
            <div class="m-label">Positivas</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""<div class="metric-card">
            <div class="m-num" style="color:#f85149">{negativos}</div>
            <div class="m-label">Negativas</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown(f"""<div class="metric-card">
            <div class="m-num" style="color:#ffa726">{neutros}</div>
            <div class="m-label">Neutras</div>
        </div>""", unsafe_allow_html=True)