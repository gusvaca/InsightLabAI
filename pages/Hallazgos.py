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

    st.warning(

        "Primero cargue un dataset."

    )

    st.stop()


with st.spinner(

    "Analizando información..."

):

    analysis = InsightService.analyze_dataset(

        df

    )


# ======================================================
# CABECERA
# ======================================================

c1, c2 = st.columns(2)

c1.metric(

    "Score de Calidad",

    f"{analysis.score:.0f}/100"

)

c2.metric(

    "Estado",

    analysis.estado

)

st.divider()


# ======================================================
# RESUMEN
# ======================================================

st.subheader(

    "📋 Resumen Ejecutivo"

)

st.info(

    analysis.resumen

)

st.divider()


# ======================================================
# HALLAZGOS
# ======================================================

st.subheader(

    "🔍 Hallazgos Detectados"

)

if len(analysis.insights) == 0:

    st.success(

        "No se identificaron hallazgos relevantes."

    )

else:

    for insight in analysis.insights:

        prioridad = insight.prioridad.lower()

        texto = f"""
### {insight.icono} {insight.titulo}

**Categoría:** {insight.categoria}

**Prioridad:** {insight.prioridad}

{insight.mensaje}
"""

        if prioridad == "alta":

            st.error(texto)

        elif prioridad == "media":

            st.warning(texto)

        else:

            st.success(texto)

st.divider()


# ======================================================
# FORTALEZAS
# ======================================================

st.subheader(

    "✅ Fortalezas"

)

if analysis.fortalezas:

    for item in analysis.fortalezas:

        st.success(item)

else:

    st.info(

        "No existen fortalezas registradas."

    )

st.divider()


# ======================================================
# RIESGOS
# ======================================================

st.subheader(

    "⚠ Riesgos"

)

if analysis.riesgos:

    for item in analysis.riesgos:

        st.warning(item)

else:

    st.success(

        "No se identificaron riesgos."

    )

st.divider()


# ======================================================
# RECOMENDACIONES
# ======================================================

st.subheader(

    "💡 Recomendaciones"

)

if analysis.recomendaciones:

    for item in analysis.recomendaciones:

        st.info(item)

else:

    st.success(

        "No existen recomendaciones adicionales."

    )

st.divider()


# ======================================================
# PRÓXIMOS PASOS
# ======================================================

st.subheader(

    "🚀 Próximos Pasos"

)

if analysis.proximos_pasos:

    for paso in analysis.proximos_pasos:

        st.write(

            f"• {paso}"

        )

else:

    st.success(

        "No existen próximos pasos definidos."

    )