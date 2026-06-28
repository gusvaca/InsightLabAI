"""
=========================================================
InsightLab AI Enterprise

Cluster DNA Dashboard

=========================================================
"""

import streamlit as st
import plotly.graph_objects as go


class ClusterDNA:

    @staticmethod
    def radar(dna, cluster):

        fila = dna[
            dna.Cluster == cluster
        ].iloc[0]

        categorias = [

            "Business",

            "Opportunity",

            "Confidence",

            "Stability",

            "Risk"

        ]

        valores = [

            fila["Business"],

            fila["Opportunity"],

            fila["Confidence"],

            fila["Stability"],

            100 - fila["Risk"]

        ]

        fig = go.Figure()

        fig.add_trace(

            go.Scatterpolar(

                r=valores,

                theta=categorias,

                fill="toself",

                name=f"Cluster {cluster}"

            )

        )

        fig.update_layout(

            polar=dict(

                radialaxis=dict(

                    visible=True,

                    range=[0,100]

                )

            ),

            showlegend=False,

            height=500

        )

        return fig
    