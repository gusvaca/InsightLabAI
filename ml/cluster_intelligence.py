"""
=========================================================
InsightLab AI Enterprise

Cluster Intelligence Engine

Motor Analítico para interpretación automática
de modelos de Clustering

=========================================================
"""

import numpy as np
import pandas as pd


class ClusterIntelligence:

    """
    =====================================================
    Cluster Intelligence Engine

    Motor analítico encargado de calcular métricas
    objetivas sobre modelos de clustering.

    Este módulo NO genera gráficos.

    Este módulo NO genera IA.

    Este módulo NO genera reportes.

    Su única responsabilidad es producir métricas que
    consumirán otros componentes del sistema.
    =====================================================
    """

    # =====================================================
    # CONSTRUCTOR
    # =====================================================

    def __init__(self, df):

        self.df = df.copy()

        if "Cluster" not in self.df.columns:

            raise ValueError(
                "El DataFrame debe contener la columna 'Cluster'."
            )

        self.numeric = self.df.select_dtypes(
            include=np.number
        ).columns.tolist()

        if "Cluster" in self.numeric:
            self.numeric.remove("Cluster")

        self.general = self.df[self.numeric]

        self.clusters = sorted(
            self.df["Cluster"].unique()
        )

    # =====================================================
    # DATASET SUMMARY
    # =====================================================

    def dataset_summary(self):

        memoria = (
            self.df.memory_usage(deep=True)
            .sum() / (1024 ** 2)
        )

        return {

            "records": len(self.df),

            "variables": len(self.df.columns),

            "numeric_variables": len(self.numeric),

            "clusters": len(self.clusters),

            "missing_values": int(
                self.df.isna().sum().sum()
            ),

            "duplicates": int(
                self.df.duplicated().sum()
            ),

            "memory_mb": round(
                memoria,
                2
            )

        }

    # =====================================================
    # DESCRIPTIVE STATISTICS
    # =====================================================

    def descriptive_statistics(self):

        resultados = []

        for cluster in self.clusters:

            datos_cluster = self.df[
                self.df["Cluster"] == cluster
            ]

            for variable in self.numeric:

                serie = datos_cluster[
                    variable
                ].dropna()

                if serie.empty:
                    continue

                resultados.append({

                    "Cluster": cluster,

                    "Variable": variable,

                    "Count": int(len(serie)),

                    "Mean": round(
                        serie.mean(),
                        4
                    ),

                    "Median": round(
                        serie.median(),
                        4
                    ),

                    "Std": round(
                        serie.std(),
                        4
                    ),

                    "Variance": round(
                        serie.var(),
                        4
                    ),

                    "Min": round(
                        serie.min(),
                        4
                    ),

                    "Q1": round(
                        serie.quantile(0.25),
                        4
                    ),

                    "Q3": round(
                        serie.quantile(0.75),
                        4
                    ),

                    "Max": round(
                        serie.max(),
                        4
                    ),

                    "Range": round(
                        serie.max() - serie.min(),
                        4
                    ),

                    "IQR": round(
                        serie.quantile(0.75)
                        - serie.quantile(0.25),
                        4
                    ),

                    "Skewness": round(
                        serie.skew(),
                        4
                    ),

                    "Kurtosis": round(
                        serie.kurt(),
                        4
                    )

                })

        return pd.DataFrame(resultados)
    
        # =====================================================
    # CLUSTER QUALITY
    # =====================================================

    def cluster_quality(self):

        """
        Calcula métricas de calidad para cada cluster.
        """

        filas = []

        for cluster in self.clusters:

            datos = self.df[
                self.df["Cluster"] == cluster
            ]

            compactacion = []

            for variable in self.numeric:

                media = datos[variable].mean()

                desviacion = datos[variable].std()

                if media == 0 or np.isnan(desviacion):

                    cv = 0

                else:

                    cv = abs(desviacion / media)

                compactacion.append(cv)

            compactacion = np.mean(compactacion)

            densidad = len(datos) / len(self.df)

            filas.append({

                "Cluster": cluster,

                "Records": len(datos),

                "Compactación": round(
                    1 / (1 + compactacion),
                    4
                ),

                "Densidad": round(
                    densidad,
                    4
                )

            })

        return pd.DataFrame(filas)
    
        # =====================================================
    # CLUSTER SEPARATION
    # =====================================================

    def cluster_separation(self):

        """
        Calcula la separación entre centroides de los clusters.
        Un mayor valor indica clusters mejor diferenciados.
        """

        centroides = []

        for cluster in self.clusters:

            datos = self.df[
                self.df["Cluster"] == cluster
            ][self.numeric]

            centroides.append(
                datos.mean().values
            )

        centroides = np.array(centroides)

        filas = []

        for i, cluster in enumerate(self.clusters):

            distancias = []

            for j in range(len(self.clusters)):

                if i == j:
                    continue

                distancia = np.linalg.norm(
                    centroides[i] - centroides[j]
                )

                distancias.append(distancia)

            filas.append({

                "Cluster": cluster,

                "Min Distance": round(
                    np.min(distancias),
                    4
                ),

                "Mean Distance": round(
                    np.mean(distancias),
                    4
                ),

                "Max Distance": round(
                    np.max(distancias),
                    4
                )

            })

        return pd.DataFrame(filas)
        # =====================================================
    # COHESION INDEX
    # =====================================================

    def cohesion_index(self):

        """
        Calcula un índice de cohesión basado en la
        compactación del cluster.
        """

        calidad = self.cluster_quality()

        filas = []

        for _, fila in calidad.iterrows():

            compactacion = fila["Compactación"]

            cohesion = compactacion * 100

            if cohesion >= 90:

                nivel = "Excelente"

            elif cohesion >= 75:

                nivel = "Alta"

            elif cohesion >= 60:

                nivel = "Media"

            elif cohesion >= 40:

                nivel = "Baja"

            else:

                nivel = "Muy Baja"

            filas.append({

                "Cluster": int(fila["Cluster"]),

                "Cohesion": round(
                    cohesion,
                    2
                ),

                "Level": nivel

            })

        return pd.DataFrame(filas)
        # =====================================================
    # FEATURE IMPORTANCE
    # =====================================================

    def feature_importance(self):

        """
        Calcula la importancia de cada variable
        dentro de cada cluster comparándola
        contra el promedio general del dataset.
        """

        media_general = self.general.mean()

        std_general = self.general.std()

        filas = []

        for cluster in self.clusters:

            datos = self.df[
                self.df["Cluster"] == cluster
            ]

            for variable in self.numeric:

                media_cluster = datos[variable].mean()

                media_dataset = media_general[variable]

                desviacion = std_general[variable]

                diferencia = media_cluster - media_dataset

                if media_dataset != 0:

                    diferencia_pct = (

                        diferencia /

                        abs(media_dataset)

                    ) * 100

                else:

                    diferencia_pct = 0

                if desviacion != 0:

                    zscore = (

                        diferencia /

                        desviacion

                    )

                else:

                    zscore = 0

                score = (

                    abs(zscore) * 60 +

                    abs(diferencia_pct) * 0.40

                )

                filas.append({

                    "Cluster": cluster,

                    "Variable": variable,

                    "Dataset Mean": round(

                        media_dataset,

                        4

                    ),

                    "Cluster Mean": round(

                        media_cluster,

                        4

                    ),

                    "Difference": round(

                        diferencia,

                        4

                    ),

                    "Difference (%)": round(

                        diferencia_pct,

                        2

                    ),

                    "Z-Score": round(

                        zscore,

                        4

                    ),

                    "Importance Score": round(

                        score,

                        2

                    )

                })

        importancia = pd.DataFrame(filas)

        importancia["Ranking"] = (

            importancia

            .groupby("Cluster")["Importance Score"]

            .rank(

                ascending=False,

                method="dense"

            )

        )

        return importancia.sort_values(

            [

                "Cluster",

                "Ranking"

            ]

        )
    
        # =====================================================
    # STATISTICAL VALIDATION
    # =====================================================

    def statistical_validation(self):

        """
        Evalúa si las variables presentan
        diferencias estadísticamente significativas
        entre los clusters.
        """

        from scipy.stats import f_oneway, kruskal

        filas = []

        for variable in self.numeric:

            grupos = []

            for cluster in self.clusters:

                serie = self.df[
                    self.df["Cluster"] == cluster
                ][variable].dropna()

                if len(serie) > 1:

                    grupos.append(serie)

            if len(grupos) < 2:

                continue

            try:

                f_stat, p_anova = f_oneway(*grupos)

            except:

                f_stat = np.nan

                p_anova = np.nan

            try:

                h_stat, p_kruskal = kruskal(*grupos)

            except:

                h_stat = np.nan

                p_kruskal = np.nan

            if pd.notna(p_anova):

                if p_anova < 0.001:

                    interpretacion = "Muy significativa"

                elif p_anova < 0.01:

                    interpretacion = "Significativa"

                elif p_anova < 0.05:

                    interpretacion = "Moderada"

                else:

                    interpretacion = "No significativa"

            else:

                interpretacion = "No evaluable"

            filas.append({

                "Variable": variable,

                "ANOVA F": round(
                    f_stat,
                    4
                ),

                "ANOVA p-value": round(
                    p_anova,
                    6
                ),

                "Kruskal H": round(
                    h_stat,
                    4
                ),

                "Kruskal p-value": round(
                    p_kruskal,
                    6
                ),

                "Interpretation": interpretacion

            })

        return pd.DataFrame(filas)
    
        # =====================================================
    # STATISTICAL RANKING
    # =====================================================

    def statistical_ranking(self):

        """
        Genera un ranking de variables
        según su significancia estadística.
        """

        ranking = self.statistical_validation().copy()

        if ranking.empty:

            return ranking

        ranking["Score"] = 0

        ranking.loc[
            ranking["ANOVA p-value"] < 0.001,
            "Score"
        ] = 100

        ranking.loc[
            (
                ranking["ANOVA p-value"] >= 0.001
            ) &
            (
                ranking["ANOVA p-value"] < 0.01
            ),
            "Score"
        ] = 90

        ranking.loc[
            (
                ranking["ANOVA p-value"] >= 0.01
            ) &
            (
                ranking["ANOVA p-value"] < 0.05
            ),
            "Score"
        ] = 75

        ranking.loc[
            ranking["ANOVA p-value"] >= 0.05,
            "Score"
        ] = 25

        ranking = ranking.sort_values(

            by=[

                "Score",

                "ANOVA F"

            ],

            ascending=[

                False,

                False

            ]

        ).reset_index(drop=True)

        ranking["Ranking"] = range(

            1,

            len(ranking)+1

        )

        return ranking
    
        # =====================================================
    # CLUSTER STRENGTH
    # =====================================================

    def cluster_strength(self):

        """
        Calcula la fuerza de cada cluster
        utilizando la importancia promedio
        de sus variables.
        """

        importancia = self.feature_importance()

        filas = []

        for cluster in self.clusters:

            datos = importancia[
                importancia["Cluster"] == cluster
            ]

            strength = datos[
                "Importance Score"
            ].mean()

            std = datos[
                "Importance Score"
            ].std()

            minimo = datos[
                "Importance Score"
            ].min()

            maximo = datos[
                "Importance Score"
            ].max()

            if strength >= 90:

                nivel = "Muy Alta"

            elif strength >= 75:

                nivel = "Alta"

            elif strength >= 60:

                nivel = "Media"

            elif strength >= 40:

                nivel = "Baja"

            else:

                nivel = "Muy Baja"

            filas.append({

                "Cluster": cluster,

                "Strength": round(
                    strength,
                    2
                ),

                "Min Score": round(
                    minimo,
                    2
                ),

                "Max Score": round(
                    maximo,
                    2
                ),

                "Std": round(
                    std,
                    2
                ),

                "Level": nivel

            })

        return pd.DataFrame(filas)
    
        # =====================================================
    # BUSINESS SCORE
    # =====================================================

    def business_score(self):

        """
        Calcula un Business Score por cluster
        combinando tamaño, cohesión, calidad
        e importancia estadística.
        """

        profile = self.cluster_profile()

        quality = self.cluster_quality()

        cohesion = self.cohesion_index()

        strength = self.cluster_strength()

        filas = []

        for cluster in self.clusters:

            p = profile[
                profile["Cluster"] == cluster
            ].iloc[0]

            q = quality[
                quality["Cluster"] == cluster
            ].iloc[0]

            c = cohesion[
                cohesion["Cluster"] == cluster
            ].iloc[0]

            s = strength[
                strength["Cluster"] == cluster
            ].iloc[0]

            score = (

                p["Percentage"] * 0.20 +

                q["Compactación"] * 100 * 0.30 +

                c["Cohesion"] * 0.20 +

                s["Strength"] * 0.30

            )

            score = min(

                round(score,2),

                100

            )

            if score >= 90:

                nivel = "Excelente"

            elif score >= 80:

                nivel = "Muy Alto"

            elif score >= 70:

                nivel = "Alto"

            elif score >= 60:

                nivel = "Medio"

            else:

                nivel = "Bajo"

            filas.append({

                "Cluster": cluster,

                "Business Score": score,

                "Level": nivel

            })

        return pd.DataFrame(filas)
    
        # =====================================================
    # RISK SCORE
    # =====================================================

    def risk_score(self):

        """
        Calcula un índice de riesgo para cada cluster.
        Un cluster es más riesgoso cuando presenta:

        - Baja cohesión
        - Baja compactación
        - Baja fuerza estadística
        """

        quality = self.cluster_quality()

        cohesion = self.cohesion_index()

        strength = self.cluster_strength()

        filas = []

        for cluster in self.clusters:

            q = quality[
                quality["Cluster"] == cluster
            ].iloc[0]

            c = cohesion[
                cohesion["Cluster"] == cluster
            ].iloc[0]

            s = strength[
                strength["Cluster"] == cluster
            ].iloc[0]

            riesgo = (

                (100 - q["Compactación"] * 100) * 0.40 +

                (100 - c["Cohesion"]) * 0.30 +

                (100 - s["Strength"]) * 0.30

            )

            riesgo = max(

                0,

                min(

                    round(riesgo,2),

                    100

                )

            )

            if riesgo <= 20:

                nivel = "Muy Bajo"

            elif riesgo <= 40:

                nivel = "Bajo"

            elif riesgo <= 60:

                nivel = "Medio"

            elif riesgo <= 80:

                nivel = "Alto"

            else:

                nivel = "Crítico"

            filas.append({

                "Cluster": cluster,

                "Risk Score": riesgo,

                "Level": nivel

            })

        return pd.DataFrame(filas)
    
        # =====================================================
    # OPPORTUNITY SCORE
    # =====================================================

    def opportunity_score(self):

        """
        Calcula el potencial de oportunidad
        de cada cluster combinando:

        - Business Score
        - Risk Score
        """

        business = self.business_score()

        risk = self.risk_score()

        filas = []

        for cluster in self.clusters:

            b = business[
                business["Cluster"] == cluster
            ].iloc[0]

            r = risk[
                risk["Cluster"] == cluster
            ].iloc[0]

            oportunidad = (

                b["Business Score"] * 0.70 +

                (100 - r["Risk Score"]) * 0.30

            )

            oportunidad = round(

                min(oportunidad,100),

                2

            )

            if oportunidad >= 90:

                prioridad = "Muy Alta"

            elif oportunidad >= 80:

                prioridad = "Alta"

            elif oportunidad >= 70:

                prioridad = "Media"

            elif oportunidad >= 60:

                prioridad = "Baja"

            else:

                prioridad = "Muy Baja"

            filas.append({

                "Cluster": cluster,

                "Opportunity Score": oportunidad,

                "Priority": prioridad

            })

        return pd.DataFrame(filas)
    
        # =====================================================
    # STABILITY SCORE
    # =====================================================

    def stability_score(self):

        """
        Calcula la estabilidad de cada cluster
        utilizando el Coeficiente de Variación (CV)
        promedio de sus variables.
        """

        estadisticas = self.descriptive_statistics()

        filas = []

        for cluster in self.clusters:

            datos = estadisticas[
                estadisticas["Cluster"] == cluster
            ].copy()

            cvs = []

            for _, fila in datos.iterrows():

                media = fila["Mean"]

                desviacion = fila["Std"]

                if media == 0 or np.isnan(media):

                    cv = 1

                else:

                    cv = abs(desviacion / media)

                cvs.append(cv)

            cv_promedio = np.mean(cvs)

            estabilidad = (

                1 / (1 + cv_promedio)

            ) * 100

            estabilidad = round(

                estabilidad,

                2

            )

            if estabilidad >= 90:

                nivel = "Muy Alta"

            elif estabilidad >= 80:

                nivel = "Alta"

            elif estabilidad >= 70:

                nivel = "Media"

            elif estabilidad >= 60:

                nivel = "Baja"

            else:

                nivel = "Muy Baja"

            filas.append({

                "Cluster": cluster,

                "Average CV": round(

                    cv_promedio,

                    4

                ),

                "Stability": estabilidad,

                "Level": nivel

            })

        return pd.DataFrame(filas)
    
        # =====================================================
    # CONFIDENCE SCORE
    # =====================================================

    def confidence_score(self):

        """
        Calcula la confianza del análisis
        para cada cluster.

        Se basa en:

        - Business Score
        - Stability
        - Cohesion
        - Strength
        """

        business = self.business_score()

        stability = self.stability_score()

        cohesion = self.cohesion_index()

        strength = self.cluster_strength()

        filas = []

        for cluster in self.clusters:

            b = business[
                business["Cluster"] == cluster
            ].iloc[0]

            s = stability[
                stability["Cluster"] == cluster
            ].iloc[0]

            c = cohesion[
                cohesion["Cluster"] == cluster
            ].iloc[0]

            st = strength[
                strength["Cluster"] == cluster
            ].iloc[0]

            confidence = (

                b["Business Score"] * 0.35 +

                s["Stability"] * 0.25 +

                c["Cohesion"] * 0.20 +

                st["Strength"] * 0.20

            )

            confidence = round(

                min(confidence, 100),

                2

            )

            if confidence >= 90:

                nivel = "Muy Alta"

            elif confidence >= 80:

                nivel = "Alta"

            elif confidence >= 70:

                nivel = "Media"

            elif confidence >= 60:

                nivel = "Baja"

            else:

                nivel = "Muy Baja"

            filas.append({

                "Cluster": cluster,

                "Confidence": confidence,

                "Level": nivel

            })

        return pd.DataFrame(filas)
    
        # =====================================================
    # CLUSTER PROFILE
    # =====================================================

    def cluster_profile(self):

        """
        Resume las principales características
        de cada cluster.
        """

        filas = []

        total = len(self.df)

        for cluster in self.clusters:

            datos = self.df[
                self.df["Cluster"] == cluster
            ]

            filas.append({

                "Cluster": cluster,

                "Records": len(datos),

                "Percentage": round(
                    len(datos) / total * 100,
                    2
                ),

                "Variables": len(self.numeric)

            })

        return pd.DataFrame(filas)
    

        # =====================================================
    # EXPLAIN CLUSTER
    # =====================================================

    def explain_cluster(self, cluster):

        """
        Genera una explicación ejecutiva
        de un cluster específico.
        """

        if cluster not in self.clusters:

            raise ValueError(
                f"El cluster {cluster} no existe."
            )

        business = self.business_score()

        risk = self.risk_score()

        opportunity = self.opportunity_score()

        stability = self.stability_score()

        confidence = self.confidence_score()

        importance = self.feature_importance()

        business_row = business[
            business["Cluster"] == cluster
        ].iloc[0]

        risk_row = risk[
            risk["Cluster"] == cluster
        ].iloc[0]

        opportunity_row = opportunity[
            opportunity["Cluster"] == cluster
        ].iloc[0]

        stability_row = stability[
            stability["Cluster"] == cluster
        ].iloc[0]

        confidence_row = confidence[
            confidence["Cluster"] == cluster
        ].iloc[0]

        top_variables = (

            importance[
                importance["Cluster"] == cluster
            ]

            .sort_values(

                "Importance Score",

                ascending=False

            )

            .head(5)

        )

        return {

            "Cluster": cluster,

            "Business Score": business_row["Business Score"],

            "Risk Score": risk_row["Risk Score"],

            "Opportunity Score": opportunity_row["Opportunity Score"],

            "Stability": stability_row["Stability"],

            "Confidence": confidence_row["Confidence"],

            "Top Variables": top_variables.reset_index(drop=True)

        }
    
        # =====================================================
    # EXPLAIN ALL CLUSTERS
    # =====================================================

    def explain_all_clusters(self):

        """
        Genera un resumen ejecutivo
        para todos los clusters.
        """

        filas = []

        for cluster in self.clusters:

            info = self.explain_cluster(cluster)

            top_variable = info[
                "Top Variables"
            ].iloc[0]["Variable"]

            filas.append({

                "Cluster": info["Cluster"],

                "Business Score": info["Business Score"],

                "Risk Score": info["Risk Score"],

                "Opportunity Score": info["Opportunity Score"],

                "Stability": info["Stability"],

                "Confidence": info["Confidence"],

                "Main Variable": top_variable

            })

        resumen = pd.DataFrame(filas)

        resumen = resumen.sort_values(

            "Business Score",

            ascending=False

        ).reset_index(drop=True)

        resumen["Ranking"] = range(

            1,

            len(resumen)+1

        )

        return resumen
    
        # =====================================================
    # CLUSTER BENCHMARK
    # =====================================================

    def cluster_benchmark(self):

        """
        Consolida todas las métricas de negocio
        y genera un benchmark entre clusters.
        """

        business = self.business_score()

        risk = self.risk_score()

        opportunity = self.opportunity_score()

        stability = self.stability_score()

        confidence = self.confidence_score()

        filas = []

        for cluster in self.clusters:

            b = business[
                business["Cluster"] == cluster
            ].iloc[0]

            r = risk[
                risk["Cluster"] == cluster
            ].iloc[0]

            o = opportunity[
                opportunity["Cluster"] == cluster
            ].iloc[0]

            s = stability[
                stability["Cluster"] == cluster
            ].iloc[0]

            c = confidence[
                confidence["Cluster"] == cluster
            ].iloc[0]

            overall = (

                b["Business Score"] * 0.30 +

                (100 - r["Risk Score"]) * 0.20 +

                o["Opportunity Score"] * 0.20 +

                s["Stability"] * 0.15 +

                c["Confidence"] * 0.15

            )

            overall = round(

                min(overall,100),

                2

            )

            if overall >= 90:

                recomendacion = "Priorizar"

            elif overall >= 80:

                recomendacion = "Mantener"

            elif overall >= 70:

                recomendacion = "Monitorear"

            else:

                recomendacion = "Revisar"

            filas.append({

                "Cluster": cluster,

                "Business Score": b["Business Score"],

                "Risk Score": r["Risk Score"],

                "Opportunity Score": o["Opportunity Score"],

                "Stability": s["Stability"],

                "Confidence": c["Confidence"],

                "Overall Score": overall,

                "Recommendation": recomendacion

            })

        benchmark = pd.DataFrame(filas)

        benchmark = benchmark.sort_values(

            "Overall Score",

            ascending=False

        ).reset_index(drop=True)

        benchmark["Ranking"] = range(

            1,

            len(benchmark)+1

        )

        columnas = [

            "Ranking",

            "Cluster",

            "Business Score",

            "Risk Score",

            "Opportunity Score",

            "Stability",

            "Confidence",

            "Overall Score",

            "Recommendation"

        ]

        return benchmark[columnas]
    
        # =====================================================
    # EXECUTIVE REPORT
    # =====================================================

    def executive_report(self):

        """
        Construye el reporte ejecutivo completo
        del modelo de clustering.

        Es el método principal que deberán consumir
        Dashboard, Reportes, APIs e IA.
        """

        resumen = self.dataset_summary()

        benchmark = self.cluster_benchmark()

        ranking = self.statistical_ranking()

        explicaciones = {}

        for cluster in self.clusters:

            explicaciones[int(cluster)] = (

                self.explain_cluster(cluster)

            )

        return {

            "Summary":{

                "Records":

                    resumen["records"],

                "Variables":

                    resumen["variables"],

                "Numeric Variables":

                    resumen["numeric_variables"],

                "Clusters":

                    resumen["clusters"],

                "Missing Values":

                    resumen["missing_values"],

                "Duplicates":

                    resumen["duplicates"],

                "Memory (MB)":

                    resumen["memory_mb"]

            },

            "Benchmark":

                benchmark,

            "Statistical Ranking":

                ranking,

            "Cluster Details":

                explicaciones

        }