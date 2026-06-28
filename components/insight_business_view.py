import streamlit as st


class InsightBusinessView:

    """
    =======================================================
    Business Executive View

    Presenta los resultados desde la perspectiva
    del negocio.

    =======================================================
    """

    @staticmethod
    def render(

        analysis

    ):

        negocio = analysis.get(

            "negocio",

            []

        )

        madurez = analysis.get(

            "madurez",

            {}

        )

        resultado = analysis["resultado"]

        score = resultado.score

        st.subheader(

            "🏢 Business Executive View"

        )

        c1, c2 = st.columns(

            [2, 1]

        )

        with c1:

            st.markdown(

                "### 📌 Impacto para el Negocio"

            )

            if negocio:

                for mensaje in negocio:

                    st.info(

                        mensaje

                    )

            else:

                st.success(

                    "No se identificaron impactos relevantes."

                )

        with c2:

            st.markdown(

                "### 📊 Estado Ejecutivo"

            )

            st.metric(

                "Score",

                f"{score}/100"

            )

            st.metric(

                "Madurez",

                madurez.get(

                    "nombre",

                    "N/D"

                )

            )

            st.metric(

                "Nivel",

                madurez.get(

                    "nivel",

                    "-"

                )

            )

        st.divider()

        st.markdown(

            "### 🎯 Beneficios Esperados"

        )

        beneficios = []

        if score >= 95:

            beneficios = [

                "Mayor confianza en los análisis.",

                "Reducción del riesgo analítico.",

                "Modelos más confiables.",

                "Mejor toma de decisiones."

            ]

        elif score >= 80:

            beneficios = [

                "Dataset apto para analítica.",

                "Preparación mínima requerida.",

                "Posibilidad de iniciar modelos predictivos."

            ]

        else:

            beneficios = [

                "Es necesario mejorar la calidad antes de iniciar proyectos analíticos."

            ]

        for beneficio in beneficios:

            st.success(

                beneficio

            )

        st.divider()

        st.markdown(

            "### 🚀 Valor para la Organización"

        )

        valor = InsightBusinessView._value(

            score

        )

        st.info(

            valor

        )

    @staticmethod
    def _value(

        score

    ):

        if score >= 95:

            return (

                "El conjunto de datos puede utilizarse "

                "como base para iniciativas de "

                "Machine Learning, Analítica Avanzada "

                "e Inteligencia Artificial."

            )

        if score >= 80:

            return (

                "El conjunto de datos ofrece una base "

                "adecuada para iniciativas de analítica "

                "descriptiva y predictiva."

            )

        return (

            "Se recomienda fortalecer la calidad "

            "del conjunto de datos antes de utilizarlo "

            "para procesos estratégicos."

        )