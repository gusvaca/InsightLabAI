"""
=========================================================
InsightLab AI Enterprise
Archivo : ml_cluster_ui.py
Descripción:
Interfaz profesional para análisis de Clustering
=========================================================
"""

import streamlit as st

from analytics.visualization import VisualizationEngine

from components.loading import LoadingManager
from components.cards import kpi_card
from components.charts import scatter_cluster
from components.cluster_charts import ClusterCharts

from ml.clustering import ClusteringEngine
from ml.cluster_profile import ClusterProfile
from ml.cluster_ai import ClusterAI


class ClusterUI:

    @staticmethod
    def render(df):

        st.subheader("🧠 Clustering con K-Means")

        numericas = VisualizationEngine.numericas(df)

        columnas = st.multiselect(
            "Variables",
            numericas,
            default=numericas[:2],
            key="cluster_variables"
        )

        k = st.slider(
            "Número de Clusters",
            min_value=2,
            max_value=10,
            value=3,
            key="cluster_k"
        )

        ejecutar = st.button(
            "🚀 Ejecutar Clustering",
            use_container_width=True
        )

        if not ejecutar:
            return

        LoadingManager.progress([
            "Preparando datos",
            "Normalizando variables",
            "Entrenando K-Means",
            "Calculando centroides",
            "Generando análisis"
        ])

        with LoadingManager.simple("Entrenando modelo..."):

            resultado = ClusteringEngine.ejecutar(
                df,
                columnas,
                k
            )

        st.success("✅ Clustering ejecutado correctamente.")

        resumen = ClusterProfile.resumen(resultado)

        perfil = ClusterProfile.perfil(resultado)

        estadisticos = ClusterProfile.estadisticos(resultado)

        comparacion = ClusterProfile.comparacion(resultado)

        insights = ClusterAI.analizar(resultado)
    @staticmethod
    def resumen_ejecutivo(resultado, columnas):

        st.divider()

        st.subheader("📊 Resumen Ejecutivo")

        resumen = ClusterProfile.resumen(resultado)

        total_registros = len(resultado)

        total_clusters = resultado["Cluster"].nunique()

        mayor_cluster = resumen["Registros"].max()

        menor_cluster = resumen["Registros"].min()

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            kpi_card(

                "Clusters",

                total_clusters,

                "🧠",

                "#2563EB",

                "Clusters generados"

            )

        with c2:

            kpi_card(

                "Registros",

                f"{total_registros:,}",

                "📄",

                "#10B981",

                "Observaciones"

            )

        with c3:

            kpi_card(

                "Variables",

                len(columnas),

                "📊",

                "#7C3AED",

                "Variables utilizadas"

            )

        with c4:

            kpi_card(

                "Mayor Cluster",

                f"{mayor_cluster:,}",

                "🏆",

                "#F59E0B",

                "Registros"

            )

        st.divider()

        col1, col2 = st.columns([1,2])

        with col1:

            st.markdown("### Distribución")

            st.dataframe(

                resumen,

                use_container_width=True,

                height=250

            )

        with col2:

            st.plotly_chart(

                ClusterCharts.distribucion(

                    resultado

                ),

                use_container_width=True

            )

        st.info(

            f"""
Se identificaron **{total_clusters} clusters** a partir de
**{len(columnas)} variables**.

El cluster con mayor tamaño contiene
**{mayor_cluster:,} registros** mientras que el menor
contiene **{menor_cluster:,} registros**.
"""
        )
    @staticmethod
    def perfil_clusters(

        resultado,

        perfil,

        estadisticos,

        comparacion

    ):

        st.divider()

        st.subheader("👥 Perfil de los Clusters")

        tab1, tab2, tab3 = st.tabs([

            "📋 Perfil",

            "📊 Estadísticos",

            "📈 Comparación"

        ])

        # ==========================================
        # PERFIL PROMEDIO
        # ==========================================

        with tab1:

            st.markdown(
                "### Valores promedio por Cluster"
            )

            st.dataframe(

                perfil,

                use_container_width=True,

                height=450

            )

        # ==========================================
        # ESTADÍSTICOS
        # ==========================================

        with tab2:

            cluster = st.selectbox(

                "Seleccione un Cluster",

                sorted(resultado["Cluster"].unique()),

                key="cluster_estadistico"

            )

            datos = estadisticos[

                estadisticos["Cluster"] == cluster

            ]

            st.dataframe(

                datos,

                use_container_width=True,

                height=500

            )

        # ==========================================
        # COMPARACIÓN
        # ==========================================

        with tab3:

            st.dataframe(

                comparacion,

                use_container_width=True,

                height=500

            )

        st.divider()

        st.subheader("📌 Resumen por Cluster")

        resumen = ClusterProfile.resumen(resultado)

        for _, fila in resumen.iterrows():

            cluster = fila["Cluster"]

            registros = fila["Registros"]

            porcentaje = fila["Porcentaje"]

            with st.expander(

                f"Cluster {cluster} ({porcentaje:.2f}%)",

                expanded=False

            ):

                st.metric(

                    "Registros",

                    registros

                )

                datos = estadisticos[

                    estadisticos["Cluster"] == cluster

                ]

                st.dataframe(

                    datos,

                    use_container_width=True,

                    height=350

                )
    @staticmethod
    def visualizaciones(resultado):

        st.divider()

        st.subheader("📈 Visualizaciones Avanzadas")

        tab1, tab2, tab3, tab4, tab5 = st.tabs([

            "🔥 Heatmap",

            "🎯 Radar",

            "📦 Boxplots",

            "📊 Barras",

            "🎯 Centroides"

        ])

        # ==========================================
        # HEATMAP
        # ==========================================

        with tab1:

            st.plotly_chart(

                ClusterCharts.heatmap(

                    resultado

                ),

                use_container_width=True

            )

        # ==========================================
        # RADAR
        # ==========================================

        with tab2:

            st.plotly_chart(

                ClusterCharts.radar(

                    resultado

                ),

                use_container_width=True

            )

        # ==========================================
        # BOXPLOTS
        # ==========================================

        with tab3:

            st.plotly_chart(

                ClusterCharts.boxplots(

                    resultado

                ),

                use_container_width=True

            )

        # ==========================================
        # BARRAS
        # ==========================================

        with tab4:

            st.plotly_chart(

                ClusterCharts.barras_medias(

                    resultado

                ),

                use_container_width=True

            )

        # ==========================================
        # CENTROIDES
        # ==========================================

        with tab5:

            st.plotly_chart(

                ClusterCharts.centroides(

                    resultado

                ),

                use_container_width=True

            )

        st.info(
            """
Las visualizaciones permiten identificar rápidamente las diferencias
entre los clusters, evaluar su separación y comprender el comportamiento
promedio de cada segmento.
"""
        )

    @staticmethod
    def insights(insights):

        st.divider()

        st.subheader("🧠 Inteligencia Artificial del Modelo")

        if len(insights) == 0:

            st.success(
                "No se generaron insights."
            )

            return

        for insight in insights:

            with st.container(border=True):

                c1, c2 = st.columns([1,3])

                with c1:

                    st.metric(

                        "Cluster",

                        insight["Cluster"]

                    )

                    st.metric(

                        "Registros",

                        insight["Registros"]

                    )

                    st.metric(

                        "Participación",

                        f"{insight['Porcentaje']} %"

                    )

                with c2:

                    st.markdown(
                        f"### 📌 Variable dominante"
                    )

                    st.info(
                        insight["Variable Dominante"]
                    )

                    st.markdown(
                        "### 📈 Comportamiento"
                    )

                    st.write(
                        insight["Comportamiento"]
                    )

                    st.markdown(
                        "### 🎯 Homogeneidad"
                    )

                    st.success(
                        insight["Homogeneidad"]
                    )

                    st.markdown(
                        "### 📝 Interpretación"
                    )

                    st.write(
                        insight["Interpretación"]
                    )

                    st.markdown(
                        "### 💡 Recomendaciones"
                    )

                    for recomendacion in insight["Recomendaciones"]:

                        st.success(
                            "✔ " + recomendacion
                        )
    @staticmethod
    def executive_summary(

        resultado,

        resumen,

        perfil,

        insights

    ):

        st.divider()

        st.subheader("📋 Executive Summary")

        total_clusters = resultado["Cluster"].nunique()

        total = len(resultado)

        mayor = resumen.loc[
            resumen["Registros"].idxmax()
        ]

        menor = resumen.loc[
            resumen["Registros"].idxmin()
        ]

        st.info(

            f"""
El algoritmo **K-Means** identificó **{total_clusters} segmentos**
a partir de **{total:,} registros**.

El **Cluster {int(mayor['Cluster'])}**
es el de mayor tamaño y concentra
**{mayor['Porcentaje']:.2f}%** del dataset.

El **Cluster {int(menor['Cluster'])}**
es el de menor tamaño con
**{menor['Porcentaje']:.2f}%** de participación.

Los segmentos presentan características diferenciadas,
lo que indica que el modelo logró separar correctamente
la población analizada.
"""

        )

        st.markdown("### 📊 Resumen Ejecutivo")

        for item in insights:

            with st.container(border=True):

                st.markdown(
                    f"### Cluster {item['Cluster']}"
                )

                c1, c2 = st.columns(2)

                with c1:

                    st.metric(

                        "Participación",

                        f"{item['Porcentaje']} %"

                    )

                    st.metric(

                        "Registros",

                        item["Registros"]

                    )

                    st.metric(

                        "Homogeneidad",

                        item["Homogeneidad"]

                    )

                with c2:

                    st.markdown(

                        "**Variable dominante**"

                    )

                    st.write(

                        item["Variable Dominante"]

                    )

                    st.markdown(

                        "**Interpretación**"

                    )

                    st.write(

                        item["Interpretación"]

                    )

        st.success(
            "El análisis ejecutivo fue generado automáticamente."
        )
    @staticmethod
    def metricas_modelo(resultado, columnas):

        from sklearn.preprocessing import StandardScaler

        from sklearn.metrics import (
            silhouette_score,
            davies_bouldin_score,
            calinski_harabasz_score
        )

        st.divider()

        st.subheader("📐 Calidad del Modelo")

        X = resultado[columnas].copy()

        X = StandardScaler().fit_transform(X)

        labels = resultado["Cluster"]

        silhouette = silhouette_score(X, labels)

        davies = davies_bouldin_score(X, labels)

        calinski = calinski_harabasz_score(X, labels)

        if silhouette >= 0.70:

            estado = "🟢 Excelente"

        elif silhouette >= 0.50:

            estado = "🟡 Bueno"

        elif silhouette >= 0.30:

            estado = "🟠 Regular"

        else:

            estado = "🔴 Deficiente"

        c1, c2, c3, c4 = st.columns(4)

        with c1:

            kpi_card(

                "Silhouette",

                round(silhouette,3),

                "📊",

                "#2563EB",

                "Separación"

            )

        with c2:

            kpi_card(

                "Davies",

                round(davies,3),

                "📈",

                "#10B981",

                "Compacidad"

            )

        with c3:

            kpi_card(

                "Calinski",

                round(calinski,1),

                "📉",

                "#7C3AED",

                "Dispersión"

            )

        with c4:

            kpi_card(

                "Estado",

                estado,

                "🎯",

                "#F59E0B",

                "Calidad"

            )

        st.divider()

        st.markdown("### Interpretación")

        texto = []

        if silhouette > 0.70:

            texto.append(
                "✔ Los clusters presentan una excelente separación."
            )

        elif silhouette > 0.50:

            texto.append(
                "✔ La segmentación es adecuada para análisis."
            )

        else:

            texto.append(
                "⚠ Se recomienda revisar el número de clusters."
            )

        if davies < 0.70:

            texto.append(
                "✔ Existe una buena compactación entre observaciones."
            )

        else:

            texto.append(
                "⚠ Algunos clusters presentan solapamiento."
            )

        if calinski > 100:

            texto.append(
                "✔ El modelo muestra una estructura consistente."
            )

        for linea in texto:

            st.success(linea)

        st.info(
            """
Estas métricas permiten evaluar objetivamente la calidad
de la segmentación antes de utilizar los clusters para
la toma de decisiones.
"""
        )
    @staticmethod
    def business_analysis(

        resultado,

        perfil,

        estadisticos,

        insights

    ):

        st.divider()

        st.subheader("💼 Business Intelligence")

        resumen = ClusterProfile.resumen(resultado)

        ranking = resumen.sort_values(

            "Registros",

            ascending=False

        ).copy()

        ranking["Ranking"] = range(

            1,

            len(ranking)+1

        )

        ranking = ranking[[

            "Ranking",

            "Cluster",

            "Registros",

            "Porcentaje"

        ]]

        st.markdown("### 🏆 Ranking de Clusters")

        st.dataframe(

            ranking,

            use_container_width=True,

            height=250

        )

        st.divider()

        st.markdown("### 🎯 Variables más representativas")

        for item in insights:

            with st.expander(

                f"Cluster {item['Cluster']}",

                expanded=False

            ):

                st.metric(

                    "Participación",

                    f"{item['Porcentaje']} %"

                )

                st.metric(

                    "Variable Dominante",

                    item["Variable Dominante"]

                )

                st.metric(

                    "Homogeneidad",

                    item["Homogeneidad"]

                )

                st.write(

                    item["Interpretación"]

                )

        st.divider()

        st.markdown("### ⭐ Registros representativos")

        cluster = st.selectbox(

            "Seleccione Cluster",

            sorted(resultado["Cluster"].unique()),

            key="cluster_top"

        )

        cantidad = st.slider(

            "Número de registros",

            5,

            50,

            10,

            key="cluster_top_n"

        )

        datos = resultado[

            resultado["Cluster"] == cluster

        ]

        numericas = datos.select_dtypes(

            include="number"

        ).columns.tolist()

        numericas.remove("Cluster")

        centroide = datos[numericas].mean()

        distancias = (

            (datos[numericas] - centroide)

            ** 2

        ).sum(axis=1)

        datos = datos.copy()

        datos["Distancia"] = distancias

        datos = datos.sort_values(

            "Distancia"

        )

        st.dataframe(

            datos.head(cantidad),

            use_container_width=True,

            height=350

        )

        st.info(

            """
Los registros mostrados son los más cercanos
al centroide del cluster y representan los
ejemplos más característicos del segmento.
"""

        )
    @staticmethod
    def cluster_health_score(

        resultado,

        estadisticos

    ):

        st.divider()

        st.subheader("🩺 Cluster Health Score")

        filas = []

        for cluster in sorted(resultado["Cluster"].unique()):

            datos = resultado[
                resultado["Cluster"] == cluster
            ]

            registros = len(datos)

            porcentaje = round(
                registros / len(resultado) * 100,
                2
            )

            variables = estadisticos[
                estadisticos["Cluster"] == cluster
            ]

            dispersion = variables["Std"].mean()

            score = 100

            # Penalización por dispersión
            score -= dispersion * 4

            # Penalización por tamaño muy pequeño
            if porcentaje < 5:
                score -= 20

            elif porcentaje < 10:
                score -= 10

            score = max(
                0,
                min(
                    100,
                    round(score,1)
                )
            )

            if score >= 90:
                estado = "🟢 Excelente"

            elif score >= 75:
                estado = "🟡 Bueno"

            elif score >= 60:
                estado = "🟠 Regular"

            else:
                estado = "🔴 Revisar"

            filas.append({

                "Cluster": cluster,

                "Registros": registros,

                "Participación (%)": porcentaje,

                "Dispersión": round(dispersion,2),

                "Health Score": score,

                "Estado": estado

            })

        import pandas as pd

        health = pd.DataFrame(filas)

        c1,c2,c3 = st.columns(3)

        with c1:

            st.metric(

                "Health Promedio",

                round(

                    health["Health Score"].mean(),

                    1

                )

            )

        with c2:

            st.metric(

                "Mejor Cluster",

                int(

                    health.loc[
                        health["Health Score"].idxmax(),
                        "Cluster"
                    ]

                )

            )

        with c3:

            st.metric(

                "Cluster Crítico",

                int(

                    health.loc[
                        health["Health Score"].idxmin(),
                        "Cluster"
                    ]

                )

            )

        st.dataframe(

            health,

            use_container_width=True,

            height=350

        )

        st.bar_chart(

            health.set_index(

                "Cluster"

            )["Health Score"]

        )

    @staticmethod
    def executive_business_report(

        resultado,

        perfil,

        insights,

        health

    ):

        st.divider()

        st.subheader("📑 Executive Business Report")

        st.caption(
            "Resumen ejecutivo generado automáticamente."
        )

        mejor = health.loc[
            health["Health Score"].idxmax()
        ]

        peor = health.loc[
            health["Health Score"].idxmin()
        ]

        total_clusters = resultado["Cluster"].nunique()

        total_registros = len(resultado)

        st.info(f"""

### Resumen Ejecutivo

El algoritmo identificó **{total_clusters} clusters**
sobre **{total_registros:,} registros**.

El segmento con mejor comportamiento es el
**Cluster {int(mejor['Cluster'])}**
con un Health Score de
**{mejor['Health Score']}**.

El segmento que requiere mayor revisión es el
**Cluster {int(peor['Cluster'])}**
con un Health Score de
**{peor['Health Score']}**.

La segmentación obtenida permite diferenciar
claramente grupos con características propias,
lo que facilita estrategias comerciales,
operativas y analíticas.

""")

        st.divider()

        st.markdown("## 📊 Recomendaciones Estratégicas")

        for item in insights:

            cluster = item["Cluster"]

            with st.expander(
                f"Cluster {cluster}",
                expanded=False
            ):

                st.markdown(
                    f"### Cluster {cluster}"
                )

                c1, c2 = st.columns(2)

                with c1:

                    st.metric(
                        "Participación",
                        f"{item['Porcentaje']} %"
                    )

                    st.metric(
                        "Registros",
                        item["Registros"]
                    )

                    st.metric(
                        "Health Score",
                        health.loc[
                            health["Cluster"] == cluster,
                            "Health Score"
                        ].values[0]
                    )

                with c2:

                    st.markdown(
                        "**Variable dominante**"
                    )

                    st.success(
                        item["Variable Dominante"]
                    )

                    st.markdown(
                        "**Interpretación**"
                    )

                    st.write(
                        item["Interpretación"]
                    )

                    st.markdown(
                        "**Acciones recomendadas**"
                    )

                    for r in item["Recomendaciones"]:

                        st.success(
                            "✔ " + r
                        )


    @staticmethod
    def business_scoring(
        resultado,
        insights,
        health
    ):

        st.divider()

        st.subheader("🏆 Business Scoring")

        filas = []

        for item in insights:

            cluster = item["Cluster"]

            score = float(

                health.loc[
                    health["Cluster"] == cluster,
                    "Health Score"
                ].values[0]

            )

            participacion = item["Porcentaje"]

            homogeneidad = item["Homogeneidad"]

            # ============================
            # Potencial Comercial
            # ============================

            potencial = score * 0.6 + participacion * 0.4

            if potencial >= 90:
                estrellas = "★★★★★"

            elif potencial >= 75:
                estrellas = "★★★★"

            elif potencial >= 60:
                estrellas = "★★★"

            elif potencial >= 40:
                estrellas = "★★"

            else:
                estrellas = "★"

            # ============================
            # Riesgo
            # ============================

            if score >= 90:

                riesgo = "🟢 Bajo"

            elif score >= 75:

                riesgo = "🟡 Medio"

            else:

                riesgo = "🔴 Alto"

            # ============================
            # Prioridad
            # ============================

            if potencial >= 85:

                prioridad = "🔥 Muy Alta"

            elif potencial >= 70:

                prioridad = "🟢 Alta"

            elif potencial >= 55:

                prioridad = "🟡 Media"

            else:

                prioridad = "⚪ Baja"

            filas.append({

                "Cluster": cluster,

                "Participación (%)": participacion,

                "Health Score": score,

                "Potencial": round(potencial,1),

                "Valor Comercial": estrellas,

                "Riesgo": riesgo,

                "Homogeneidad": homogeneidad,

                "Prioridad": prioridad

            })

        import pandas as pd

        ranking = pd.DataFrame(filas)

        ranking = ranking.sort_values(

            "Potencial",

            ascending=False

        )

        st.dataframe(

            ranking,

            use_container_width=True,

            height=320

        )

        st.bar_chart(

            ranking.set_index(

                "Cluster"

            )[

                "Potencial"

            ]

        )

        st.success(

            "Los clusters fueron priorizados automáticamente."

        )
        
    @staticmethod
    def business_scoring(
        resultado,
        insights,
        health
    ):

        st.divider()

        st.subheader("🏆 Business Scoring")

        filas = []

        for item in insights:

            cluster = item["Cluster"]

            score = float(

                health.loc[
                    health["Cluster"] == cluster,
                    "Health Score"
                ].values[0]

            )

            participacion = item["Porcentaje"]

            homogeneidad = item["Homogeneidad"]

            # ============================
            # Potencial Comercial
            # ============================

            potencial = score * 0.6 + participacion * 0.4

            if potencial >= 90:
                estrellas = "★★★★★"

            elif potencial >= 75:
                estrellas = "★★★★"

            elif potencial >= 60:
                estrellas = "★★★"

            elif potencial >= 40:
                estrellas = "★★"

            else:
                estrellas = "★"

            # ============================
            # Riesgo
            # ============================

            if score >= 90:

                riesgo = "🟢 Bajo"

            elif score >= 75:

                riesgo = "🟡 Medio"

            else:

                riesgo = "🔴 Alto"

            # ============================
            # Prioridad
            # ============================

            if potencial >= 85:

                prioridad = "🔥 Muy Alta"

            elif potencial >= 70:

                prioridad = "🟢 Alta"

            elif potencial >= 55:

                prioridad = "🟡 Media"

            else:

                prioridad = "⚪ Baja"

            filas.append({

                "Cluster": cluster,

                "Participación (%)": participacion,

                "Health Score": score,

                "Potencial": round(potencial,1),

                "Valor Comercial": estrellas,

                "Riesgo": riesgo,

                "Homogeneidad": homogeneidad,

                "Prioridad": prioridad

            })

        import pandas as pd

        ranking = pd.DataFrame(filas)

        ranking = ranking.sort_values(

            "Potencial",

            ascending=False

        )

        st.dataframe(

            ranking,

            use_container_width=True,

            height=320

        )

        st.bar_chart(

            ranking.set_index(

                "Cluster"

            )[

                "Potencial"

            ]

        )

        st.success(

            "Los clusters fueron priorizados automáticamente."

        )