import streamlit as st


class InsightDashboard:

    """
    =======================================================
    Dashboard Ejecutivo del Insight Engine

    Muestra los principales indicadores inteligentes
    generados por el motor de análisis.

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

        riesgo = InsightDashboard._calculate_risk(

            score

        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(

            "🎯 Score",

            f"{score}/100"

        )

        c2.metric(

            "🏆 Madurez",

            f"Nivel {madurez['nivel']}"

        )

        c3.metric(

            "📈 Estado",

            estado

        )

        c4.metric(

            "⚠️ Riesgo",

            riesgo

        )

        st.divider()

        c1, c2 = st.columns(

            [2, 1]

        )

        with c1:

            st.subheader(

                "Descripción"

            )

            st.info(

                madurez["descripcion"]

            )

        with c2:

            st.subheader(

                "Recomendación"

            )

            st.success(

                madurez["recomendacion"]

            )

    @staticmethod
    def _calculate_risk(

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