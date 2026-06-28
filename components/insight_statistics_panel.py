import streamlit as st


class InsightStatisticsPanel:

    """
    =======================================================
    Insight Statistics Panel

    Presenta un resumen ejecutivo de los indicadores
    generados por el Insight Intelligence Engine.

    =======================================================
    """

    @staticmethod
    def render(

        analysis

    ):

        resultado = analysis["resultado"]

        insights = resultado.insights

        recomendaciones = resultado.recomendaciones

        siguientes = analysis["siguientes_pasos"]

        st.subheader(

            "📈 Estadísticas del Análisis"

        )

        total = len(insights)

        altas = sum(

            1

            for i in insights

            if i.prioridad.lower() == "alta"

        )

        medias = sum(

            1

            for i in insights

            if i.prioridad.lower() == "media"

        )

        bajas = sum(

            1

            for i in insights

            if i.prioridad.lower() == "baja"

        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(

            "Insights",

            total

        )

        c2.metric(

            "Alta Prioridad",

            altas

        )

        c3.metric(

            "Media Prioridad",

            medias

        )

        c4.metric(

            "Baja Prioridad",

            bajas

        )

        st.divider()

        c1, c2 = st.columns(2)

        with c1:

            st.metric(

                "Recomendaciones",

                len(recomendaciones)

            )

        with c2:

            st.metric(

                "Próximos Pasos",

                len(siguientes)

            )

        st.divider()

        if total > 0:

            porcentaje = round(

                bajas * 100 / total,

                1

            )

            st.progress(

                porcentaje / 100

            )

            st.caption(

                f"{porcentaje}% de los insights corresponden a hallazgos de baja prioridad."

            )