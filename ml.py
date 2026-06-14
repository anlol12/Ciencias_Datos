# ml.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score, mean_squared_error
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
        "legend.facecolor": "#161b22",
        "legend.edgecolor": "#30363d",
        "legend.labelcolor":"#c9d1d9",
    })

def ml(df):
    page_header("🤖", "Aprendizaje Automático", "Modelos de regresión interactivos sobre datos de la Play Store")

    col_config, col_resultado = st.columns([1, 2], gap="large")

    with col_config:
        section_label("Configuración del modelo")

        algoritmo = st.selectbox("Algoritmo:", ["Regresión Lineal", "Árbol de Decisión"])
        var_y     = st.selectbox("Variable objetivo (Y):", ["Rating_numeric", "Installs_numeric"])

        opciones_x = ["Reviews_numeric", "Size_MB", "Price_numeric", "Installs_numeric"]
        if var_y in opciones_x:
            opciones_x.remove(var_y)
        var_x = st.selectbox("Variable independiente (X):", opciones_x)

        test_pct  = st.slider("Datos de prueba (%):", 10, 50, 20, 5)
        test_prop = test_pct / 100.0

        st.markdown(f"""
        <div class="content-card" style="margin-top:12px">
            <h4>Resumen de configuración</h4>
            <p>
                <span class="badge">{algoritmo}</span>
                <span class="badge badge-green">Y: {var_y}</span>
                <span class="badge badge-purple">X: {var_x}</span>
                <span class="badge badge-orange">Test: {test_pct}%</span>
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_resultado:
        # ── Preparar datos ───────────────────────────────────────
        datos = df[[var_x, var_y]].dropna()
        if var_x in ["Reviews_numeric", "Installs_numeric"]:
            q_lim = datos[var_x].quantile(0.95)
            datos = datos[datos[var_x] <= q_lim]

        X = datos[[var_x]]
        y = datos[var_y]
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_prop, random_state=42
        )

        # ── Entrenar ─────────────────────────────────────────────
        if algoritmo == "Regresión Lineal":
            modelo = LinearRegression()
        else:
            modelo = DecisionTreeRegressor(max_depth=4, random_state=42)

        modelo.fit(X_train, y_train)
        pred_train = modelo.predict(X_train)
        pred_test  = modelo.predict(X_test)

        r2_tr = r2_score(y_train, pred_train)
        r2_te = r2_score(y_test,  pred_test)
        mse_te = mean_squared_error(y_test, pred_test)

        # ── Métricas ─────────────────────────────────────────────
        section_label("Métricas del modelo")
        c1, c2, c3 = st.columns(3)
        c1.metric("R² Entrenamiento", f"{r2_tr:.4f}")
        c2.metric("R² Prueba", f"{r2_te:.4f}")

        if algoritmo == "Regresión Lineal":
            c3.metric("Pendiente (coef)", f"{modelo.coef_[0]:.4e}")
        else:
            c3.metric("MSE Prueba", f"{mse_te:,.0f}")

        # ── Gráfica ──────────────────────────────────────────────
        section_label("Visualización del ajuste")
        _set_dark_style()
        fig, ax = plt.subplots(figsize=(8, 4))

        ax.scatter(X_train, y_train, color="#30363d", alpha=0.4,
                   label="Entrenamiento", s=18, edgecolors='none')
        ax.scatter(X_test,  y_test,  color="#4fc3f7", alpha=0.6,
                   label="Prueba (real)", s=22, edgecolors='none')

        idx   = np.argsort(X_test.iloc[:, 0])
        X_ord = X_test.iloc[idx]
        p_ord = pred_test[idx]
        ax.plot(X_ord, p_ord, color="#f85149", linewidth=2.5, label="Predicción")

        ax.set_xlabel(var_x, fontsize=10)
        ax.set_ylabel(var_y, fontsize=10)
        ax.set_title(f"{algoritmo} — Test {test_pct}%", color="#e6edf3", fontsize=13, pad=10)
        ax.legend(framealpha=0.8)
        ax.grid(True)
        fig.tight_layout()
        st.pyplot(fig)