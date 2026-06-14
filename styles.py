# styles.py 
import streamlit as st

def aplicar_estilos():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"], .stApp {
        font-family: 'Inter', sans-serif;
    }

    /* ── SIDEBAR ── */
    [data-testid="stSidebar"] {
        background: #0d1117 !important;
        border-right: 1px solid #21262d;
    }
    [data-testid="stSidebar"] * {
        color: #e6edf3 !important;
    }

    /* ── FONDO GENERAL ── */
    .stApp {
        background: #0d1117;
    }

    /* ── TÍTULOS DE PÁGINA ── */
    .page-header {
        padding: 28px 0 8px 0;
        margin-bottom: 4px;
    }
    .page-header h2 {
        font-size: 1.6rem;
        font-weight: 700;
        color: #e6edf3;
        margin: 0;
    }
    .page-header p {
        color: #7d8590;
        font-size: 0.9rem;
        margin: 4px 0 0 0;
    }
    .page-divider {
        border: none;
        border-top: 1px solid #21262d;
        margin: 12px 0 24px 0;
    }

    /* ── TARJETAS DE MÉTRICAS ── */
    .metric-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 20px 18px;
        text-align: center;
    }
    .metric-card .m-num {
        font-size: 2rem;
        font-weight: 700;
        color: #4fc3f7;
        line-height: 1;
    }
    .metric-card .m-label {
        font-size: 0.8rem;
        color: #7d8590;
        margin-top: 6px;
    }

    /* ── TARJETAS DE CONTENIDO ── */
    .content-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 22px;
        margin-bottom: 14px;
        color: #e6edf3;
    }
    .content-card h4 {
        color: #e6edf3;
        font-size: 1rem;
        font-weight: 600;
        margin: 0 0 8px 0;
    }
    .content-card p {
        color: #7d8590;
        font-size: 0.87rem;
        margin: 0;
        line-height: 1.6;
    }

    /* ── BADGES ── */
    .badge {
        display: inline-block;
        background: rgba(79,195,247,0.12);
        border: 1px solid rgba(79,195,247,0.35);
        color: #4fc3f7;
        padding: 3px 11px;
        border-radius: 20px;
        font-size: 0.75rem;
        margin: 3px 3px 3px 0;
        font-weight: 500;
    }
    .badge-green {
        background: rgba(63,185,80,0.12);
        border-color: rgba(63,185,80,0.35);
        color: #3fb950;
    }
    .badge-purple {
        background: rgba(188,140,255,0.12);
        border-color: rgba(188,140,255,0.35);
        color: #bc8cff;
    }
    .badge-orange {
        background: rgba(255,167,38,0.12);
        border-color: rgba(255,167,38,0.35);
        color: #ffa726;
    }

    /* ── SECCIÓN TÍTULO ── */
    .section-label {
        font-size: 0.7rem;
        font-weight: 600;
        color: #4fc3f7;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin: 28px 0 10px 0;
    }

    /* ── HERO PORTAFOLIO ── */
    .hero-wrap {
        background: linear-gradient(135deg, #161b22 0%, #0d1117 100%);
        border: 1px solid #30363d;
        border-radius: 14px;
        padding: 36px 32px;
        margin-bottom: 28px;
        position: relative;
        overflow: hidden;
    }
    .hero-wrap::before {
        content: '';
        position: absolute;
        top: -60px; right: -60px;
        width: 220px; height: 220px;
        background: radial-gradient(circle, rgba(79,195,247,0.08) 0%, transparent 70%);
        pointer-events: none;
    }
    .hero-name {
        font-size: 2rem;
        font-weight: 700;
        color: #e6edf3;
        margin: 0 0 4px 0;
    }
    .hero-sub {
        font-size: 0.9rem;
        color: #7d8590;
        margin: 0 0 16px 0;
    }
    .hero-bio {
        font-size: 0.95rem;
        color: #c9d1d9;
        line-height: 1.75;
        border-left: 3px solid #4fc3f7;
        padding-left: 16px;
        margin-top: 16px;
    }

    /* ── TARJETAS DE NAVEGACIÓN ── */
    .nav-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 18px 20px;
        margin-bottom: 10px;
        transition: border-color 0.2s;
    }
    .nav-card:hover { border-color: #4fc3f7; }
    .nav-card .nc-icon { font-size: 1.4rem; margin-bottom: 6px; }
    .nav-card .nc-title { font-weight: 600; font-size: 0.93rem; color: #e6edf3; }
    .nav-card .nc-desc { font-size: 0.82rem; color: #7d8590; margin-top: 3px; line-height: 1.5; }

    /* ── SENTIMIENTOS ── */
    .sent-card {
        border-radius: 10px;
        padding: 16px 18px;
        margin-bottom: 12px;
        border-left: 4px solid;
    }
    .sent-pos { background: rgba(63,185,80,0.08); border-color: #3fb950; }
    .sent-neg { background: rgba(248,81,73,0.08); border-color: #f85149; }
    .sent-neu { background: rgba(255,167,38,0.08); border-color: #ffa726; }
    .sent-card .sc-text { color: #c9d1d9; font-size: 0.9rem; line-height: 1.6; margin-bottom: 8px; }
    .sent-card .sc-result { font-size: 0.82rem; font-weight: 600; }
    .sent-pos .sc-result { color: #3fb950; }
    .sent-neg .sc-result { color: #f85149; }
    .sent-neu .sc-result { color: #ffa726; }

    /* ── OVERRIDES STREAMLIT ── */
    .stSelectbox label, .stRadio label, .stSlider label,
    .stTextInput label, .stFileUploader label {
        color: #c9d1d9 !important;
        font-size: 0.88rem !important;
        font-weight: 500 !important;
    }
    .stMetric { background: #161b22; border: 1px solid #30363d; border-radius: 10px; padding: 14px 18px !important; }
    .stMetric label { color: #7d8590 !important; font-size: 0.78rem !important; }
    .stMetric [data-testid="stMetricValue"] { color: #4fc3f7 !important; font-size: 1.6rem !important; font-weight: 700 !important; }
    div[data-testid="stDataFrame"] { border: 1px solid #30363d; border-radius: 8px; overflow: hidden; }
    .stButton > button {
        background: #4fc3f7 !important;
        color: #0d1117 !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 8px 20px !important;
    }
    .stButton > button:hover { background: #29b6f6 !important; }

    /* ── PIE DE PÁGINA ── */
    .footer {
        text-align: center;
        color: #484f58;
        font-size: 0.78rem;
        padding: 32px 0 12px 0;
        border-top: 1px solid #21262d;
        margin-top: 40px;
    }
    </style>
    """, unsafe_allow_html=True)


def page_header(icon, title, subtitle=""):
    st.markdown(f"""
    <div class="page-header">
        <h2>{icon} {title}</h2>
        {"<p>" + subtitle + "</p>" if subtitle else ""}
    </div>
    <hr class="page-divider">
    """, unsafe_allow_html=True)


def section_label(text):
    st.markdown(f'<p class="section-label">{text}</p>', unsafe_allow_html=True)


def metric_cards(items):
    """items = list of (numero, label)"""
    cols = st.columns(len(items))
    for col, (num, label) in zip(cols, items):
        with col:
            st.markdown(f"""
            <div class="metric-card">
                <div class="m-num">{num}</div>
                <div class="m-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)