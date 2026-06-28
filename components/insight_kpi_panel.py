import streamlit as st


class InsightKPIPanel:

    """
    =======================================================
    Insight KPI Panel

    Consolida los principales indicadores ejecutivos
    generados por el Insight Intelligence Engine.

    =======================================================
    """

    @staticmethod
    def render(

        analysis

    ):

        resultado = analysis["resultado"]

        madurez = analysis["madurez"]

        siguientes = analysis["siguientes_pasos"]

        insights = resultado.insights

        recomendaciones = resultado.recomendaciones

        score = resultado.score

        st.subheader(

            "📊 Executive KPI Panel"

        )

        kpi1, kpi2, kpi3, kpi4 = st.columns(4)

        kpi5, kpi6, kpi7, kpi8 = st.columns(4)

        # ==========================================
        # PRIMERA FILA
        # ==========================================

        kpi1.metric(

            "🎯 Calidad",

            f"{score:.1f}"

        )

        kpi2.metric(

            "🏆 Madurez",

            madurez["nivel"]

        )

        kpi3.metric(

            "📋 Insights",

            len(insights)

        )

        kpi4.metric(

            "💡 Recomendaciones",

            len(recomendaciones)

        )

        # ==========================================
        # SEGUNDA FILA
        # ==========================================

        riesgo = InsightKPIPanel._risk(

            score

        )

        confianza = InsightKPIPanel._confidence(

            score

        )

        kpi5.metric(

            "⚠️ Riesgo",

            riesgo

        )

        kpi6.metric(

            "🤖 ML Ready",

            "Sí" if madurez["nivel"] >= 4 else "No"

        )

        kpi7.metric(

            "🚀 Próximos Pasos",

            len(siguientes)

        )

        kpi8.metric(

            "🔒 Confianza",

            confianza

        )

        st.divider()

        st.progress(

            score / 100

        )

        st.caption(

            f"Índice Global de Calidad: {score:.1f}%"

        )

    @staticmethod
    def _risk(

        score

    ):

        if score >= 95:

            return "Muy Bajo"

        elif score >= 85:

            return "Bajo"

        elif score >= 70:

            return "Medio"

        elif score >= 50:

            return "Alto"

        else:

            return "Crítico"

    @staticmethod
    def _confidence(

        score

    ):

        if score >= 95:

            return "Muy Alta"

        elif score >= 85:

            return "Alta"

        elif score >= 70:

            return "Media"

        elif score >= 50:

            return "Baja"

        else:

            return "Muy Baja"