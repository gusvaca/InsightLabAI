import streamlit as st

from core.session import obtener_dataset
from analytics.quality import DataQuality
from analytics.insights.engine import InsightEngine

from components.layout import Layout
from components.cards import kpi_card

from components.charts import (
    gauge,
    tipos_variables
)

st.set_page_config(layout="wide")

df = obtener_dataset()

if df is None:
    st.warning("Primero carga un dataset.")
    st.stop()

# ======================
# TopBar
# ======================

Layout.render(

    "📊 Dashboard",

    df

)

resumen = DataQuality.resumen(df)

# ======================
# KPIs
# ======================

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    kpi_card(
        "Registros",
        f"{resumen['filas']:,}",
        "📄",
        "#2563EB",
        "Total de registros"
    )

with c2:
    kpi_card(
        "Variables",
        resumen["columnas"],
        "📊",
        "#7C3AED",
        "Variables detectadas"
    )

with c3:
    kpi_card(
        "Memoria",
        f"{resumen['memoria']} MB",
        "💾",
        "#10B981",
        "Uso de memoria"
    )

with c4:
    kpi_card(
        "Calidad",
        f"{resumen['score']}/100",
        "🎯",
        "#F59E0B",
        resumen["estado"]
    )
    
    with c5:

        kpi_card(
        "Estado",
        resumen["estado"],
        "✅",
        "#22C55E",
        "Estado general"
    )

st.markdown("## 📊 Dashboard Ejecutivo")
st.caption("Resumen de calidad, estructura y hallazgos del dataset.")

# ======================
# Dashboard
# ======================

izquierda, derecha = st.columns([2, 1])

with izquierda:

    st.subheader("🎯 Data Health Score")

    st.plotly_chart(
        gauge(resumen["score"]),
        use_container_width=True
    )

    st.subheader("📊 Tipos de Variables")

    st.plotly_chart(
        tipos_variables(df),
        use_container_width=True
    )

with derecha:

    st.subheader("🧠 Hallazgos Destacados")

    from analytics.insights.service import InsightService

    analysis = InsightService.analyze_dataset(df)

    insights = analysis["resultado"].insights

if not insights:

    st.success("No se encontraron problemas.")

else:

    for insight in insights[:5]:

        if insight.prioridad.lower() == "alta":

            st.error(insight.mensaje)

        elif insight.prioridad.lower() == "media":

            st.warning(insight.mensaje)

        elif insight.prioridad.lower() == "baja":

            st.success(insight.mensaje)

        else:

            st.info(insight.mensaje)

    st.divider()

# ======================
# Calidad
# ======================

st.subheader("📋 Checklist del Dataset")

col1, col2 = st.columns(2)

with col1:

    if resumen["nulos"] == 0:
        st.success("✅ Sin valores nulos")
    else:
        st.warning(f"⚠ {resumen['nulos']} valores nulos")

    if resumen["duplicados"] == 0:
        st.success("✅ Sin duplicados")
    else:
        st.warning(f"⚠ {resumen['duplicados']} duplicados")

with col2:

    if resumen["score"] >= 90:
        st.success("✅ Calidad Excelente")

    elif resumen["score"] >= 70:
        st.warning("⚠ Calidad Buena")

    else:
        st.error("❌ Calidad Baja")

    st.info(f"💾 Memoria utilizada: {resumen['memoria']} MB")

st.divider()

st.subheader("📈 Estadísticos")

st.dataframe(
    df.describe(include="all").transpose(),
    use_container_width=True,
    height=450
)