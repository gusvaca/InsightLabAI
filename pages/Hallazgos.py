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


resultado = analysis["resultado"]


# ===========================================================
# HEADER
# ===========================================================

st.title("🧠 Insight Intelligence Engine")

st.caption(
    "Hallazgos automáticos generados por InsightLab AI"
)

st.divider()


# ===========================================================
# SCORE
# ===========================================================

c1, c2 = st.columns(2)

c1.metric(

    "Score",

    resultado.score

)

c2.metric(

    "Estado",

    resultado.estado

)

st.divider()


# ===========================================================
# RESUMEN
# ===========================================================

st.subheader(

    "📋 Resumen Ejecutivo"

)

st.info(

    resultado.resumen

)

st.divider()


# ===========================================================
# HALLAZGOS
# ===========================================================

st.subheader(

    "🔍 Hallazgos Detectados"

)

if len(resultado.insights) == 0:

    st.success(

        "No se encontraron hallazgos."

    )

else:

    for insight in resultado.insights:

        texto = f"""
### {insight.icono} {insight.titulo}

**Categoría:** {insight.categoria}

**Prioridad:** {insight.prioridad}

{insight.mensaje}
"""

        prioridad = insight.prioridad.lower()

        if prioridad == "alta":

            st.error(texto)

        elif prioridad == "media":

            st.warning(texto)

        else:

            st.success(texto)

        if insight.recomendacion:

            st.caption(

                f"💡 {insight.recomendacion}"

            )

st.divider()


# ===========================================================
# FORTALEZAS
# ===========================================================

st.subheader(

    "✅ Fortalezas"

)

if resultado.fortalezas:

    for item in resultado.fortalezas:

        st.success(item)

else:

    st.info(

        "No existen fortalezas registradas."

    )

st.divider()


# ===========================================================
# RIESGOS
# ===========================================================

st.subheader(

    "⚠ Riesgos"

)

if resultado.riesgos:

    for item in resultado.riesgos:

        st.warning(item)

else:

    st.success(

        "No se identificaron riesgos."

    )

st.divider()


# ===========================================================
# RECOMENDACIONES
# ===========================================================

st.subheader(

    "💡 Recomendaciones"

)

if resultado.recomendaciones:

    for item in resultado.recomendaciones:

        st.info(item)

else:

    st.success(

        "No existen recomendaciones."

    )

st.divider()


# ===========================================================
# PRÓXIMOS PASOS
# ===========================================================

st.subheader(

    "🚀 Próximos Pasos"

)

if resultado.proximos_pasos:

    for paso in resultado.proximos_pasos:

        st.write(

            f"• {paso}"

        )

else:

    st.success(

        "No existen próximos pasos definidos."

    )

st.divider()


# ===========================================================
# INFORMACIÓN ADICIONAL
# ===========================================================

st.subheader(

    "📊 Información del Análisis"

)

st.write(

    f"**Hallazgos:** {len(resultado.insights)}"

)

st.write(

    f"**Fortalezas:** {len(resultado.fortalezas)}"

)

st.write(

    f"**Riesgos:** {len(resultado.riesgos)}"

)

st.write(

    f"**Recomendaciones:** {len(resultado.recomendaciones)}"

)

st.write(

    f"**Próximos pasos:** {len(resultado.proximos_pasos)}"

)