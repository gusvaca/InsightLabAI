import streamlit as st

from core.session import obtener_dataset

from analytics.statistics import Statistics
from analytics.insights.service import InsightService

from components.insight_overview import InsightOverview

from components.executive_report_viewer import ExecutiveReportViewer
from components.layout import Layout
from components.charts import (

    heatmap_correlation,

    grafico_outliers

)

df = obtener_dataset()

Layout.render(

    "📈 Estadísticas Inteligentes",

    df

)

if df is None:

    st.warning("Primero carga un dataset.")

    st.stop()

corr = Statistics.correlation(df)
analysis = InsightService.analyze_dataset(

    df

)
if corr.empty:

    st.warning("No existen variables numéricas.")

    st.stop()

tab1, tab2, tab3 = st.tabs([

    "Correlaciones",

    "Skewness",

    "Outliers"

])

with tab1:

    st.plotly_chart(

        heatmap_correlation(corr),

        use_container_width=True

    )

with tab2:

    st.dataframe(

        Statistics.skewness(df),

        use_container_width=True,

        hide_index=True

    )

with tab3:

    st.plotly_chart(

        grafico_outliers(

            Statistics.outliers(df)

        ),

        use_container_width=True

    )
    st.divider()

InsightOverview.render(

    analysis

)
st.divider()

ExecutiveReportViewer.render(

    analysis

)