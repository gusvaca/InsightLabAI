import streamlit as st

from analytics.insights.service import InsightService

from components.executive_report_viewer import ExecutiveReportViewer
from components.insight_overview import InsightOverview


st.set_page_config(
    page_title="Reportes Ejecutivos",
    page_icon="📑",
    layout="wide"
)

st.title("📑 Reportes Ejecutivos")
st.caption(
    "Reporte ejecutivo generado automáticamente por InsightLab AI."
)

# ==========================================================
# VALIDAR DATASET
# ==========================================================

if "df" not in st.session_state:

    st.warning(
        "⚠️ Primero cargue un conjunto de datos desde la página **Cargar Dataset**."
    )

    st.stop()

df = st.session_state.df

# ==========================================================
# GENERAR ANÁLISIS
# ==========================================================

with st.spinner("Generando análisis ejecutivo..."):

    analysis = InsightService.analyze_dataset(
        df
    )

# ==========================================================
# RESUMEN EJECUTIVO
# ==========================================================

InsightOverview.render(
    analysis
)

st.divider()

# ==========================================================
# REPORTE EJECUTIVO
# ==========================================================

ExecutiveReportViewer.render(
    analysis
)