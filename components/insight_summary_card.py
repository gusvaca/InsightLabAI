import streamlit as st


class InsightSummaryCard:

    """
    =======================================================
    Executive Summary Card

    Tarjeta ejecutiva para mostrar un resumen compacto
    del análisis generado por el Insight Intelligence
    Engine.

    =======================================================
    """

    @staticmethod
    def render(

        analysis

    ):

        resultado = analysis["resultado"]

        madurez = analysis["madurez"]

        score = resultado.score

        estado = resultado.estado

        resumen = analysis["resumen"]

        color = InsightSummaryCard._color(

            score

        )

        st.markdown(

            f"""
<div style="
background:white;
border-left:8px solid {color};
padding:25px;
border-radius:12px;
box-shadow:0 4px 12px rgba(0,0,0,.08);
margin-bottom:25px;
">

<div style="
font-size:14px;
color:#64748B;
font-weight:600;
">

INSIGHT EXECUTIVE SUMMARY

</div>

<div style="
font-size:28px;
font-weight:700;
color:#0F172A;
margin-top:10px;
">

{estado}

</div>

<div style="
margin-top:10px;
font-size:17px;
color:#475569;
">

Score General:
<b>{score}/100</b>

<br>

Nivel de Madurez:
<b>{madurez["nombre"]}</b>

</div>

</div>
""",

            unsafe_allow_html=True

        )

        st.info(

            resumen

        )

    @staticmethod
    def _color(

        score

    ):

        if score >= 95:

            return "#16A34A"

        if score >= 85:

            return "#2563EB"

        if score >= 70:

            return "#D97706"

        return "#DC2626"