import streamlit as st

from core.session import existe_dataset
from components.topbar import TopBar
st.title("🏠 Inicio")

st.write(
    """
Bienvenido a **InsightLab AI**.

Una plataforma para:

- Analítica Exploratoria
- Machine Learning
- Hallazgos Automáticos
- Visualizaciones
- Reportes Ejecutivos
"""
)

if existe_dataset():

    st.success("✅ Hay un dataset cargado.")

else:

    st.info("📂 Todavía no has cargado un dataset.")