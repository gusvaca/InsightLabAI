"""
=========================================================
InsightLab AI Enterprise

Cluster AI Engine

Generador de narrativa basado en
Cluster Intelligence

=========================================================
"""

from ml.cluster_intelligence import ClusterIntelligence


class ClusterAI:

    def __init__(self, df):

        self.engine = ClusterIntelligence(df)

    # =====================================================
    # EXPLICAR UN CLUSTER
    # =====================================================

    def explain(self, cluster):

        info = self.engine.explain_cluster(cluster)

        texto = []

        texto.append(

            f"El Cluster {cluster} contiene "

            f"{info['Size']} registros."

        )

        texto.append(

            f"Presenta un Business Score de "

            f"{info['Business Score']:.2f}."

        )

        texto.append(

            f"Su Opportunity Score es "

            f"{info['Opportunity Score']:.2f}."

        )

        texto.append(

            f"El Risk Score calculado es "

            f"{info['Risk Score']:.2f}."

        )

        texto.append(

            f"La cohesión interna alcanza "

            f"{info['Cohesion']:.2f}."

        )

        texto.append(

            "Las variables que más caracterizan "

            "este segmento son:"

        )

        for variable in info["Main Features"]:

            texto.append(

                f"• {variable['Variable']} "

                f"({variable['Difference (%)']}%)"

            )

        return "\n".join(texto)

    # =====================================================
    # TODOS LOS CLUSTERS
    # =====================================================

    def explain_all(self):

        salida = {}

        for cluster in self.engine.clusters:

            salida[cluster] = self.explain(cluster)

        return salida
    
        # =====================================================
    # RESUMEN EJECUTIVO
    # =====================================================

    def executive_summary(self):

        report = self.engine.executive_report()

        texto = []

        texto.append(

            "RESUMEN EJECUTIVO"

        )

        texto.append("")

        texto.append(

            f"Registros analizados: "

            f"{report['General']['Records']}"

        )

        texto.append(

            f"Variables: "

            f"{report['General']['Variables']}"

        )

        texto.append(

            f"Clusters: "

            f"{report['General']['Clusters']}"

        )

        texto.append("")

        business = report["Quality"]["Business Score"]

        mejor = business.iloc[0]

        texto.append(

            f"El Cluster "

            f"{int(mejor['Cluster'])}"

            " presenta el mayor "

            "Business Score."

        )

        texto.append("")

        texto.append(

            "Se recomienda priorizar "

            "este segmento para "

            "las iniciativas "

            "estratégicas."

        )

        return "\n".join(texto)
    
        # =====================================================
    # REPORTE IA
    # =====================================================

    def report(self):

        reporte = {}

        reporte["summary"] = (

            self.executive_summary()

        )

        reporte["clusters"] = (

            self.explain_all()

        )

        return reporte