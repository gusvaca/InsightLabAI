import streamlit as st


class InsightRiskMatrix:

    """
    =======================================================
    Insight Risk Matrix

    Presenta una matriz ejecutiva de riesgos basada en los
    insights generados por el motor inteligente.

    =======================================================
    """

    @staticmethod
    def render(

        analysis

    ):

        resultado = analysis["resultado"]

        insights = resultado.insights

        critico = []

        alto = []

        medio = []

        bajo = []

        for insight in insights:

            prioridad = insight.prioridad.lower()

            if prioridad == "alta":

                alto.append(insight)

            elif prioridad == "media":

                medio.append(insight)

            elif prioridad == "baja":

                bajo.append(insight)

            else:

                critico.append(insight)

        st.subheader(

            "⚠️ Matriz de Riesgos"

        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(

            "🔴 Crítico",

            len(critico)

        )

        c2.metric(

            "🟠 Alto",

            len(alto)

        )

        c3.metric(

            "🟡 Medio",

            len(medio)

        )

        c4.metric(

            "🟢 Bajo",

            len(bajo)

        )

        st.divider()

        InsightRiskMatrix._section(

            "🔴 Riesgos Críticos",

            critico,

            "error"

        )

        InsightRiskMatrix._section(

            "🟠 Riesgos Altos",

            alto,

            "warning"

        )

        InsightRiskMatrix._section(

            "🟡 Riesgos Medios",

            medio,

            "info"

        )

        InsightRiskMatrix._section(

            "🟢 Riesgos Bajos",

            bajo,

            "success"

        )

    @staticmethod
    def _section(

        titulo,

        lista,

        tipo

    ):

        if not lista:

            return

        st.markdown(

            f"### {titulo}"

        )

        for insight in lista:

            texto = (

                f"**{insight.titulo}**\n\n"

                f"{insight.mensaje}\n\n"

                f"**Impacto:** {insight.impacto}"

            )

            if tipo == "error":

                st.error(texto)

            elif tipo == "warning":

                st.warning(texto)

            elif tipo == "info":

                st.info(texto)

            else:

                st.success(texto)