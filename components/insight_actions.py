import streamlit as st


class InsightActions:

    """
    =======================================================

    Insight Action Center

    Convierte los resultados del Insight Engine
    en un plan de acción priorizado.

    =======================================================
    """

    @staticmethod
    def render(

        analysis

    ):

        st.subheader(

            "🚀 Plan de Acción Inteligente"

        )

        pasos = analysis.get(

            "siguientes_pasos",

            []

        )

        if not pasos:

            st.success(

                "No existen acciones pendientes."

            )

            return

        inmediatas = []
        recomendadas = []
        preventivas = []
        buenas = []

        for paso in pasos:

            estado = paso.get(

                "estado",

                ""

            ).lower()

            if "pendiente" in estado:

                inmediatas.append(

                    paso

                )

            elif "muy" in estado:

                recomendadas.append(

                    paso

                )

            elif "recomendado" in estado:

                preventivas.append(

                    paso

                )

            else:

                buenas.append(

                    paso

                )

        InsightActions._render_group(

            "🔴 Acciones Inmediatas",

            inmediatas,

            "error"

        )

        InsightActions._render_group(

            "🟠 Acciones Recomendadas",

            recomendadas,

            "warning"

        )

        InsightActions._render_group(

            "🟡 Acciones Preventivas",

            preventivas,

            "info"

        )

        InsightActions._render_group(

            "🟢 Buenas Prácticas",

            buenas,

            "success"

        )

    @staticmethod
    def _render_group(

        titulo,

        acciones,

        tipo

    ):

        if not acciones:

            return

        st.markdown(

            f"### {titulo}"

        )

        for accion in acciones:

            texto = (

                f"**{accion['titulo']}**"

            )

            if tipo == "error":

                st.error(

                    texto

                )

            elif tipo == "warning":

                st.warning(

                    texto

                )

            elif tipo == "info":

                st.info(

                    texto

                )

            else:

                st.success(

                    texto

                )