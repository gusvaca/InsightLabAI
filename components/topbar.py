import streamlit as st

from analytics.quality import DataQuality


class TopBar:

    @staticmethod
    def render(df=None):

        st.markdown(
        """
        <style>

        .topbar{

            background:linear-gradient(90deg,#2563EB,#1D4ED8);

            color:white;

            padding:18px;

            border-radius:15px;

            margin-bottom:20px;

            box-shadow:0 4px 12px rgba(0,0,0,.12);

        }

        .title{

            font-size:30px;

            font-weight:bold;

        }

        .subtitle{

            font-size:15px;

            opacity:.9;

        }

        </style>

        """,

        unsafe_allow_html=True

        )

        st.markdown(

        """
        <div class="topbar">

        <div class="title">

        📊 InsightLab AI Enterprise

        </div>

        <div class="subtitle">

        Intelligent Data Analytics Platform

        </div>

        </div>

        """,

        unsafe_allow_html=True

        )

        if df is not None:

            resumen = DataQuality.resumen(df)

            c1,c2,c3,c4,c5 = st.columns(5)

            c1.metric(
                "📄 Registros",
                f"{resumen['filas']:,}"
            )

            c2.metric(
                "📊 Variables",
                resumen["columnas"]
            )

            c3.metric(
                "💾 Memoria",
                f"{resumen['memoria']} MB"
            )

            c4.metric(
                "🎯 Calidad",
                resumen["score"]
            )

            c5.metric(
                "🟢 Estado",
                resumen["estado"]
            )

            st.divider()