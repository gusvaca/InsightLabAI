import streamlit as st

from core.session import obtener_dataset

from analytics.insights import InsightEngine
from components.layout import Layout


df = obtener_dataset()
Layout.render(

    "🧠 Hallazgos Automáticos",df

)

if df is None:

    st.warning("Primero carga un dataset.")

    st.stop()

insights = InsightEngine.generar(df)

st.subheader(f"Se encontraron {len(insights)} hallazgos")

st.divider()

for insight in insights:

    if insight["tipo"] == "success":

        st.success(
            f"**{insight['titulo']}**\n\n{insight['mensaje']}"
        )

    elif insight["tipo"] == "warning":

        st.warning(
            f"**{insight['titulo']}**\n\n{insight['mensaje']}"
        )

    elif insight["tipo"] == "error":

        st.error(
            f"**{insight['titulo']}**\n\n{insight['mensaje']}"
        )

    else:

        st.info(
            f"**{insight['titulo']}**\n\n{insight['mensaje']}"
        )