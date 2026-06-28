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

st.title("📊 InsightLab AI")

st.caption("Intelligent Data Analytics Platform")

st.info(
    """
Bienvenido.

Esta plataforma permitirá:

• Analítica Exploratoria

• Machine Learning

• Hallazgos Automáticos

• IA sobre Datos

• Reportes Ejecutivos

Todo desde un único lugar.
"""
)

st.markdown("---")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Datasets", 0)

c2.metric("Reportes", 0)

c3.metric("Modelos", 0)

c4.metric("Insights", 0)

st.markdown("---")

st.success("Sprint 1 iniciado correctamente.")