"""
=========================================================
InsightLab AI Enterprise
Archivo : cluster_profile.py
Descripción:
Perfil estadístico de los clusters
=========================================================
"""

import numpy as np
import pandas as pd


class ClusterProfile:

    @staticmethod
    def resumen(df):

        resumen = (
            df["Cluster"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        resumen.columns = [
            "Cluster",
            "Registros"
        ]

        resumen["Porcentaje"] = (
            resumen["Registros"] /
            len(df) *
            100
        ).round(2)

        return resumen

    @staticmethod
    def perfil(df):

        columnas = df.select_dtypes(
            include=np.number
        ).columns.tolist()

        if "Cluster" in columnas:
            columnas.remove("Cluster")

        perfil = (

            df

            .groupby("Cluster")[columnas]

            .mean()

            .round(2)

        )

        return perfil

    @staticmethod
    def estadisticos(df):

        columnas = df.select_dtypes(
            include=np.number
        ).columns.tolist()

        if "Cluster" in columnas:
            columnas.remove("Cluster")

        datos = []

        for cluster in sorted(df.Cluster.unique()):

            aux = df[df.Cluster == cluster]

            for col in columnas:

                datos.append({

                    "Cluster": cluster,

                    "Variable": col,

                    "Min": round(aux[col].min(),2),

                    "Q1": round(aux[col].quantile(.25),2),

                    "Media": round(aux[col].mean(),2),

                    "Mediana": round(aux[col].median(),2),

                    "Q3": round(aux[col].quantile(.75),2),

                    "Max": round(aux[col].max(),2),

                    "Std": round(aux[col].std(),2)

                })

        return pd.DataFrame(datos)

    @staticmethod
    def comparacion(df):

        columnas = df.select_dtypes(
            include=np.number
        ).columns.tolist()

        if "Cluster" in columnas:
            columnas.remove("Cluster")

        general = df[columnas].mean()

        filas = []

        for cluster in sorted(df.Cluster.unique()):

            aux = df[df.Cluster == cluster]

            for col in columnas:

                media = aux[col].mean()

                filas.append({

                    "Cluster": cluster,

                    "Variable": col,

                    "Media Cluster": round(media,2),

                    "Media General": round(general[col],2),

                    "Diferencia": round(media-general[col],2)

                })

        return pd.DataFrame(filas)