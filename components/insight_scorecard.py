import streamlit as st


class InsightScorecard:

    """
    =======================================================
    Executive Scorecard

    Consolida los principales indicadores generados por el
    Insight Intelligence Engine.

    =======================================================
    """

    @staticmethod
    def render(

        analysis

    ):

        resultado = analysis["resultado"]

        madurez = analysis["madurez"]

        recomendaciones = resultado.recomendaciones

        siguientes = analysis["siguientes_pasos"]

        insights = resultado.insights

        score = resultado.score

        estado = resultado.estado

        riesgo = InsightScorecard._risk(

            score

        )

        st.subheader(

            "📈 Executive Scorecard"

        )

        c1, c2, c3 = st.columns(3)

        c4, c5, c6 = st.columns(3)

        c1.metric(

            "🎯 Score",

            f"{score}/100"

        )

        c2.metric(

            "🏆 Madurez",

            madurez["nombre"]

        )

        c3.metric(

            "📊 Estado",

            estado

        )

        c4.metric(

            "⚠️ Riesgo",

            riesgo

        )

        c5.metric(

            "💡 Insights",

            len(insights)

        )

        c6.metric(

            "✅ Recomendaciones",

            len(recomendaciones)

        )

        st.divider()

        progreso = InsightScorecard._progress(

            score

        )

        st.progress(

            progreso / 100

        )

        st.caption(

            f"Nivel de preparación: {progreso}%"

        )

        if siguientes:

            st.markdown(

                "### 🚀 Próximos pasos"

            )

            for paso in siguientes:

                st.markdown(

                    f"- **{paso['titulo']}** ({paso['estado']})"

                )

    @staticmethod
    def _risk(

        score

    ):

        if score >= 95:

            return "Muy Bajo"

        if score >= 85:

            return "Bajo"

        if score >= 70:

            return "Medio"

        if score >= 50:

            return "Alto"

        return "Crítico"

    @staticmethod
    def _progress(

        score

    ):

        if score >= 95:

            return 100

        if score >= 85:

            return 85

        if score >= 70:

            return 70

        if score >= 50:

            return 50

        return 25