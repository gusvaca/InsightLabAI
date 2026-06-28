import streamlit as st

from core.session import obtener_dataset
from components.layout import Layout

from analytics.insights.service import InsightService


df = obtener_dataset()

Layout.render(
    "🧠 Hallazgos Inteligentes",
    df
)

if df is None:

    st.warning("Primero carga un dataset.")

    st.stop()


with st.spinner("Analizando información..."):

    analysis = InsightService.analyze_dataset(df)


# =====================================================
# RESUMEN EJECUTIVO
# =====================================================

st.subheader("📋 Resumen Ejecutivo")

st.info(

    analysis["resumen"]

)

st.divider()


# =====================================================
# NIVEL DE MADUREZ
# =====================================================

st.subheader("📈 Nivel de Madurez")

madurez = analysis["madurez"]

if isinstance(madurez, dict):

    for k, v in madurez.items():

        if isinstance(v, (int, float)):

            st.metric(

                k.replace("_", " ").title(),

                v

            )

        else:

            st.write(

                f"**{k}:** {v}"

            )

else:

    st.write(madurez)

st.divider()


# =====================================================
# INTERPRETACIÓN DEL NEGOCIO
# =====================================================

st.subheader("💼 Interpretación del Negocio")

negocio = analysis["negocio"]

if isinstance(negocio, dict):

    for k, v in negocio.items():

        st.write(

            f"**{k}:** {v}"

        )

else:

    st.write(

        negocio

    )

st.divider()


# =====================================================
# HISTORIA
# =====================================================

st.subheader("📖 Historia del Dataset")

st.write(

    analysis["historia"]

)

st.divider()


# =====================================================
# RECOMENDACIONES
# =====================================================

st.subheader("💡 Recomendaciones")

resultado = analysis["resultado"]

if isinstance(resultado, dict):

    recomendaciones = resultado.get(

        "recomendaciones",

        []

    )

    if recomendaciones:

        for r in recomendaciones:

            st.success(r)

    else:

        st.info(

            "No existen recomendaciones."

        )

else:

    st.write(resultado)

st.divider()


# =====================================================
# PRÓXIMOS PASOS
# =====================================================

st.subheader("🚀 Próximos Pasos")

pasos = analysis["siguientes_pasos"]

if isinstance(pasos, list):

    for paso in pasos:

        st.write(

            f"• {paso}"

        )

else:

    st.write(

        pasos

    )