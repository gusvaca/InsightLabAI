import streamlit as st

from ml.cluster_intelligence import ClusterIntelligence
from components.layout import Layout

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(

    page_title="Cluster Intelligence",

    page_icon="🧠",

    layout="wide"

)



# =====================================================
# VALIDACIÓN
# =====================================================

if "cluster_result" not in st.session_state:

    st.warning(

        """
        No existe un modelo de clustering.

        Primero ejecute un modelo desde la página
        🤖 Machine Learning.
        """

    )

    st.stop()

resultado = st.session_state["cluster_result"]
Layout.render(

    "🧠 Cluster Intelligence"


)

engine = ClusterIntelligence(

    resultado

)
# =====================================================
# DASHBOARD EJECUTIVO
# =====================================================

st.divider()

st.subheader("📊 Executive Dashboard")

benchmark = engine.cluster_benchmark()

mejor = benchmark.iloc[0]

kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

with kpi1:

    st.metric(

        "🏆 Mejor Cluster",

        int(mejor["Cluster"])

    )

with kpi2:

    st.metric(

        "⭐ Overall",

        f"{mejor['Overall Score']:.2f}"

    )

with kpi3:

    st.metric(

        "💼 Business",

        f"{mejor['Business Score']:.2f}"

    )

with kpi4:

    st.metric(

        "🎯 Opportunity",

        f"{mejor['Opportunity Score']:.2f}"

    )

with kpi5:

    st.metric(

        "🛡 Confidence",

        f"{mejor['Confidence']:.2f}"

    )

st.divider()

st.subheader("🏅 Benchmark de Clusters")

st.dataframe(

    benchmark,

    use_container_width=True,

    height=320

)

# =====================================================
# EXPLAINABILITY
# =====================================================

st.divider()

st.subheader("🧠 Explainability")

cluster = st.selectbox(

    "Seleccione un Cluster",

    options=engine.clusters,

    key="cluster_detail"

)

detalle = engine.explain_cluster(cluster)

m1, m2, m3, m4, m5 = st.columns(5)

with m1:

    st.metric(

        "Business",

        f"{detalle['Business Score']:.2f}"

    )

with m2:

    st.metric(

        "Risk",

        f"{detalle['Risk Score']:.2f}"

    )

with m3:

    st.metric(

        "Opportunity",

        f"{detalle['Opportunity Score']:.2f}"

    )

with m4:

    st.metric(

        "Stability",

        f"{detalle['Stability']:.2f}"

    )

with m5:

    st.metric(

        "Confidence",

        f"{detalle['Confidence']:.2f}"

    )

st.divider()

st.subheader("🏅 Variables Más Importantes")

st.dataframe(

    detalle["Top Variables"],

    use_container_width=True,

    height=300

)
# =====================================================
# COMPARATIVO EJECUTIVO
# =====================================================

st.divider()

st.subheader("📈 Comparativo Ejecutivo de Clusters")

comparativo = engine.explain_all_clusters()

st.dataframe(

    comparativo,

    use_container_width=True,

    height=320

)

st.divider()

st.subheader("🏆 Resumen Ejecutivo")

mejor = comparativo.iloc[0]

peor = comparativo.iloc[-1]

c1, c2 = st.columns(2)

with c1:

    st.success(

        f"""
### 🥇 Mejor Cluster

**Cluster:** {int(mejor['Cluster'])}

**Business Score:** {mejor['Business Score']:.2f}

**Opportunity Score:** {mejor['Opportunity Score']:.2f}

**Confidence:** {mejor['Confidence']:.2f}

**Variable Principal:** {mejor['Main Variable']}
"""

    )

with c2:

    st.warning(

        f"""
### ⚠ Cluster a Revisar

**Cluster:** {int(peor['Cluster'])}

**Business Score:** {peor['Business Score']:.2f}

**Opportunity Score:** {peor['Opportunity Score']:.2f}

**Confidence:** {peor['Confidence']:.2f}

**Variable Principal:** {peor['Main Variable']}
"""

    )

    # =====================================================
# EXECUTIVE REPORT
# =====================================================

st.divider()

st.subheader("📑 Executive Report")

reporte = engine.executive_report()

# =====================================================
# RESUMEN GENERAL
# =====================================================

st.markdown("### 📊 Resumen General")

resumen = reporte["Summary"]

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(

        "📄 Registros",

        resumen["Records"]

    )

with c2:

    st.metric(

        "📊 Variables",

        resumen["Variables"]

    )

with c3:

    st.metric(

        "🤖 Clusters",

        resumen["Clusters"]

    )

with c4:

    st.metric(

        "💾 Memoria",

        f"{resumen['Memory (MB)']} MB"

    )

st.divider()

# =====================================================
# RANKING ESTADÍSTICO
# =====================================================

st.subheader("📈 Ranking Estadístico")

st.dataframe(

    reporte["Statistical Ranking"],

    use_container_width=True,

    height=320

)

st.divider()

# =====================================================
# BENCHMARK EJECUTIVO
# =====================================================

st.subheader("🏆 Benchmark Ejecutivo")

st.dataframe(

    reporte["Benchmark"],

    use_container_width=True,

    height=320

)

st.divider()

# =====================================================
# DETALLE DE LOS CLUSTERS
# =====================================================

st.subheader("📋 Detalle de Todos los Clusters")

for cluster, detalle in reporte["Cluster Details"].items():

    with st.expander(

        f"Cluster {cluster}",

        expanded=False

    ):

        c1, c2, c3, c4, c5 = st.columns(5)

        with c1:

            st.metric(

                "Business",

                f"{detalle['Business Score']:.2f}"

            )

        with c2:

            st.metric(

                "Risk",

                f"{detalle['Risk Score']:.2f}"

            )

        with c3:

            st.metric(

                "Opportunity",

                f"{detalle['Opportunity Score']:.2f}"

            )

        with c4:

            st.metric(

                "Stability",

                f"{detalle['Stability']:.2f}"

            )

        with c5:

            st.metric(

                "Confidence",

                f"{detalle['Confidence']:.2f}"

            )

        st.markdown("#### Variables más importantes")

        st.dataframe(

            detalle["Top Variables"],

            use_container_width=True,

            height=220

        )