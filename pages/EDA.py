import streamlit as st

from core.session import obtener_dataset

from analytics.eda import EDAEngine
from analytics.insights.service import InsightService

from components.insight_overview import InsightOverview

from components.executive_report_viewer import ExecutiveReportViewer
from components.layout import Layout
from components.charts import (
    histograma,
    boxplot,
    densidad
)
from components.layout import Layout




df = obtener_dataset()
Layout.render(

    "📊 Análisis Exploratorio (EDA)",df

)
if df is None:

    st.warning("Primero carga un dataset.")

    st.stop()

analysis = InsightService.analyze_dataset(

    df

)
variables = EDAEngine.variables_numericas(df)

if len(variables) == 0:

    st.warning("No existen variables numéricas.")

    st.stop()

columna = st.selectbox(
    "Seleccione una variable",
    variables
)

st.plotly_chart(
    histograma(df, columna),
    use_container_width=True
)

c1, c2 = st.columns(2)

with c1:

    st.plotly_chart(
        boxplot(df, columna),
        use_container_width=True
    )

with c2:

    st.plotly_chart(
        densidad(df, columna),
        use_container_width=True
    )

st.divider()

st.subheader("Estadísticos")

estadisticas = EDAEngine.estadisticas(df, columna)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Media", estadisticas["Media"])
c2.metric("Mediana", estadisticas["Mediana"])
c3.metric("Mínimo", estadisticas["Mínimo"])
c4.metric("Máximo", estadisticas["Máximo"])

c1, c2, c3 = st.columns(3)

c1.metric("Q1", estadisticas["Q1"])
c2.metric("Q3", estadisticas["Q3"])
c3.metric(
    "Outliers",
    EDAEngine.cantidad_outliers(df, columna)
)
st.divider()

st.header("🧠 Insight Intelligence")

InsightOverview.render(

    analysis

)
st.divider()

ExecutiveReportViewer.render(

    analysis

)