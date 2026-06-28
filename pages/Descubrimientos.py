import streamlit as st

from core.session import obtener_dataset

from analytics.discovery import DiscoveryEngine
from components.layout import Layout


df = obtener_dataset()
Layout.render(

    "🔎 Descubrimientos Inteligentes",

    df

)
if df is None:

    st.warning("Primero carga un dataset.")

    st.stop()

descubrimientos = DiscoveryEngine.generar(df)

st.success(

    f"Se encontraron {len(descubrimientos)} descubrimientos."

)

st.divider()

for d in descubrimientos:

    if d["tipo"] == "success":

        st.success(

            f"### {d['titulo']}\n\n{d['mensaje']}"

        )

    elif d["tipo"] == "warning":

        st.warning(

            f"### {d['titulo']}\n\n{d['mensaje']}"

        )

    elif d["tipo"] == "error":

        st.error(

            f"### {d['titulo']}\n\n{d['mensaje']}"

        )

    else:

        st.info(

            f"### {d['titulo']}\n\n{d['mensaje']}"

        )