import streamlit as st

from core.session import obtener_dataset
from analytics.quality import DataQuality
from analytics.insights.service import InsightService

from components.layout import Layout
from components.cards import kpi_card

from components.charts import (
    gauge,
    tipos_variables
)

st.set_page_config(
    layout="wide"
)

# =====================================================
# DATASET
# =====================================================

df = obtener_dataset()

if df is None:

    st.warning(
        "Primero carga un dataset."
    )

    st.stop()

# =====================================================
# LAYOUT
# =====================================================

Layout.render(

    "📊 Dashboard Ejecutivo",

    df

)

# =====================================================
# INFORMACIÓN GENERAL
# =====================================================

resumen = DataQuality.resumen(df)

analysis = InsightService.analyze_dataset(df)

resultado = analysis["resultado"]

# =====================================================
# HEADER
# =====================================================

st.title("📊 Dashboard Ejecutivo")

st.markdown("""
### InsightLab AI Intelligence Platform

Panel ejecutivo para evaluar la calidad, estructura,
estado y preparación de un conjunto de datos para
proyectos de Analítica, Machine Learning e Inteligencia Artificial.
""")

st.progress(
    resumen["score"] / 100
)

st.caption(
    f"Estado General del Dataset: **{resumen['estado']}**"
)

st.divider()

# =====================================================
# KPIs
# =====================================================

k1, k2, k3, k4, k5 = st.columns(5)

with k1:

    kpi_card(

        "Registros",

        f"{resumen['filas']:,}",

        "📄",

        "#2563EB",

        "Número total de registros"

    )


with k2:

    kpi_card(

        "Variables",

        resumen["columnas"],

        "📊",

        "#7C3AED",

        "Columnas detectadas"

    )


with k3:

    kpi_card(

        "Memoria",

        f"{resumen['memoria']} MB",

        "💾",

        "#10B981",

        "Consumo de memoria"

    )


with k4:

    kpi_card(

        "Calidad",

        f"{resumen['score']}/100",

        "🎯",

        "#F59E0B",

        "Data Health Score"

    )


with k5:

    kpi_card(

        "Estado",

        resumen["estado"],

        "✅",

        "#22C55E",

        "Estado general"

    )

st.divider()

# =====================================================
# PANEL EJECUTIVO
# =====================================================

st.header("🧠 Visión Ejecutiva del Dataset")

c1, c2 = st.columns([2, 1])

# =====================================================
# COLUMNA IZQUIERDA
# =====================================================

with c1:

    st.subheader("🎯 Data Health Score")

    st.plotly_chart(

        gauge(
            resumen["score"]
        ),

        use_container_width=True

    )

    st.subheader("📊 Distribución de Tipos de Variables")

    st.plotly_chart(

        tipos_variables(df),

        use_container_width=True

    )

# =====================================================
# COLUMNA DERECHA
# =====================================================

with c2:

    st.subheader("🏥 Estado del Dataset")

    if resumen["score"] >= 90:

        st.success(
            "✅ Excelente calidad de datos."
        )

    elif resumen["score"] >= 70:

        st.warning(
            "⚠ Buena calidad. Se recomienda una revisión antes del entrenamiento."
        )

    else:

        st.error(
            "❌ Calidad insuficiente. Se recomienda ejecutar procesos de limpieza."
        )

    st.metric(

        "Registros",

        resumen["filas"]

    )

    st.metric(

        "Variables",

        resumen["columnas"]

    )

    st.metric(

        "Valores Nulos",

        resumen["nulos"]

    )

    st.metric(

        "Duplicados",

        resumen["duplicados"]

    )

st.divider()

# =====================================================
# HALLAZGOS
# =====================================================

st.subheader("🧠 Hallazgos Inteligentes")

if len(resultado.insights) == 0:

    st.success(
        "No se identificaron hallazgos relevantes."
    )

else:

    for insight in resultado.insights[:5]:

        prioridad = insight.prioridad.lower()

        titulo = f"{insight.icono} {insight.titulo}"

        if prioridad == "alta":

            st.error(titulo)

        elif prioridad == "media":

            st.warning(titulo)

        else:

            st.success(titulo)

        st.caption(insight.mensaje)

        if insight.recomendacion:

            st.info(
                f"💡 {insight.recomendacion}"
            )

st.divider()
# =====================================================
# FORTALEZAS - RIESGOS
# =====================================================

c1, c2 = st.columns(2)

with c1:

    st.subheader("💪 Fortalezas Detectadas")

    if resultado.fortalezas:

        for fortaleza in resultado.fortalezas:

            st.success(fortaleza)

    else:

        st.info(
            "No existen fortalezas registradas."
        )


with c2:

    st.subheader("⚠ Riesgos Identificados")

    if resultado.riesgos:

        for riesgo in resultado.riesgos:

            st.warning(riesgo)

    else:

        st.success(
            "No se identificaron riesgos."
        )

st.divider()


# =====================================================
# RECOMENDACIONES
# =====================================================

st.subheader("💡 Recomendaciones Inteligentes")

if resultado.recomendaciones:

    for recomendacion in resultado.recomendaciones:

        st.info(recomendacion)

else:

    st.success(
        "No existen recomendaciones."
    )

st.divider()


# =====================================================
# PRÓXIMOS PASOS
# =====================================================

st.subheader("🚀 Próximos Pasos")

if resultado.proximos_pasos:

    for paso in resultado.proximos_pasos:

        st.write(f"✅ {paso}")

else:

    st.success(
        "No existen próximos pasos definidos."
    )

st.divider()


# =====================================================
# CHECKLIST EJECUTIVO
# =====================================================

st.header("📋 Estado General del Dataset")

c1, c2, c3, c4 = st.columns(4)

with c1:

    if resumen["nulos"] == 0:

        st.success("✅ Sin Nulos")

    else:

        st.warning(f"⚠ {resumen['nulos']} Nulos")


with c2:

    if resumen["duplicados"] == 0:

        st.success("✅ Sin Duplicados")

    else:

        st.warning(f"⚠ {resumen['duplicados']} Duplicados")


with c3:

    if resumen["score"] >= 90:

        st.success("✅ Calidad Excelente")

    elif resumen["score"] >= 70:

        st.warning("⚠ Calidad Buena")

    else:

        st.error("❌ Calidad Baja")


with c4:

    st.info(
        f"💾 {resumen['memoria']} MB"
    )

st.divider()


# =====================================================
# ESTADÍSTICOS
# =====================================================

st.header("📈 Resumen Estadístico")

st.dataframe(

    df.describe(include="all").transpose(),

    use_container_width=True,

    height=450

)

st.divider()


# =====================================================
# INFORMACIÓN EJECUTIVA
# =====================================================

st.header("📌 Información Ejecutiva")

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(

        "Hallazgos",

        len(resultado.insights)

    )

with c2:

    st.metric(

        "Fortalezas",

        len(resultado.fortalezas)

    )

with c3:

    st.metric(

        "Riesgos",

        len(resultado.riesgos)

    )

with c4:

    st.metric(

        "Recomendaciones",

        len(resultado.recomendaciones)

    )

st.divider()

st.caption(
    "InsightLab AI © 2026 | Dashboard Ejecutivo generado automáticamente por el Insight Intelligence Engine."
)