"""
=========================================================
InsightLab AI Enterprise
Archivo : cluster_charts.py
Descripción:
Visualizaciones para análisis de Clusters
=========================================================
"""

import numpy as np
import pandas as pd
import plotly.express as px

from components.theme import ChartTheme


class ClusterCharts:

    @staticmethod
    def distribucion(df):

        datos = (
            df["Cluster"]
            .value_counts()
            .sort_index()
            .reset_index()
        )

        datos.columns = [
            "Cluster",
            "Registros"
        ]

        fig = px.bar(

            datos,

            x="Cluster",

            y="Registros",

            text="Registros",

            color="Cluster",

            color_discrete_sequence=ChartTheme.colors()

        )

        fig.update_traces(textposition="outside")

        fig.update_layout(

            title="Distribución de Registros por Cluster",

            showlegend=False,

            height=420

        )

        return ChartTheme.apply(fig)

    @staticmethod
    def heatmap(df):

        columnas = df.select_dtypes(
            include=np.number
        ).columns.tolist()

        columnas.remove("Cluster")

        datos = (

            df

            .groupby("Cluster")[columnas]

            .mean()

            .round(2)

        )

        fig = px.imshow(

            datos,

            text_auto=True,

            color_continuous_scale="RdYlBu_r",

            aspect="auto"

        )

        fig.update_layout(

            title="Heatmap de Centroides"

        )

        return ChartTheme.apply(fig)

    @staticmethod
    def radar(df):

        columnas = df.select_dtypes(
            include=np.number
        ).columns.tolist()

        columnas.remove("Cluster")

        medias = (

            df

            .groupby("Cluster")[columnas]

            .mean()

        )

        fig = px.line_polar()

        for cluster in medias.index:

            fig.add_scatterpolar(

                r=medias.loc[cluster],

                theta=columnas,

                fill="toself",

                name=f"Cluster {cluster}"

            )

        fig.update_layout(

            title="Perfil de Clusters",

            height=650

        )

        return ChartTheme.apply(fig)

    @staticmethod
    def boxplots(df):

        columnas = df.select_dtypes(
            include=np.number
        ).columns.tolist()

        columnas.remove("Cluster")

        variable = columnas[0]

        fig = px.box(

            df,

            x="Cluster",

            y=variable,

            color="Cluster",

            points="outliers",

            color_discrete_sequence=ChartTheme.colors()

        )

        fig.update_layout(

            title=f"Comparación por Cluster ({variable})"

        )

        return ChartTheme.apply(fig)

    @staticmethod
    def centroides(df):

        columnas = df.select_dtypes(
            include=np.number
        ).columns.tolist()

        columnas.remove("Cluster")

        datos = (

            df

            .groupby("Cluster")[columnas]

            .mean()

            .reset_index()

        )

        fig = px.scatter(

            datos,

            x=columnas[0],

            y=columnas[1],

            size=columnas[2] if len(columnas) > 2 else None,

            color="Cluster",

            text="Cluster",

            color_discrete_sequence=ChartTheme.colors()

        )

        fig.update_layout(

            title="Centroides"

        )

        return ChartTheme.apply(fig)

    @staticmethod
    def barras_medias(df):

        columnas = df.select_dtypes(
            include=np.number
        ).columns.tolist()

        columnas.remove("Cluster")

        datos = (

            df

            .groupby("Cluster")[columnas]

            .mean()

            .reset_index()

        )

        datos = datos.melt(

            id_vars="Cluster",

            var_name="Variable",

            value_name="Valor"

        )

        fig = px.bar(

            datos,

            x="Variable",

            y="Valor",

            color="Cluster",

            barmode="group",

            color_discrete_sequence=ChartTheme.colors()

        )

        fig.update_layout(

            title="Comparación de Variables"

        )

        return ChartTheme.apply(fig)