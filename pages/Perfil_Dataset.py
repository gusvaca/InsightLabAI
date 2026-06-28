import streamlit as st

from core.session import obtener_dataset

from analytics.profiler import DataProfiler
from components.layout import Layout


df = obtener_dataset()
Layout.render(

    "📋 Perfil del Dataset",

    df

)
if df is None:

    st.warning("Primero carga un dataset.")

    st.stop()
c1, c2, c3 = st.columns(3)

c1.metric(
    "Variables",
    len(df.columns)
)

c2.metric(
    "Numéricas",
    len(df.select_dtypes("number").columns)
)

c3.metric(
    "Texto",
    len(df.select_dtypes("object").columns)
)

st.divider()
perfil = DataProfiler.profile(df)

st.success(
    f"Se analizaron {len(df.columns)} columnas."
)

st.dataframe(

    perfil,

    use_container_width=True,

    hide_index=True

)