"""
=========================================================
InsightLab AI Enterprise
Archivo : theme.py
Descripción:
Tema visual para todos los gráficos Plotly.
=========================================================
"""

import plotly.graph_objects as go


class ChartTheme:

    PRIMARY = "#2563EB"
    SECONDARY = "#7C3AED"
    SUCCESS = "#16A34A"
    WARNING = "#F59E0B"
    DANGER = "#DC2626"
    INFO = "#06B6D4"
    PINK = "#EC4899"
    TEAL = "#14B8A6"

    BACKGROUND = "#FFFFFF"
    GRID = "#E2E8F0"
    FONT = "Arial"

    @staticmethod
    def colors():
        """
        Paleta corporativa utilizada por todos los gráficos.
        """
        return [
            ChartTheme.PRIMARY,
            ChartTheme.SECONDARY,
            ChartTheme.SUCCESS,
            ChartTheme.WARNING,
            ChartTheme.DANGER,
            ChartTheme.INFO,
            ChartTheme.PINK,
            ChartTheme.TEAL
        ]

    @staticmethod
    def apply(fig):

        fig.update_layout(

            template="plotly_white",

            paper_bgcolor=ChartTheme.BACKGROUND,

            plot_bgcolor=ChartTheme.BACKGROUND,

            font=dict(
                family=ChartTheme.FONT,
                size=13,
                color="#334155"
            ),

            margin=dict(
                l=25,
                r=25,
                t=50,
                b=25
            ),

            legend=dict(
                bgcolor="rgba(0,0,0,0)",
                borderwidth=0,
                orientation="h",
                y=-0.20
            ),

            hoverlabel=dict(
                bgcolor="white",
                font_size=13
            )

        )

        fig.update_xaxes(
            gridcolor=ChartTheme.GRID,
            zeroline=False
        )

        fig.update_yaxes(
            gridcolor=ChartTheme.GRID,
            zeroline=False
        )

        return fig