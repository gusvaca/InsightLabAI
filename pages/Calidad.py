import streamlit as st

from analytics.quality import DataQuality

from analytics.missing import MissingAnalyzer

from core.session import obtener_dataset
from components.layout import Layout
from analytics.insights.service import InsightService

from components.insight_overview import InsightOverview

from components.executive_report_viewer import ExecutiveReportViewer
from components.charts import (

    grafico_nulos,

    barra_calidad

)



df = obtener_dataset()
Layout.render(

    "📊 Calidad de Datos",

    df

)
if df is None:

    st.warning("Primero carga un dataset.")

    st.stop()

score = DataQuality.score(df)

st.plotly_chart(

    barra_calidad(score),

    use_container_width=True

)

st.divider()

st.subheader("Valores Nulos")

st.plotly_chart(

    grafico_nulos(df),

    use_container_width=True

)

st.divider()

st.subheader("Resumen")

st.dataframe(

    MissingAnalyzer.resumen(df),

    use_container_width=True,

    hide_index=True

)
analysis = InsightService.analyze_quality(

    df

)
st.divider()

st.subheader("💡 Recomendaciones")

for r in DataQuality.recomendaciones(df):

    st.info(r)

    st.divider()

InsightOverview.render(

    analysis

)