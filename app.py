import streamlit as st

from config import *

st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout=LAYOUT,
    initial_sidebar_state=SIDEBAR
)

def cargar_css():

    try:

        with open("style.css", "r", encoding="utf-8") as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

    except FileNotFoundError:

        pass


cargar_css()
from components.sidebar import sidebar

sidebar()

st.title("🚀 InsightLab AI")

st.markdown(
    """
### Plataforma Inteligente para Analítica de Datos, Calidad de Datos y Machine Learning

**InsightLab AI** es una plataforma desarrollada por **Gustavo Vaca** para facilitar el análisis integral de datos mediante técnicas de Analítica, Ciencia de Datos e Inteligencia Artificial.

La solución integra en una única plataforma herramientas para exploración de datos, evaluación de calidad, limpieza inteligente, entrenamiento de modelos de Machine Learning y generación automática de hallazgos ejecutivos, permitiendo acelerar el ciclo completo de análisis desde la carga del dataset hasta la obtención de conclusiones y reportes.
"""
)

st.divider()

st.subheader("🎯 Capacidades Principales")

col1, col2 = st.columns(2)

with col1:

    st.success("📂 Carga de múltiples formatos")
    st.success("🧹 Limpieza Inteligente de Datos")
    st.success("📊 Estadísticas Descriptivas")
    st.success("📈 Análisis Exploratorio de Datos (EDA)")
    st.success("✅ Evaluación de Calidad de Datos")
    st.success("🔍 Detección automática de problemas")

with col2:

    st.success("🤖 Machine Learning")
    st.success("🧠 Insight Intelligence Engine")
    st.success("📑 Reportes Ejecutivos")
    st.success("📉 Visualizaciones Interactivas")
    st.success("💡 Recomendaciones automáticas")
    st.success("⚙️ Preparación de datos para IA")

st.divider()

st.subheader("⭐ Características Diferenciadoras")

st.markdown("""
- Motor propio de análisis inteligente basado en reglas.
- Evaluación automática de la calidad de los datos.
- Centro de limpieza inteligente para preparación de datasets.
- Generación automática de insights y recomendaciones.
- Reportes ejecutivos orientados a la toma de decisiones.
- Arquitectura modular y escalable.
- Preparación de datos para proyectos de Machine Learning.
- Exportación de resultados y datasets procesados.
""")

st.divider()

st.subheader("📌 Flujo de Trabajo")

st.markdown("""

1. 📂 Cargar Dataset

2. 🧹 Limpiar Datos

3. ✅ Evaluar Calidad

4. 📊 Explorar Información

5. 🤖 Entrenar Modelos

6. 🧠 Generar Insights

7. 📑 Exportar Reportes

""")

st.divider()

if "df" in st.session_state:

    st.success(
        "✅ Existe un conjunto de datos cargado y listo para su análisis."
    )

else:

    st.info(
        "📂 Aún no existe un conjunto de datos cargado. Utilice la opción **Cargar Dataset** del menú lateral para comenzar."
    )

st.divider()

st.caption(
    "InsightLab AI © 2026 | Desarrollado por Gustavo Vaca | Plataforma para Analítica de Datos, Calidad de Datos e Inteligencia Artificial."
)

