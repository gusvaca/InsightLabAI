import streamlit as st

from core.session import obtener_dataset

from analytics.visualization import VisualizationEngine

from ml.clustering import ClusteringEngine
from ml.anomaly import AnomalyEngine
from ml.cluster_intelligence import ClusterIntelligence

from components.loading import LoadingManager
from components.layout import Layout
from analytics.insights.service import InsightService

from components.insight_overview import InsightOverview

from components.executive_report_viewer import ExecutiveReportViewer

from components.charts import (
    scatter_cluster,
    scatter_anomaly
)

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="Machine Learning",
    page_icon="🤖",
    layout="wide"
)



# =====================================================
# DATASET
# =====================================================

df = obtener_dataset()

Layout.render(

    "🤖 Machine Learning",

    df

)

if df is None:

    st.warning(
        "Primero carga un dataset."
    )

    st.stop()
    
numericas = VisualizationEngine.numericas(df)
analysis = InsightService.analyze_dataset(

    df

)

if len(numericas) < 2:

    st.warning(
        "El dataset debe contener al menos dos variables numéricas."
    )

    st.stop()

# =====================================================
# PESTAÑAS
# =====================================================

tab_cluster, tab_anomalias = st.tabs(
    [
        "🤖 Clustering",
        "🚨 Detección de Anomalías"
    ]
)
# =====================================================
# CLUSTERING
# =====================================================

with tab_cluster:

    st.subheader("⚙ Configuración del Modelo")

    col1, col2 = st.columns([3, 1])

    with col1:

        columnas_cluster = st.multiselect(

            "Variables para el modelo",

            numericas,

            default=numericas[:2],

            key="cluster_variables"

        )

    with col2:

        numero_clusters = st.slider(

            "Número de Clusters",

            min_value=2,

            max_value=10,

            value=3,

            step=1

        )

    ejecutar_cluster = st.button(

        "🚀 Ejecutar Clustering",

        type="primary",

        use_container_width=True

    )

    if ejecutar_cluster:

        if len(columnas_cluster) < 2:

            st.warning(

                "Seleccione al menos dos variables."

            )

            st.stop()

        LoadingManager.progress(

            [

                "Preparando datos",

                "Normalizando variables",

                "Entrenando modelo K-Means",

                "Generando clusters",

                "Calculando inteligencia",

                "Construyendo dashboard"

            ]

        )

        with LoadingManager.simple(

            "Procesando modelo de Machine Learning..."

        ):

            resultado_cluster = ClusteringEngine.ejecutar(

                df,

                columnas_cluster,

                numero_clusters

            )

            st.session_state["cluster_result"] = resultado_cluster

            inteligencia = ClusterIntelligence(

                resultado_cluster

            )

        st.success(

            "✅ Modelo de clustering generado correctamente."

        )
                # =====================================================
        # DATASET CLUSTERIZADO
        # =====================================================

        st.divider()

        st.subheader("📄 Dataset Clusterizado")

        st.dataframe(

            resultado_cluster,

            use_container_width=True,

            height=350

        )

        # =====================================================
        # INDICADORES EJECUTIVOS
        # =====================================================

        benchmark = inteligencia.cluster_benchmark()

        mejor_cluster = benchmark.iloc[0]

        kpi1, kpi2, kpi3, kpi4 = st.columns(4)

        with kpi1:

            st.metric(

                "🏆 Mejor Cluster",

                int(mejor_cluster["Cluster"])

            )

        with kpi2:

            st.metric(

                "⭐ Overall Score",

                f"{mejor_cluster['Overall Score']:.2f}"

            )

        with kpi3:

            st.metric(

                "💼 Business Score",

                f"{mejor_cluster['Business Score']:.2f}"

            )

        with kpi4:

            st.metric(

                "🎯 Opportunity",

                f"{mejor_cluster['Opportunity Score']:.2f}"

            )

        # =====================================================
        # VISUALIZACIÓN
        # =====================================================

        st.divider()

        st.subheader("📊 Visualización de Clusters")

        if len(columnas_cluster) >= 2:

            st.plotly_chart(

                scatter_cluster(

                    resultado_cluster,

                    columnas_cluster[0],

                    columnas_cluster[1]

                ),

                use_container_width=True

            )

        # =====================================================
        # BENCHMARK
        # =====================================================

        st.divider()

        st.subheader("🏅 Benchmark de Clusters")

        st.dataframe(

            benchmark,

            use_container_width=True,

            height=280

        )

                # =====================================================
        # EXPLICACIÓN EJECUTIVA
        # =====================================================

        st.divider()

        st.subheader("🧠 Inteligencia del Modelo")

        cluster_seleccionado = st.selectbox(

            "Seleccione un Cluster",

            options=inteligencia.clusters,

            key="cluster_selector"

        )

        explicacion = inteligencia.explain_cluster(

            cluster_seleccionado

        )

        m1, m2, m3, m4, m5 = st.columns(5)

        with m1:

            st.metric(

                "Business",

                f"{explicacion['Business Score']:.2f}"

            )

        with m2:

            st.metric(

                "Risk",

                f"{explicacion['Risk Score']:.2f}"

            )

        with m3:

            st.metric(

                "Opportunity",

                f"{explicacion['Opportunity Score']:.2f}"

            )

        with m4:

            st.metric(

                "Stability",

                f"{explicacion['Stability']:.2f}"

            )

        with m5:

            st.metric(

                "Confidence",

                f"{explicacion['Confidence']:.2f}"

            )

        st.markdown("### 📈 Variables más importantes")

        st.dataframe(

            explicacion["Top Variables"],

            use_container_width=True,

            height=260

        )

        st.divider()

        st.subheader("📊 Resumen Ejecutivo de Todos los Clusters")

        resumen = inteligencia.explain_all_clusters()

        st.dataframe(

            resumen,

            use_container_width=True,

            height=280

        )
                # =====================================================
        # EXECUTIVE REPORT
        # =====================================================

        st.divider()

        st.subheader("📑 Executive Report")

        reporte = inteligencia.executive_report()

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

                "💾 Memoria (MB)",

                resumen["Memory (MB)"]

            )

        st.divider()

        st.subheader("🏆 Ranking Estadístico")

        st.dataframe(

            reporte["Statistical Ranking"],

            use_container_width=True,

            height=300

        )

        st.divider()

        st.subheader("📈 Benchmark Ejecutivo")

        st.dataframe(

            reporte["Benchmark"],

            use_container_width=True,

            height=280

        )

        st.divider()

        st.subheader("🔍 Detalle Ejecutivo por Cluster")

        cluster = st.selectbox(

            "Cluster",

            options=list(

                reporte["Cluster Details"].keys()

            ),

            key="executive_cluster"

        )

        detalle = reporte["Cluster Details"][cluster]

        d1, d2, d3, d4, d5 = st.columns(5)

        with d1:

            st.metric(

                "Business",

                f"{detalle['Business Score']:.2f}"

            )

        with d2:

            st.metric(

                "Risk",

                f"{detalle['Risk Score']:.2f}"

            )

        with d3:

            st.metric(

                "Opportunity",

                f"{detalle['Opportunity Score']:.2f}"

            )

        with d4:

            st.metric(

                "Stability",

                f"{detalle['Stability']:.2f}"

            )

        with d5:

            st.metric(

                "Confidence",

                f"{detalle['Confidence']:.2f}"

            )

        st.markdown("### 📊 Variables más relevantes")

        st.dataframe(

            detalle["Top Variables"],

            use_container_width=True,

            height=250

        )
        st.divider()

st.header("🧠 Insight Intelligence")

InsightOverview.render(

    analysis

)
st.divider()

ExecutiveReportViewer.render(

    analysis

)